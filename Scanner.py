import socket
import time
import sys


def port_checker(socket_ip, start_port, end_port):
    print("Start port is:", start_port, "End port is:", end_port)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Open socket

    for i in range(start_port, end_port):
        start_ms_counter = int(round(time.time() * 1000))  # Ping counter start
        socket_status = s.connect_ex((socket_ip, i))  # Get the socket port status
        # if status is 0 – port is opened, else – port is closed.

        if socket_status == 0:
            status = "is opened"
        else:
            status = "is closed"

        count_millis = int(round(time.time() * 1000)) - start_ms_counter  # Ping counter end

        ends = (end_port - i) / ((count_millis/1000) * 60)  # Time's left counter

        # Output
        print(socket_ip + ", port", str(i), status + ", ping:", str(count_millis), end='')
        print('\tTime\'s left:', int(ends / 60), 'Hours', int(ends % 60), 'Minutes')


if __name__ == '__main__':

    # Software env
    ip = "127.0.0.1"
    start = 1
    end = 65535

    # Get user's arguments
    if len(sys.argv) >= 2:
        ip = str(sys.argv[1])
    if len(sys.argv) >= 3:
        start = int(sys.argv[2])
    if len(sys.argv) == 4:
        end = int(sys.argv[3])

    port_checker(ip, start, end)
