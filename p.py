#!/usr/bin/python
# coding=UTF-8

import time
import socket
import socks
import requests
from bs4 import BeautifulSoup
from stem import Signal
from stem.control import Controller

from selenium.webdriver.common.keys import Keys
controller = Controller.from_port(port=9051)

def connectTor():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5 , "127.0.0.1", 9050, True)
    socket.socket = socks.socksocket

def showmyip():
    url = "http://www.showmyip.gr/"
    r = requests.Session()
    page = r.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    ip_address = soup.find("span",{"class":"ip_address"}).text.strip()
    print(ip_address)

with Controller.from_port(port = 9051) as controller:
    controller.authenticate("16:872860B76453A77D60CA2BB8C1A7042072093276A3D701AD684053EC4C")
    for i in range(10):
        showmyip()
	controller.signal(Signal.NEWNYM)
	time.sleep(7)
	connectTor()
