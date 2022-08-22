from asyncio import exceptions
import random
import requests
from bs4 import BeautifulSoup
import time
import os

class renkler:
    PEMBE = '\033[95m'
    MAVI = '\033[94m'
    CAMGOBEGI = '\033[96m'
    YESIL = '\033[92m'
    SARI = '\033[93m'
    KIRMIZI = '\033[91m'
    DUZ = '\033[0m'
    KALIN = '\033[1m'
    ALTICIZILI = '\033[4m'

def meta():
    try:
      r_url = str(input(renkler.KIRMIZI + "[ <Url İnput> ] Url: "))
      url_get = requests.get(r_url)
      nicesoup = BeautifulSoup(url_get.content, "html.parser")
      metaticket = nicesoup.find_all("meta")
      print(renkler.YESIL + f"Info:\n\n")
      for meta in metaticket:
        print(renkler.YESIL + f"{meta}")
    except :
      print(renkler.KIRMIZI + "Please Enter True Url.")


def script():
    try:
      r_url = str(input(renkler.KIRMIZI + "[ <Url İnput> ] Url: "))
      url_get = requests.get(r_url)
      nicesoup = BeautifulSoup(url_get.content, "html.parser")
      scriptticket = nicesoup.find_all("script")
      print(renkler.YESIL + f"Info:\n\n")
      for script in scriptticket:
        print(renkler.YESIL + f"{meta}")
    except :
      print(renkler.KIRMIZI + "Please Enter True Url.")

def a_link():
    try:
      r_url = str(input(renkler.KIRMIZI + "[ <Url İnput> ] Url: "))
      url_get = requests.get(r_url)
      nicesoup = BeautifulSoup(url_get.content, "html.parser")
      aticket = nicesoup.find_all("a")
      print(renkler.YESIL + f"Info:\n\n")
      for i in aticket:
        print(renkler.YESIL + f"{i}")
    except :
      print(renkler.KIRMIZI + "Please Enter True Url.")

banner = """

▓█████▄  ▄▄▄     ▄▄▄█████▓ ▄▄▄                          
▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒▒████▄                        
░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░▒██  ▀█▄                      
░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ ░██▄▄▄▄██                     
░▒████▓  ▓█   ▓██▒ ▒██▒ ░  ▓█   ▓██▒                    
 ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░    ▒▒   ▓▒█░                    
 ░ ▒  ▒   ▒   ▒▒ ░   ░      ▒   ▒▒ ░                    
 ░ ░  ░   ░   ▒    ░        ░   ▒                       
   ░          ░  ░              ░  ░                    
 ░                                                      
 ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
░                       ░                               

"""

selectmenu = """
[======================================================]
|                   -Command Menu-                     |
|                                                      |
|  1- Meta Ticket Checker / Command = /meta            |
|  2- Script Ticket Checker / Command = /script        |
|  3- Other Ticket Checker / Command = /other          |
|  4- <a ...> Ticket Checker / Command = /link         |
|                                                      |
|  Coded By Kuzey Ceylan                               |
|                                                      |
|  Licence: This Program Cannot Be Shared Anywhere     |
|  Else Without My Permission.                         |
|                                                      |
[======================================================]
"""

print(renkler.KALIN)
print(renkler.KIRMIZI + banner)
time.sleep(2)

if os.name == "nt":

    os.system("cls")

if os.name == "posix":

    os.system("clear")

print(renkler.MAVI + selectmenu)

selectcommand = str(input(renkler.KIRMIZI + "Command: "))

if selectcommand == "/meta":
    meta()
  

if selectcommand == "/script":
    script()
  
if selectcommand == "/link":
  a_link()

else:
  try:
    r_url = str(input(renkler.MAVI + "[ <Url İnput> ] Url: "))
    print(renkler.SARI + "Importing Html Data...")
    time.sleep(1)
    url_get = requests.get(r_url)
    print(renkler.YESIL + "Imported Html Data!")
    time.sleep(1)

    if os.name == "nt":

        os.system("cls")

    if os.name == "posix":

        os.system("clear")

    print(renkler.SARI)
    ticket_name = str(input(renkler.ALTICIZILI + "[ <Ticket Name> ] Ticket Name: "))


    print(renkler.SARI + f"Reading {ticket_name} Ticket...")
    nicesoup = BeautifulSoup(url_get.content, "html.parser")
    class_name = str(input(renkler.DUZ + "[ <Class Name> ] Name: "))
    tickets = nicesoup.find_all(f"{ticket_name}",{"class" : f"{class_name}"})
    print(renkler.SARI)
    for ticket in tickets:
        print(ticket)

  except :
    print(renkler.KIRMIZI + "Please Enter True Url.")


