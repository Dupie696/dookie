# dookie
Flash Card App


# Installation on windows
All of these commands can be ran from the windows powershell.

This can be access by right click on the start button and clicking:

windows10: powershell
windows11: terminal

## Install Python
The Python interpreter is required to execute the project source code.

This can be installed from the window store by running the following command in a powershell terminal:
```powershell
winget install -e --id Python.Python.3.11
```

## installing QT5
The graphical user interface is written using the QT5 framework library.

This can be installed using the python package manager pip

```powershell
pip install pyqt5
```

## download the source
This can be manually downloaded and unzipped to the c:\git\dookie directory or you can run the following:

First creat the C:\git\dookie directory with the following command:
```powershell
New-Item -ItemType Directory -Path "C:\git\" -Force
```

Next, download the source code tot he c:\git directory, or by running the following command:
```powershell
Invoke-WebRequest -Uri "https://github.com/Dupie696/dookie/archive/refs/heads/main.zip" -OutFile "C:\git\dookie.zip"
```

Finally unzip the file to the c:\git\dookie folder
```powershell
Expand-Archive -Path "C:\git\dookie.zip" -DestinationPath "C:\git\" -Force
```

next just a couple of cleanup items.

correct the directory name from dookie-main to just dookie

```powershell
Rename-Item -Path "C:\git\dookie-main" -NewName "dookie"
```

Then delete unused files by running:
```powershell
Remove-Item "C:\git\dookie.zip"
```
