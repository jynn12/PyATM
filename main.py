###                  ###
## Date    : 01-24-23 ##
## Author  : Jy4n     ##
## License : MIT      ##
###m                 ###

import os
import json
import colorama
from colorama import Fore, Back, Style
from time import sleep

# Initialize the colors lol
colorama.init()

# Load the json file

with open("account.json", "r") as j:
	user = json.load(j)

def banner():
	print(Fore.YELLOW + Back.GREEN + "+-----------------------------+")
	print(Fore.YELLOW + "|" + Fore.WHITE + " Landbank of the Philippines " + Fore.YELLOW + "|" + Style.RESET_ALL)
	print(Fore. YELLOW + Back.GREEN + "+-----------------------------+" + Style.RESET_ALL)
def clear_screen():
	os.system("clear")

def withdraw():
	sleep(0.5)
	clear_screen()
	banner()
	while True:
		amount = int(input("Enter the amount you want to withdraw: ₱"))
		if amount > user['balance']:
			print("You have insuffucient balance in your account")
		else:
			clear_screen()
			banner()
			user['balance'] = user['balance'] - amount
			print(f"₱{amount} Succesfully withdrawn")
			print('')
			sleep(3)
			return False

def deposit():
	sleep(0.5)
	clear_screen()
	banner()
	amount = int(input("Enter the amount you want to deposit: "))
	clear_screen()
	banner()
	user['balance'] = user['balance'] + amount
	print(f"Deposited ₱{amount}")
	print('')
	sleep(3)
	return False

def balance():
	sleep(0.5)
	clear_screen()
	banner()
	print(f"Account balance ₱{user['balance']}")
	print('')
	sleep(3)

is_quit = False
clear_screen()
banner()

pin = int(input('Enter your 4-digit pin: '))

if pin == user['pin']:
	while is_quit == False:
		sleep(1)
		clear_screen()
		banner()
		print("Select Option")
		print(" [1] : Withdraw \n [2] : Balance \n [3] : Deposit \n [4] : Exit")
		query = int(input("Enter the number of your choice: "))
		
		if query == 1:
			withdraw()
		elif query == 2:
			balance()
		elif query == 3:
			deposit()
		elif query == 4:
			is_quit = True
		else:
			print("Please enter a valid option")
else:
	print("Wrong PIN")
