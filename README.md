Netrack
=======================================================================================================================
[![GPL Licence](https://badges.frapsoft.com/os/gpl/gpl-150x33.png?v=103)](https://opensource.org/licenses/GPL-3.0/)

[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source-175x29.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

Installation (using pip3)
=========================

The easiest and best way to install netrack is using pip3.

1. If you don't have pip3 installed, use your package manager to install the package python3-pip. For Debian based systems
   the command to use would be. `$ sudo apt-get install python3-pip`.
2. Now it's time to install scapy. `$ sudo pip3 install scapy`.
3. Next, use pip3 to install netrack. `$ sudo pip3 install netrack`.

Installation (from source)
==========================

Installing from source is easy.

1. First use wget to download scapy. `$ wget https://files.pythonhosted.org/packages/c6/8f/438d4d0bab4c8e22906a7401dd082b4c0f914daf2bbdc7e7e8390d81a5c3/scapy-2.4.4.tar.gz`.
2. Extract the tar.gz package. `$ tar -xf scapy-2.4.4.tar.gz/`.
3. Navigate to the extracted directory. `$ cd scapy-2.4.4/`.
4. Now install the library. `$ sudo python3 setup.py install`.
5. Next clone the file with git. `$ git clone https://github.com/Nathalon/netrack.git`.
6. Enter the source directory. `$ cd netrack/`.
7. if you have sudo installed, log in as a sudoer and execute the setup.py file with sudo. `$ sudo python3 setup.py install`.
8. Done! It should now be a simple case of executing `$ netrack` in your favorite terminal emulator.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
