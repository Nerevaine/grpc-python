import time
import logging
import click

import grpc
import geyser_pb2
import geyser_pb2_grpc


class TritonAuthMetadataPlugin(grpc.AuthMetadataPlugin):
    """
    Metadata wrapper for raw access token credentials (x-token).
    If x_token is empty or None, it won't add anything.
    """

    def __init__(self, x_token: str):
        self.x_token = x_token

    def __call__(self, context, callback):
        if self.x_token:
            metadata = (("x-token", self.x_token),)
            return callback(metadata, None)
        else:
            return callback((), None)


def make_subscribe_request(wallet_pubkey: str):
    """
    Builds a SubscribeRequest to listen for changes to a specific account.
    Equivalent to:
      accounts: {
        exampleAccount: {
          account: [wallet_pubkey],
          filters: []
        }
      }
    """
    req = geyser_pb2.SubscribeRequest()

    # 1) Add an entry to the "accounts" map
    account_filter = geyser_pb2.SubscribeRequestFilterAccounts()
    account_filter.account.extend([wallet_pubkey])
    # If you wanted an owner or lamport filter, you'd set it here. e.g. account_filter.owner.extend([...])
    req.accounts["exampleAccount"].CopyFrom(account_filter)

    # 2) (Optional) Set commitment if your node supports it
    req.commitment = geyser_pb2.PROCESSED

    # 3) You can also add slots, blocks, etc. if needed. For now, just account updates.
    # req.slots["someSlotFilter"].CopyFrom(geyser_pb2.SubscribeRequestFilterSlots())
    # etc.

    return req


def request_generator(subscribe_req):
    """
    We only send the SubscribeRequest once, then keep reading updates indefinitely.
    """
    yield subscribe_req
    # If you wanted to send additional requests later, you'd yield them here.


def handle_stream(endpoint, x_token, wallet_pubkey):
    """
    Open a gRPC channel, subscribe to account, and read updates.
    Raises grpc.RpcError if something goes wrong.
    """

    # 1) Build credentials
    # If your endpoint is https://..., you typically want a secure channel:
    ssl_creds = grpc.ssl_channel_credentials()
    auth_plugin = TritonAuthMetadataPlugin(x_token or "")
    call_creds = grpc.metadata_call_credentials(auth_plugin)
    combined_creds = grpc.composite_channel_credentials(ssl_creds, call_creds)

    # 2) Create channel (secure if you have TLS, or insecure if your node doesn't use TLS)
    # For TLS:   channel = grpc.secure_channel(endpoint, combined_creds)
    # For no TLS: channel = grpc.insecure_channel(endpoint) # ignoring x_token
    channel = grpc.secure_channel(endpoint, combined_creds)

    # 3) Create stub
    stub = geyser_pb2_grpc.GeyserStub(channel)

    # 4) Prepare request for that specific wallet
    subscribe_req = make_subscribe_request(wallet_pubkey)

    # 5) Initiate the bidi stream
    stream = stub.Subscribe(request_generator(subscribe_req))

    # 6) Read updates forever (until an exception is raised or the server closes)
    for update in stream:
        # 'update' is a SubscribeUpdate message
        # If it has an 'account' field, it might look like update.account.account_info.lamports, etc.
        print("🔄 Update:", update)


@click.command()
@click.option("--endpoint", required=True, help="e.g. 'geyser.gsnode.io:443' or '127.0.0.1:10000'")
@click.option("--x-token", default="", help="Optional x-token if your node requires it")
@click.option("--wallet-pubkey", default="66ZC9U8y1uYaAxt4WFYVW11YZeZohvi8ev6wBHsAxykh",
              help="The account/wallet to subscribe to")
def subscribe_account(endpoint, x_token, wallet_pubkey):
    """
    Simple program to subscribe to changes in a specific account (wallet).
    Reconnects automatically on error.
    """
    logging.basicConfig(level=logging.INFO)
    while True:
        try:
            handle_stream(endpoint, x_token, wallet_pubkey)
        except grpc.RpcError as e:
            logging.error(f"Stream error, reconnecting in 1s... {e}")
            time.sleep(1)
        except Exception as ex:
            logging.error(f"Unexpected error: {ex}")
            break


if __name__ == "__main__":
    subscribe_account()
