
import socket
import sys
import time

HOST = "127.0.0.1"
PORTS = {1: 5001, 2: 5002, 3: 5003}

if len(sys.argv) != 2 or sys.argv[1] not in ("1", "2", "3"):
    print("Usage: python node.py 1|2|3")
    sys.exit(1)

node = int(sys.argv[1])
next_node = node % 3 + 1

requested = False
printed = False
has_token = (node == 1)
completed = set()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORTS[node]))


def send(target, message):
    sock.sendto(message.encode(), (HOST, PORTS[target]))


def use_token():
    global has_token, printed, requested

    if not has_token:
        return

    if requested and not printed:
        print(f"P{node}: TOKEN received - permission granted")
        print(f"P{node}: PRINTING (critical section)")

        time.sleep(1)

        print(f"P{node}: RELEASE printer")

        printed = True
        requested = False

        if node == 1:
            completed.add(1)
        else:
            send(1, f"DONE {node}")

    has_token = False
    send(next_node, "TOKEN")
    print(f"P{node}: TOKEN passed to P{next_node}")


print(f"P{node}: Ready on port {PORTS[node]}")

try:
    if node == 1:
        input("Start P2 and P3, then press Enter to begin... ")

        send(2, "START")
        send(3, "START")

        send(next_node, "REQUEST 1")
        print("P1: REQUEST sent")

    while True:
        message, _ = sock.recvfrom(1024)
        message = message.decode()

        if message == "START":
            send(next_node, f"REQUEST {node}")
            print(f"P{node}: REQUEST sent")

        elif message.startswith("REQUEST "):
            origin = int(message.split()[1])

            if origin == node:
                requested = True
                print(f"P{node}: REQUEST completed around ring")
                use_token()
            else:
                print(f"P{node}: REQUEST forwarded from P{origin}")
                send(next_node, message)

        elif message == "TOKEN":
            has_token = True
            use_token()

        elif message.startswith("DONE ") and node == 1:
            completed.add(int(message.split()[1]))
            print(f"P1: {len(completed)}/3 print jobs finished")

            if len(completed) == 3:
                send(2, "STOP")
                print("P1: All three print jobs finished")
                break

        elif message == "STOP":
            if node == 2:
                send(3, "STOP")

            print(f"P{node}: Finished")
            break

finally:
    sock.close()
