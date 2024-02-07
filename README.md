# AESED
This is a open source AES256 encryption/decryption tool with error support.
NOTE: Versions after 1.0.3(portable and embedded) will be non-interchangerble with versions 1.0.0 to 1.0.3 due to a change of salt key for security reasons.

## How to install (embedded):
1. If you don't have python installed then make sure that you download python from [here](https://www.python.org/downloads/)
2. To check that you have python installed properly open CMD and type ```py --version``` if something alnog the lines of ```Python 3.12.0``` shows up then you are good to go, IF you get an error message that read something along the lines of ```Python was not found; \ run without arguments to install from the Microsoft Store, or disable this shortcut``` then that probably means that you havnt added python to your computers PATH (use [this](https://realpython.com/add-python-to-path/) link to add python to your path). If this still doesnt fix your problem try looking around the offical python website for a solution.
3. Download the latest AESED version from [here](https://github.com/FinnAIA/AESED/releases) also download the ```images``` file and the ```pip_installer.bat``` file from the [homepage](https://github.com/FinnAIA/AESED/tree/v1.0.5) So that they are all in the same directory.
4. Run the pip_installer.bat file and wait until it closes, then procead with the next step, if you have problems make sure that when you use the python installer you have the "install pip" checkbox ticked.
5. Run the AESED_embedded.py file, it should now work! if any issues arise please contact me/make a GitHub issue.

## How to install (portable):
1. Simplily download the ```AESED_portable.exe``` file (from [here](https://github.com/FinnAIA/AESED/releases))and run it! (Note: Windows defender may stop you from running this file, in that case just click "More options" and then click "run anyway") if any issues arise please contact me/make a GitHub issue.

## Support:
1. I am attempting to get the installers to work on Linux (probably just Debian) and Mac OS however this will not be avaliable for a while.
