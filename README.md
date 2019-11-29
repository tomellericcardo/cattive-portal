# *cattive-portal*
An evil captive portal designed to work on a Raspberry Pi set up as an indipendent wireless AP.

## How to
Install Flask with:

    pip install flask

Set up the portal by editing the configuration file:

    nano portal.conf

Start the web-app:

    python portal.py

## To do
- Add fake third party access option (such as Google and Facebook).
- Create a real authentication system, in order to provide Internet connection to the registered user and perform a MITM attack.
