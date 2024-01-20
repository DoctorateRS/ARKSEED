import sys
from base64 import b64decode

import frida
import json
from time import sleep

import get_static_js

with open("config/config.json") as f:
    config = json.load(f)

server = config["server"]
MODE = server["mode"]

def on_message(message, data):
    print("[%s] => %s" % (message, data))

def main():
    device = frida.get_usb_device(timeout=1)

    if MODE == "cn":
        pid = device.spawn(
            b64decode('Y29tLmh5cGVyZ3J5cGguYXJrbmlnaHRz').decode())
        device.resume(pid)
        session = device.attach(pid)

    else:
        pid = device.spawn(
            b64decode('Y29tLllvU3RhckVOLkFya25pZ2h0cw==').decode())
        device.resume(pid)
        session = device.attach(pid, realm="emulated")

    s = get_static_js.getStaticJS()

    script = session.create_script(s)
    script.on('message', on_message)
    script.load()
    print("[!] Ctrl+Z on Windows/cmd.exe to detach from instrumented program. [!]")
    sys.stdin.read()
    session.detach()

if __name__ == '__main__':
    sleep(0.25)
    main()