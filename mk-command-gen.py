import os
import pyperclip
import subprocess

RK = """
██████╗ ██╗  ██╗███████╗ █████╗ ██╗   ██╗███████╗███████╗
██╔══██╗██║ ██╔╝██╔════╝██╔══██╗██║   ██║██╔════██╔════╝
██████╔╝█████╔╝ █████╗  ███████║██║   ██║█████╗  ███████╗
██╔══██╗██╔═██╗ ██╔══╝  ██╔══██║██║   ██║██╔══╝  ╚════██║
██║  ██║██║  ██╗███████╗██║  ██║╚██████╔╝███████╗███████║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝
"""

def windows_to_cygwin_path(win_path):
    """Convert a Windows path to a properly escaped Cygwin-compatible path."""
    win_path = win_path.replace("\\", "/")  # Replace backslashes with forward slashes
    if ":" in win_path:
        drive, path = win_path.split(":", 1)
        cygwin_path = f"/cygdrive/{drive.lower()}{path}"
    else:
        cygwin_path = win_path

    # Escape special characters (spaces, brackets, etc.)
    cygwin_path = cygwin_path.replace(" ", "\\ ")
    cygwin_path = cygwin_path.replace("[", "\\[").replace("]", "\\]")

    return cygwin_path

def main():
    os.system("cls" if os.name == "nt" else "clear")

    print("\033[1;36m" + RK + "\033[0m")
    print("\n\033[1;37m Welcome !\033[0m")
    print("\033[1;37m This script automatically generates mktorrent commands,\033[0m")
    print("\033[1;37m it also converts windows paths into properly escaped cygwin compatible paths.\033[0m")


    base_path = input("\n Enter base path (Windows format, e.g., C:\\Folder\\[ My uploads ]\\): ").strip()
    
    while True:
        announce_url = input(" Enter announce URL: ").strip()
        if announce_url:
            break
        print(" Announce URL is required. Please enter a valid URL.")

    while True:
        source = input(" Enter source: ").strip()
        if source:
            break
        print(" Source is required. Please enter a valid source.")

    cygwin_path = windows_to_cygwin_path(base_path)

    command = f"""cd {cygwin_path}

for folder in */; do
    mktorrent --announce={announce_url} --source={source} -p "$folder"
done"""

    print("\n\033[1;32m Compiled Command:\033[0m\n")
    print("\033[1;33m" + command + "\033[0m")

    pyperclip.copy(command)
    print("\n\033[1;36mCommand copied to clipboard!\033[0m")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    cmd_path = os.path.join(script_dir, "mktorrent.cmd")

    if os.path.exists(cmd_path):
        print("\nOpening mktorrent.cmd with persistent output...")
        subprocess.run(f'start "mktorrent" cmd /K "call \"{cmd_path}\" & pause"', shell=True)
    else:
        print("\n\033[1;31m mktorrent.cmd not found in script folder!\033[0m")

    if os.path.exists(cmd_path):
        print("\nOpening mktorrent.cmd wrapper...")
        print("\nPaste *compiled command* into the mktorrent bash window.")
        # Prepend each line of the generated command with the ANSI color code for yellow (1;33m)
        cmd_command_text = "\n".join(["echo %ESC%[1;33m " + line for line in command.splitlines()])
        cmd_window = f"""@echo off
for /F "delims=" %%A in ('echo prompt $E^| cmd') do set "ESC=%%A"
echo.
echo %ESC%[1;37mcygwin path: {cygwin_path}
echo.
echo %ESC%[1;36m  The above command has been copied to your clipboard
echo %ESC%[1;36m  Please paste it into the mktorrent bash window.
echo.
echo.
echo.
pause
"""
        cmd_script_path = os.path.join(script_dir, "tmp.cmd")
        with open(cmd_script_path, "w", encoding="utf-8", errors="replace") as cmd_script:
            cmd_script.write(cmd_window)

        subprocess.run(f'cmd /K "{cmd_script_path}"', shell=True)
    else:
        print("\n\033[1;31m mktorrent.cmd not found in script folder!\033[0m")

if __name__ == "__main__":
    main()
