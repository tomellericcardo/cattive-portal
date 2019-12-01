echo "Stopping dnsmasq and hostapd ..."
systemctl stop dnsmasq
systemctl stop hostapd

echo "Configuring and restarting dhcpcd ..."
cp /etc/dhcpcd.conf.client /etc/dhcpcd.conf
service dhcpcd restart
cp /etc/dhcpcd.conf.portal /etc/dhcpcd.conf
