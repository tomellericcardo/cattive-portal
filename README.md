# *cattive-portal*
Sets up your Raspberry Pi as an indipendent wireless AP and runs an evil captive portal which logs the credentials of the unsuspicious users.

## How to
To set up the AP and make the portal run at boot, enter:

    sh install.sh

To stop the AP and use the Pi as a WiFi client (it will restart as an AP anyway), enter:

    sh stop.sh

To manage the AP by yourself and just run the captive portal web-app, enter:

    python portal.py

## To do
Create a real authentication system, in order to provide Internet connection to the registered user and perform a MITM attack.
