echo "Installing dependencies ..."
apt update -y && apt upgrade -y
apt install dnsmasq hostapd python-pip -y
pip install flask

echo "Stopping dnsmasq and hostapd ..."
systemctl stop dnsmasq
systemctl stop hostapd

echo "Configuring dhcpcd ..."
cp /etc/dhcpcd.conf /etc/dhcpcd.conf.client
cat config/dhcpcd.conf >> /etc/dhcpcd.conf
cp /etc/dhcpcd.conf /etc/dhcpcd.conf.portal
service dhcpcd restart

echo "Configuring dnsmasq ..."
mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
cp config/dnsmasq.conf /etc/dnsmasq.conf
systemctl start dnsmasq

echo "Configuring hostapd ..."
cp config/hostapd.conf /etc/hostapd/hostapd.conf
sh -c "echo 'DAEMON_CONF=\"/etc/hostapd/hostapd.conf\"' >> /etc/default/hostapd"
systemctl unmask hostapd
systemctl enable hostapd
systemctl start hostapd

echo "Configuring IPv4 forwarding ..."
sh -c "echo 'net.ipv4.ip_forward=1' >> /etc/sysctl.conf"
iptables -t nat -A  POSTROUTING -o eth0 -j MASQUERADE
sh -c "iptables-save > /etc/iptables.ipv4.nat"

echo "Setting up on boot commands ..."
sed -i 's/exit 0//g' /etc/rc.local
sh -c "echo 'sudo iptables-restore < /etc/iptables.ipv4.nat' >> /etc/rc.local"
sh -c "echo 'sudo python /home/pi/cattive-portal/portal.py &' >> /etc/rc.local"
sh -c "echo 'exit 0' >> /etc/rc.local"

echo "Rebooting ..."
shutdown -r now
