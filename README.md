# PyScanner

This is a simple Port Scanner written in Python that aims to provide similar features to Nmap without external dependencies.

## How to Use
**Installation**
- Clone the repository
- Run the following
```console
foo@bar:~$ python ./main.py [options] [target]
```
**Examples**
```console
foo@bar:~$ python ./main.py -v -sT 192.168.45.xx
foo@bar:~$ python ./main.py -v -sT -p 80 192.168.45.xx
foo@bar:~$ python ./main.py -v -sn 192.168.45.0/24
```
