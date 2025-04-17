import time
import logging
import click

import grpc
import geyser_pb2
import geyser_pb2_grpc


def make_subscribe_request(wallet_pubkey: str):
    req = geyser_pb2.SubscribeRequest()
    account_filter = geyser_pb2.SubscribeRequestFilterAccounts()
    account_filter.account.extend([wallet_pubkey])
    req.accounts["exampleAccount"].CopyFrom(account_filter)
    req.commitment = geyser_pb2.PROCESSED
    return req


def request_generator(subscribe_req):
    yield subscribe_req


def handle_stream(endpoint, wallet_pubkey):
    channel = grpc.insecure_channel(endpoint)
    stub = geyser_pb2_grpc.GeyserStub(channel)
    subscribe_req = make_subscribe_request(wallet_pubkey)
    stream = stub.Subscribe(request_generator(subscribe_req))
    for update in stream:
        print("🔄 Update:", update)


@click.command()
@click.option("--endpoint", required=True)
@click.option("--wallet-pubkey", required=True)
def subscribe_account(endpoint, wallet_pubkey):
    logging.basicConfig(level=logging.INFO)
    while True:
        try:
            handle_stream(endpoint, wallet_pubkey)
        except grpc.RpcError as e:
            logging.error(f"Stream error, reconnecting in 1s... {e}")
            time.sleep(1)
        except Exception as ex:
            logging.error(f"Unexpected error: {ex}")
            break


if __name__ == "__main__":
    subscribe_account()
