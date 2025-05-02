import docker

def is_container_running(containername):
    RUNNING = "running"
    client = docker.from_env()
    try: #got the try/except stuff from a stackexchange post
        container = client.containers.get(containername)
        attributes = container.attrs
        network_settings = attributes['NetworkSettings']
        ipaddress = network_settings['IPAddress']
    except docker.errors.NotFound as exc:
        print(f"Check container ", containername)
    else:
        container_state = container.attrs["State"]
        return ipaddress, container_state["Status"] == RUNNING

if __name__ == "__main__":
    containers = ["tupperware", "rubbermaid"]
    for container in containers:
        result = is_container_running(container)
        print(result)