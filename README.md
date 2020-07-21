# youtube_instrumentals
Download multiple tracks and create instrumentals / stems automatically from youtube.

# Start:

Open `init.py` file.

## Requirements:

System-wide:
- `python3.8` 
- `ffmpeg`

Python3 packages:
- `PySimpleGUI`
- `youtube_dl`
- `validators`

# Installation (windows):

### System wide:
I suggest using `chocolatey` - package manager (similar to Microsoft Store but in command line).

### Installation Chocolatey:
https://chocolatey.org/install </br>

**or** <br/> run `Windows PowerShell (Admin)` - shortcut (`win`+`x`) <br/> 
and type: <br/>
`Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))`


### Installation Python:

`choco install python -y`

### Installation ffmpeg:

`choco install ffmpeg -y`

### Installation Python Packages:
`python -m pip install PySimpleGUI youtube_dl validators`
