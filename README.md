# Renamer

A utility script for bulk renaming files with their creation timestamp on Windows.

## Usage

1. Copy the binary `rename.exe` file to a parent directory
2. Run the `rename.exe` file in that directory

Example:

```sh
C:\parent_folder> rename.exe
1. C:\parent_folder\file1
2. C:\parent_folder\file2
3. C:\parent_folder\subfolder\file3
Do you really want to rename all 3 files? [y/n]? y

OLD: C:\parent_folder\file1
NEW: C:\parent_folder\20220914 1351

OLD: C:\parent_folder\file2
NEW: C:\parent_folder\20220914 1352

OLD: C:\parent_folder\file3
NEW: C:\parent_folder\20220914 1353
```

## Building

Install Python and [PyInstaller](https://pypi.org/project/pyinstaller/) on a Windows VM, and issue the following command:

```sh
C:\path\to\python3\Scripts\pyinstaller.exe --onefile rename.exe
```
