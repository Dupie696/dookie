---

# Dookie
A Flash Card App for efficient learning.

---

## Installation on Windows
The following instructions assume you are using **Windows PowerShell**.

### Accessing PowerShell
- **Windows 10:** Right-click the Start button and select `PowerShell`.
- **Windows 11:** Right-click the Start button and select `Terminal`.

---

### Step 1: Install Python
The Python interpreter is required to run the project's source code.

To install Python (version 3.11) via the Microsoft Store, run the following command:
```powershell
winget install -e --id Python.Python.3.11
```

**Note:** After installing Python, you may need to restart your computer to ensure the system PATH is updated correctly.

---

### Step 2: Install PyQt5
The graphical user interface is built using the Qt5 framework, which is accessible through the PyQt5 library.

Install PyQt5 using `pip`:
```powershell
pip install pyqt5
```

---

### Step 3: Download the Source Code
You can either manually download and unzip the source code or automate the process with PowerShell commands.

#### Option 1: Manual Download
1. Navigate to the [Dookie GitHub Repository](https://github.com/Dupie696/dookie).
2. Download the source code ZIP file.
3. Extract the contents to `C:\git\dookie`.

#### Option 2: Automated Download
Follow these steps to set up the project:

1. **Create the directory:**
   ```powershell
   New-Item -ItemType Directory -Path "C:\git\" -Force
   ```

2. **Download the source code:**
   ```powershell
   Invoke-WebRequest -Uri "https://github.com/Dupie696/dookie/archive/refs/heads/main.zip" -OutFile "C:\git\dookie.zip"
   ```

3. **Extract the ZIP file:**
   ```powershell
   Expand-Archive -Path "C:\git\dookie.zip" -DestinationPath "C:\git\" -Force
   ```

4. **Rename the directory:**
   ```powershell
   Rename-Item -Path "C:\git\dookie-main" -NewName "dookie"
   ```

5. **Clean up unused files:**
   ```powershell
   Remove-Item "C:\git\dookie.zip"
   ```

---

### Step 4: Run the Application
Navigate to the source directory and execute the application:
```powershell
cd C:\git\dookie
python main.py
```

---

## Notes
- Ensure Python and `pip` are added to your system's PATH during installation.
- A reboot may be required after installing Python to refresh the system PATH.
- If you encounter errors, verify all dependencies are installed and up-to-date.

---

### Acknowledgments
This project was enhanced with insights and assistance from **ChatGPT 4.0**.

---
