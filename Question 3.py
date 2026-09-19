import socket

HOST = "127.0.0.1"
PORT = 65432
MESSAGE = "Hello from client!"


def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.settimeout(5)  
            client.connect((HOST, PORT))
            print(f"Connected to server at {HOST}:{PORT}")
            client.sendall(MESSAGE.encode("utf-8"))
            print(f"Sent: {MESSAGE}")

    except ConnectionRefusedError:
        print("Connection refused: is the server running?")
    except socket.timeout:
        print("Connection timed out.")
    except socket.gaierror as e:
        print(f"Address error: {e}")
    except OSError as e:
        print(f"Network error: {e}")


if __name__ == "__main__":
    main()