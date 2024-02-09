import os
import subprocess
from contextlib import suppress
import json
from setup_requirements import get_device

from ppadb.client import Client as AdbClient

server_port = json.load(open("config/config.json", "r"))["server"]["port"]
default_ports = [7555, 5555, 62001]
ADB_PATH = "platform-tools\\adb.exe"

os.system("cls")
# subprocess.run(f'"{ADB_PATH}" kill-server')
subprocess.run(f'"{ADB_PATH}" start-server')

client = AdbClient(host="127.0.0.1", port=5037)
device = None

print("Trying to connect to currently opened emulator...")
device = get_device()

print("Check the emulator and accept if it asks for root permission.")
with suppress(RuntimeError):
    device.root()
device = get_device()
os.system(f'"{ADB_PATH}" wait-for-device')

print("\nRunning frida...\nNow you can start fridahook...\n")
os.system(f'"{ADB_PATH}" reverse tcp:{server_port} tcp:{server_port}')
os.system("start cmd.exe /c start_frida-hook.bat")
os.system(f'"{ADB_PATH}"' + " shell /data/local/tmp/frida-server &")
