from os import system


def main():
    system("start cmd.exe /c nu start_local_server.nu")
    system("start cmd.exe /c nu start_frida-server.nu")
    print("All done!")


if __name__ == "__main__":
    main()
