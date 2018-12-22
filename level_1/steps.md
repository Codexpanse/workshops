## For Windows

1. Download and install VS Code from https://code.visualstudio.com/

1. Install Chocolatey (https://chocolatey.org/install):
    1. Select and copy: `@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"`
    1. Press `Windows X` and choose `Command Prompt (Admin)`
    1. Right click inside the command prompt window and select "Paste"
    1. Hit `Enter`
    1. Wait

1. Install `cmder` using Chocolatey:
    1. In the same command prompt window, type `choco install cmder` 
    1. Hit `Enter`
    1. Wait
    
1. Install `netcat` using Chocolatey: `choco install netcat` 
    
1. Install Python using Chocolatey: `choco install python`. Or alternatively download and install Python manually from here https://www.python.org/downloads/

---

## For Apple macOS

1. Download and install VS Code from https://code.visualstudio.com/

1. (Optional) Install homebrew:
    1. Select and copy this: `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
    1. Open Terminal.app
    1. Paste
    1. Hit `Enter`
    1. Wait
    
1. Install Python using brew: `brew install python` OR download and install manually from https://www.python.org/downloads/

---

## Links

1. Python3 web repl https://repl.it/languages/python3
2. HTTP server code https://github.com/Codexpanse/workshops/blob/master/level_1/2_simple_HTTP_server/server.py
