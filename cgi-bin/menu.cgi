#!/usr/bin/python
#-*- coding: utf8 -*-
var=raw_input()

import os

acao=var.split("=")[0]
print("content-type: text/html")
print("")

if acao == "d_i":
	os.system("sudo /usr/lib/cgi-bin/script.sh bind9 start")
	print("<h1><center>Iniciando serviço DNS!</center></h1>")
elif acao == "d_p":
	os.system("sudo /usr/lib/cgi-bin/script.sh bind9 stop")
	print("<h1><center>Parando serviço DNS!</center></h1>")
elif acao == "d_r":
	os.system("sudo /usr/lib/cgi-bin/script.sh bind9 restart")
	print("<h1><center>Reiniciando serviço DNS!</center></h1>")
elif acao == "d_s":
	os.system("sudo /usr/lib/cgi-bin/status.sh bind9 status")
	status = open("/var/www/html/cgi-bin/status.txt", "r")
	html=status.read()
	status.close()
	print(html)

elif acao == "f_i":
	os.system("sudo /usr/lib/cgi-bin/regras.sh")
	print("<h1><center>Iniciando serviço Firewall!</center></h1>")
elif acao == "f_p":
	os.system("sudo /usr/lib/cgi-bin/panico.sh")
	print("<h1><center>Parando serviço Firewall!</center></h1>")
elif acao == "f_r":
	os.system("sudo /usr/lib/cgi-bin/regras.sh")
	print("<h1><center>Reiniciando serviço Firewall!</center></h1>")
elif acao == "f_s":
	os.system("/var/www/html/cgi-bin/firewall.sh")
	status = open ("/var/www/html/cgi-bin/firewall.txt")
	html=status.read()
	status.close()
	print(html)

elif acao == "n_i":
	os.system("sudo /usr/lib/cgi-bin/script.sh nagios3 restart")
	print("<h1><center>Iniciando serviço Nagios!</center></h1>")
elif acao == "n_p":
	os.system("sudo /usr/lib/cgi-bin/script.sh nagios3 stop")
	print("<h1><center>Parando serviço Nagios!</center></h1>")
elif acao == "n_r":
	os.system("sudo /usr/lib/cgi-bin/script.sh nagios3 restart")
	print("<h1><center>Reiniciando serviço Nagios!</center></h1>")
elif acao == "n_s":
	os.system("sudo /usr/lib/cgi-bin/status.sh nagios3 status")
	status = open("/var/www/html/cgi-bin/status.txt", "r")
	html=status.read()
	status.close()
	print(html)

elif acao == "Agendar":
	print("<h1><center>Agendado!</center></h1>")
