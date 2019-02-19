# airpurifier2
It is a simple PyQt5 application for Xiaomi Air Purifier 2. It requires **miio** package installed (you can install it with pip)

You need to know what is the IP address of your device.
Also you need to know the device token.

To obtain your device token, run in the bash console (Linux):

> echo -ne '\x21\x31\x00\x20\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff' | nc -u 192.168.X.XXX 54321 | od -j 16 -t x1

It should return the device token (16 bytes).

**Important update**

Unfortunately, there is no way to obtain the token from the recent xiaomi airpurifier firmware with above method.
Device responds with zeros. Check the link below to see details:

https://github.com/rytilahti/python-miio/issues/461

The fastest way to obtain the device token is use proper version of the Android Mi Home app (5.4.49) and view the log file in the /SmartHome/logs/plug_DeviceManager
