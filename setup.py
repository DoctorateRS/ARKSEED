import pip

requires = [
    "flask",
    "requests",
    "frida",
    "pure-python-adb",
    "pycryptodome",
    "UnityPy",
    "bson"
]

def main():
    for req in requires:
        pip.main(['install', req])

if __name__ == "__main__":
    main()