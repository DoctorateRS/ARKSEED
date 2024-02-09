from os import system


def main():
    system("start cmd.exe /c start_local_server.bat")
    system("start cmd.exe /c start_frida-server.bat")
    print("All done!")


if __name__ == "__main__":
    main()
