import json
import os
import zmq


from dizzy.daemon.client.basic import DizzyClient


class CustomDizzyClient(DizzyClient):
    pass


dizzy_client = CustomDizzyClient(
    address=os.getenv("DIZZY_COMPUTE_HOST"), port=os.getenv("DIZZY_COMPUTE_PORT")
)


def main():
    pass


if __name__ == "__main__":
    main()
    # pass
