import pip

requires = [
    "requests",
    "frida",
    "pure-python-adb",
    "pycryptodome"
]

def main():
    for req in requires:
        pip.main(['install', req])

if __name__ == "__main__":
    main()