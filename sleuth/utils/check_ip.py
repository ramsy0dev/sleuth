import subprocess

def check_ip(ip: str) -> bool:
    """ Checks if the ip is alive """
    command = ["ping", "-c", "1", ip]
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Check the return code
    return result.returncode == 0
