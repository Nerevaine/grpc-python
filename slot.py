import sys
import grpc
import geyser_pb2_grpc
import geyser_pb2

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 slot.py <host:port>")
        sys.exit(1)

    endpoint = sys.argv[1]
    channel = grpc.insecure_channel(endpoint)
    stub = geyser_pb2_grpc.GeyserStub(channel)

    response = stub.GetSlot(geyser_pb2.GetSlotRequest())
    print("slot:", response.slot)

if __name__ == "__main__":
    main()
