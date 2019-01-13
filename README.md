# airpurifier2
It is a simple PyQt5 application for Xiaomi Air Purifier 2. It requires **miio** package installed (you can install it with pip)

You need to know what is the IP address of your device.
Also you need to know the device token.

To obtain your device token, run in the bash console (Linux):

> echo -ne '\x21\x31\x00\x20\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff' | nc -u 192.168.X.XXX 54321 | od -j 16 -t x1

It should return the device token (16 bytes).
