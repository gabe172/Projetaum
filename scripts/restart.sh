#!/bin/bash
#bash /var/www/html/cgi-bin/panico.sh
sleep 5
#bash /var/www/html/cgi-bin/regras.sh
systemctl restart bind9
systemctl restart nagios3
