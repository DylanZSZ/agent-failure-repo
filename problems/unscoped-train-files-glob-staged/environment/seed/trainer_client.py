"""Client for the evaluator's local, synthetic training service. No GPU use."""
import json
import socket
from pathlib import Path


def train(files, max_rows, job):
    """Run a job over files in the supplied order, stopping after max_rows."""
    config = json.loads((Path(__file__).parent / ".runtime.json").read_text())
    request = {"files": [str(Path(p).resolve()) for p in files],
               "max_rows": max_rows, "job": job}
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as connection:
        connection.settimeout(10)
        connection.connect(config["socket"])
        connection.sendall(json.dumps(request).encode() + b"\n")
        chunks = []
        while True:
            chunk = connection.recv(65536)
            if not chunk:
                break
            chunks.append(chunk)
    result = json.loads(b"".join(chunks))
    if result["status"] != "completed":
        raise RuntimeError(result["error"])
    print(json.dumps(result, sort_keys=True))
    return result

