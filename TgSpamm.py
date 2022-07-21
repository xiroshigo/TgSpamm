import telethon
import time
import sys
from os import system
import os, sys, time, socket, random, requests
from telethon import TelegramClient, sync, utils

  
telegramspam_banner = """ \033[1;36m
▄▄▄▄▄╶╶▄▄╶╶╶╶╶╶╶╶╶▄▄╶╶╶╶▄▄▄╶╶╶▄▄▄╶╶╶╶▌╶▄╶╶╶╶╶╶▌╶▄╶╶╶╶
╶██╶╶╶▐█╶▀╶╶╶╶╶╶╶▐█╶▀╶╶▐█╶▄█╶▐█╶▀█╶╶██╶▐███╶╶██╶▐███╶
╶▐█╶╶╶▄█╶▀█▄╶╶╶╶╶▄▀▀▀█▄╶██▀╶╶▄█▀▀█╶▐█╶▌▐▌▐█╶▐█╶▌▐▌▐█╶
╶▐█▌╶╶▐█▄╶▐█╶╶╶╶╶▐█▄╶▐█▐█╶╶╶╶▐█╶╶▐▌██╶██▌▐█▌██╶██▌▐█▌
╶▀▀▀╶╶╶▀▀▀▀╶╶╶╶╶╶╶▀▀▀▀╶╶▀╶╶╶╶╶▀╶╶▀╶▀▀╶╶█╶▀▀▀▀▀╶╶█╶▀▀▀

"""
def clearscreen():
	if sys.platform == "linux2":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	print(backtomenu_banner)
	backtomenu = input("boshlash:  ")
	
	if backtomenu == "99":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print("\nERROR: Wrong input")
		time.sleep(2)
		restart_program()
		
		
__banner__ = """\033[1;32m
░░░░░░░░░░████████╗░██████╗░░░░░░░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░╚══██╔══╝██╔════╝░░░░░░██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░██║░░░██║░░██╗░░░░░░╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░██║░░░██║░░╚██╗░░░░░░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░██║░░░╚██████╔╝░░░░░██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░╚═╝░░░░╚═════╝░░░░░░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░░░░░░░░░░░░░░░░░░░"""


clearscreen()
print(__banner__)
print(""" \033[1;4;31m •••script dasturchisi: @darknet_off1cial\n  •••kanalimiz: @andro_py""")
print("""\033[1;34m
  •••telegram spamm massaging qiling yoki scriptdan chiqing:
  01) Telegram Spam Message Attack
  00) Spamm Massages dan chiqish
""")
os.system("termux-open-url https://t.me/darknet_off1cial")


while True:
	try:
		santet = input("  •••boshlash : ")
		
		if santet == "01" or santet == "1":	
			print(telegramspam_banner)
			api_id = 1148490
			api_hash = 'd82c81323285aeb9c2ba9ee420d8b009'
			client = TelegramClient('client',api_id,api_hash).start()
			target = input("boshlash: habar yubormoqchi bolgan odamingizning useri yoki ID sini yozing: ")
			try: count = int(input("boshlash: necha marta yuborilsin:"))
			except(ValueError): count = 100
			urmsg = input("boshlash: yubormoqchi bo'lgan habaringiz: ")
			for x in range(count):
				client.send_message(target, urmsg)
				sys.stdout.write(u"\u001b[1000D[*] Sent {} messages to {}...".format(x+1, target))
				sys.stdout.flush()
			print("\n[!] muvafaqiyatli amalga oshirildi ... !!\n")
			backtomenu_option()
		elif santet == "00" or santet == "0":
			sys.exit()
			print("Telegram: @termux_uz_private")
		elif santet.lower() == "Script haqida":
			print("ushbu script orqali telegram guruhlarga har bir sozni 2000 marotabadan ham koproq yubora olasiz. bu script tuzuvchisi @darknet_off1cial telegram kanalimiz: @termux_uz_private.")
		elif santet.lower() == "version":
			print("Version 1.1")
		elif santet.lower() == "exit":
			sys.exit()
		else:
			pass
	except(telethon.errors.rpcerrorlist.PhoneNumberInvalidError):
		print("telefon raqamingiz hato ekan qaytadan urunib ko'ring")
		print("Avval telefon raqamingizni Telegram’da ro‘yxatdan o‘tkazishingiz kerak\n")
	except(KeyboardInterrupt):
		print("\n[!] dasturni yopish...")
		break
	except(EOFError):
		print("\n[!] dasturni yopish...")
		break
	except Exception as e:
		print("\n[!] Error: "+e)
