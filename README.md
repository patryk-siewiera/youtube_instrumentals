# youtube_instrumentals
Download multiple tracks from youtube by single query. <br/> <br/>
(in future also and create instrumentals / stems automatically) <br/>

![](doc/release%20v0_1%20.gif)

# Start:

Open `main.py` file in command line.
```
python main.py
```

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
I suggest using `chocolatey` -  (package manager, similar to Microsoft Store but in command line).
https://chocolatey.org/install

### Installation Chocolatey:
Run `Windows PowerShell (Admin)` - shortcut (`win`+`x`) <br/> 
and type: <br/>
```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```


### Installation Python:
```
choco install python -y
```

### Installation ffmpeg:
```
choco install ffmpeg -y
```

After installation with `chocolatey` **restart** `Windows PowerShell (Admin)` (close and open it again).

### Installation Python Packages:
```
python -m pip install PySimpleGUI youtube_dl validators
```
<br/>
<br/>

# Future development plan:
- move from pip -> conda-forge
- add spleeter module (right now I have problems with numba==0.48)
- write tests 


 
 
