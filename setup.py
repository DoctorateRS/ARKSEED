import pip
from setup_requirements import setup_requirements

requires = ["flask", "requests", "frida", "pure-python-adb", "pycryptodome", "UnityPy", "bson"]


def main():
    for req in requires:
        pip.main(["install", req])


if __name__ == "__main__":
    main()
    setup_requirements()
