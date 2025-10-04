import subprocess
import json

# Test the server directly
result = subprocess.run(
    ["python", "server.py"],
    input='{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test", "version": "1.0.0"}}}\n',
    text=True,
    capture_output=True,
    timeout=5
)

print("Server output:", result.stdout)
print("Server error:", result.stderr)
print("Return code:", result.returncode)
