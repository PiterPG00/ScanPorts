#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Criador: PiterPG
#Canal Telegram: @hackersdobem
#Grupo Telegram: @grupohdb

import socket
import os
port_enco = []
port_0 = []
class portsc():  
    def scansc():
        print("""
            x===================x
            |	Scan de Portas  |
            |	    V 1.0       |
            |	 By: PiterPG    |
            x===================x
            """)
        esc = int(input("Opcoes:\n1 - IP\n2 - Site\n===> "))
        if (esc == 1):
            ip = input("Digite o IP: ")

        elif (esc == 2):
            host = input("Digite o site: ")
            ip = socket.gethostbyname(host)

        port_ini = int(input("Porta do Inicio: "))
        port_fim = int(input("Porta do Fim: "))
        print("\nESCANEANDO PORTAS EM\n===> [{}] <===\n".format(ip))
        for ports in range(port_ini, port_fim):
    
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.03)
    
            login = s.connect_ex((ip,ports))
            if (login == 0):
                port_enco.append(ports)
                print("[+] PORTA ABERTA ===> [{}] <===".format(ports))

        if (port_enco == port_0):
                print("="*30)
                print("NENHUMA PORTA ABERTA DE [{}] ATE [{}]!".format(port_ini,port_fim))
                print("="*30)
    
        elif (port_enco != port_0):
                print("\n\nPORTAS ABERTAS!\n===> {} <===".format(port_enco))
                print("\n\nSCAN FINALIZADO COM SUCESSO!")
                
        else:
                print("ERRO!")
pt = portsc
pt.scansc()