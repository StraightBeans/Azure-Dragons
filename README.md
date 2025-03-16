# Azure RPG
## Development Setup for VSCode
Download Python on your system from https://www.python.org/downloads/ \
Download Visual Studio Code from https://code.visualstudio.com/download \
Download some syntax highlighting to preserve your sanity:
- [Python Syntax Highlighting](https://open-vsx.org/vscode/item?itemName=ms-python.python)
- [Python Debugging](https://open-vsx.org/vscode/item?itemName=ms-python.debugpy)

Then, Download Git from https://git-scm.com/downloads \
Once you're inside your IDE, open up a terminal and run the following after changing the path:
```
git clone https://github.com/StraightBeans/Azure-Dragons /path/to/where/you/want/it/saved
```
Now open up your IDE from where you saved our repository, \
the directory should be called Azure-Dragons, and run the following:
```
python -m venv .venv
```
```
source .venv/bin/activate
```
```
pip install -r requirements.txt
```
Now you ready to start working

## Uploading Changes with Git
Run the following after changing the username and email:
```
git config user.name "enter your github username here"
```
```
git config user.email "enter email used on your github account"
```
Now when you commit changes from Source Control, you commits should go straight to this repository