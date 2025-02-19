# mktorrent builds for Windows (with Cygwin)

## mktorrent 1.1 build2 (with Cygwin):

### Windows downloads:
- [mktorrent-1.1-win-32bit-build2.7z](https://github.com/q3aql/mktorrent-win/releases/download/v1.1-2/mktorrent-1.1-win-32bit-build2.7z)
- [mktorrent-1.1-win-64bit-build2.7z](https://github.com/q3aql/mktorrent-win/releases/download/v1.1-2/mktorrent-1.1-win-64bit-build2.7z)

### Source code:
- [mktorrent-1.1-git.tar.bz2](https://github.com/q3aql/mktorrent-win/releases/download/v1.1-2/mktorrent-1.1.tar.bz2)
- [mktorrent-1.1-git.tar.gz](https://github.com/q3aql/mktorrent-win/releases/download/v1.1-2/mktorrent-1.1-git.tar.gz)

## How to install:

### Instructions:
1. Unzip the package with [7-zip](http://www.7-zip.org/) or [Winrar](http://www.rarlab.com/).
2. Copy `mktorrent` folder to `C:\` or `C:\Program Files\`.
3. Run the script `Install.cmd`.

### Install requirements:
- Run `python -m pip install --user -U -r requirements.txt` to ensure dependencies are up to date

## New Feature: mk-command-gen.py

if you have folders named Folder1, Folder2, and Folder3, the loop processes each folder in turn and runs the mktorrent command, resulting in the creation of Folder1.torrent, Folder2.torrent, and Folder3.torrent respectively.

A new script, `mk-command-gen.py`, has been added to streamline the process of generating mktorrent commands. This script:
- Automatically converts Windows paths into properly escaped Cygwin-compatible paths.
- Generates the full mktorrent command based on user inputs.
- Copies the command to the clipboard for easy pasting into the mktorrent Bash window.
- Creates a temp file tmp.cmd containing the command.
- Opens the mktorrent environment for direct use.

### Example Usage:


```text
Welcome !
This script automatically generates mktorrent commands,
it also converts windows paths into properly escaped cygwin compatible paths.

 Enter base path (Windows format, e.g., C:\Folder\[ My uploads ]\): C:\Folder\[ My uploads ]
 Enter announce URL: FLAG
 Enter source: https:///announceURL

Compiled Command:

cd /cygdrive/c/Folder/\[\ My\ uploads\ \]

for folder in */; do
    mktorrent --announce=FLAG --source=https:///announceURL -p "$folder"
done

Command copied to clipboard!

Opening mktorrent.cmd with persistent output...

Opening mktorrent.cmd wrapper...

Paste *compiled command* into the mktorrent bash window.

cygwin path: /cygdrive/c/Folder/\[\ My\ uploads\ \]

  The above command has been copied to your clipboard
  Please paste it into the mktorrent bash window.
```

### Create a desktop shortcut:

Run Installer:
Navigate to the downloaded folder and double-click install.cmd to create a desktop shortcut.

### How to build mktorrent on Cygwin:

  * Install [Cygwin](http://cygwin.com/) and add the following packages to the default configuration:

```shell
    * Devel/gcc-core
    * Devel/gcc
    * Devel/make
    * Devel/pkgconfig
    * Libs/openssl
    * Libs/openssl-devel
````

  * Download [mktorrent-1.1.tar.gz](https://github.com/q3aql/mktorrent-win/releases/download/v1.1/mktorrent-1.1.tar.gz) and save it to `C:\Cygwin\home\<User>\`.
  * Open a Cygwin terminal, and run the following commands:

    ```shell
    $ tar zxvf mktorrent-1.1-git.tar.gz
    $ cd mktorrent-git
    $ make USE_PTHREADS=1 USE_OPENSSL=1 USE_LONG_OPTIONS=1 USE_LARGE_FILES=1 (32-bits)
    $ make USE_PTHREADS=1 USE_OPENSSL=1 USE_LONG_OPTIONS=1 (64-bits)
    ````

### External links:

  * [mktorrent homepage](http://mktorrent.sourceforge.net/)
  * [mktorrent source code (Github)](https://github.com/esmil/mktorrent/)
  * [Cygwin homepage](https://www.cygwin.com/)




Credits to [q3aql](https://github.com/q3aql)
