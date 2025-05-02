import docker
import time

client = docker.from_env()
containers = ["tupperware", "rubbermaid"]

def shutdowncheck():
    while True:
        for container in containers:
            client = client.containers.get(container)
            if container.status != "running": #got this from https://docker-py.readthedocs.io/en/stable/containers.html
                container.start()
                print("{container} had to be restarted")
            if time.strftime("%H") == "01":
                container.restart()
        time.sleep(10)

if __name__ == "__main__":
    shutdowncheck()