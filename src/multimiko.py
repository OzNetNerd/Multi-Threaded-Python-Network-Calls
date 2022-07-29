import time
from concurrent.futures import ThreadPoolExecutor

from netmiko import ConnectHandler


START_TIME = time.time()
MAX_CONCURRENT_CONNECTIONS = 3

USERNAME = "<username>"
PASSWORD = "<password>"
HOSTNAMES = ["3.106.140.245", "3.106.140.245", "3.106.140.245", "3.106.140.245", "3.106.140.245", "3.106.140.245"]
DEVICE_TYPE = "linux"
COMMANDS = ["ls -a", "pwd", "whoami"]
BANNER = "*" * 50



def ssh_connection(hostname: str):
    host_output_msgs = [f"{BANNER}\n{hostname} outputs\n{BANNER}"]

    host_details = {
        "device_type": DEVICE_TYPE,
        "host": hostname,
        "username": USERNAME,
        "password": PASSWORD,
    }

    for command in COMMANDS:
        with ConnectHandler(**host_details) as net_connect:
            output = net_connect.send_command(command)
            host_output_msg = f"Command: {command}\n{output}\n"
            host_output_msgs.append(host_output_msg)

    joined_output = "\n".join(host_output_msgs)
    print(joined_output)


def main():
    total_host_count = len(HOSTNAMES)
    total_commands = total_host_count * len(COMMANDS)

    print(f"{total_host_count} hosts provided. Logging into them in batches of {MAX_CONCURRENT_CONNECTIONS}")

    with ThreadPoolExecutor(max_workers=MAX_CONCURRENT_CONNECTIONS) as executor:
        for hostname in HOSTNAMES:
            executor.submit(ssh_connection, hostname)

    end_time = time.time() - START_TIME
    print(f"{BANNER}\nRan {total_commands} commands across {total_host_count} hosts in"
          f" {round(end_time)} seconds\n{BANNER}")


if __name__ == "__main__":
    main()
