# readme start

# How to get enablesalad to work:
# 1: Go to app.salad.io
# 2: Click on lock near url
# 3: Go to cookies
# 4: Open app-api.salad.io folder
# 5: Copy salad.antiforgery and salad.authentication into a ".env" file like this:
# SALAD_ANTIFORGERY='Your antiforgery code here!'
# SALAD_AUTHENTICATION='Your authentication code here!'
# 6: Make sure salad.py is in same folder as the .env
# 7: Try starting
# 8: ray that it works
# If it works: yay!
# If it doesn't: Contact SharkOfGod#8424 on Discord!

# readme end

# settings begin

import random
from datetime import datetime
import json
import os
import time
import requests
import traceback
import math
rainbow = False
try:
	with open('colors.json') as f:
		coloors = json.load(f)
	coloorswork = True
	enablesalad = coloors['settings']['enable_salad_balance_tracker']
	title = coloors['settings']['window_title']
	presence = coloors['settings']['experimental_discord_presence']
	pclient = coloors['settings']['presence_client_id']
	typewriteroff = coloors['settings']['disable_typewriter']
	notifthreshold = coloors['settings']['balance_notification_every']
	try:
		enablekey = coloors['settings']['console_enabled']
	except:
		coloors['settings']['console_enabled'] = False
		coloors['settings']["/comment/console"] = "Hold E to open console to control logs"
		with open('colors.json', 'w+') as f:
			f.write(json.dumps(coloors, indent=4, sort_keys=True))
		enablekey = False
		print('Added a new in colors.json go check it out!')

	class custom_colors:
		pass
	for color in coloors['custom_colors'].keys():
		setattr(custom_colors, color, coloors['custom_colors'][color])
except Exception as e:
	print(traceback.format_exc())
	print('important: if ur getting this after an update add "disable_typewriter: false" to "settings" part of colors.json')
	print('colors.json error using defaults')
	coloorswork = False
	presence = False
	enablesalad = False  # balance updates in logs
	title = 'fancy salad miner logs'
	notifthreshold = 1  # ping when balance changes by this
	enablekey = False
	typewriteroff = False

# settings end (shark made settings in a json file therefore he is no longer an idiot)

os.system('title ' + title)
limit = 10
path = os.getenv('APPDATA')
path = path + '/salad/logs/main.log'


class default_colors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	DEFAULT = '\033[37;1m'
	#
	rainbow_1 = '\033[31m'
	rainbow_2 = '\033[31;1m'
	rainbow_3 = '\033[32m'
	rainbow_4 = '\033[36m'
	rainbow_5 = '\033[34;1m'
	rainbow_6 = '\033[35;1m'


def fancytype(words, notime=False, colors=[], speed=0.0078125):
	colorwords = ''
	for color in colors:
		colorwords = eval(color) + colorwords
	if not notime:
		words = ' ' + colorwords + timenow() + ' ' + words
	else:
		words = ' ' + colorwords + words
	
	if typewriteroff:
		print(words + default_colors.ENDC + default_colors.DEFAULT)
		return
	strin = ''
	if rainbow:
		speed /= 8
		newwords = ''
		for letter in words:
			newwords = newwords + \
				eval('default_colors.rainbow_' +
					 str(random.randint(1, 6))) + letter
		words = newwords
	for let in words:
		strin = strin + let
		print(strin, end='\r')
		time.sleep(speed)
	print(words + default_colors.ENDC + default_colors.DEFAULT)


def timenow():
	return '[' + str(datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]) + ']'

# *dont* abuse this or i will eat your salad account >:C /s

prices = {}

try:
	
	r = requests.get(url = 'http://api.shruc.ml/saladlog/news', params = {}, timeout = 5)
	fancytype('[news] ' + r.text[1:-2], colors = ['default_colors.WARNING', 'default_colors.BOLD'])
	time.sleep(1)
	
	r = requests.get(url = 'http://api.shruc.ml/saladlog/price?coin=eth', params = {}, timeout = 5)
	ans = r.json()
	if ans['RAW']['CHANGE24HOUR'] < 0:
		prices['ETH'] = (ans['RAW']['PRICE'], ans['RAW']['CHANGE24HOUR'], '-')
	else:
		prices['ETH'] = (ans['RAW']['PRICE'], ans['RAW']['CHANGE24HOUR'], '+')

	r = requests.get(url = 'http://api.shruc.ml/saladlog/price?coin=etc', params = {}, timeout = 5)
	ans = r.json()
	if ans['RAW']['CHANGE24HOUR'] < 0:
		prices['ETC'] = (ans['RAW']['PRICE'], ans['RAW']['CHANGE24HOUR'], '-')
	else:
		prices['ETC'] = (ans['RAW']['PRICE'], ans['RAW']['CHANGE24HOUR'], '+')
except:
	print('oops the api is dead')
	prices['ETH'] = (0, 0, '+')
	prices['ETC'] = (0, 0, '+')
	
# end

# prevent enablesalad from working


if enablesalad:
	enablesalad = False
	fancytype('[salad] Enablesalad has been disabled | We aren\'t allowed to use the salad api...', colors=[
			  'default_colors.FAIL'])
	fancytype('[salad] Remove this message by changing enablesalad to false in colors.json', colors=[
			  'default_colors.FAIL'])
	fancytype('[salad] Or remove this part of code to use balance tracker | This officially isn\'t allowed', colors=[
			  'default_colors.FAIL'])
	time.sleep(2)

# You can delete this part to allow enablesalad
# However the saladlogreader dev team does not care what happens to ur account if u do
# have fun :D


with open(path) as f:
	oldest = f.readlines()[-1]

if presence:
	try:
		from pypresence import Presence
	except ImportError:
		print('not found a few modules press any key to install')
		os.system('pause')
		os.system('pip install pypresence --user')
		from pypresence import Presence
	rpc = Presence(int(pclient))
	rpc.connect()
	fancytype('[rpc] ok', colors=['default_colors.OKGREEN'])
	oldp = int(time.time())
	
if enablesalad:
	fancytype('[salad] enabled!', colors=['default_colors.OKGREEN'])
	headers = {
		"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Salad/0.4.0 Chrome/78.0.3904.130 Electron/7.1.9 Safari/537.36'
	}
	try:
		import requests
		from dotenv import load_dotenv
		load_dotenv()
		from win10toast import ToastNotifier
		toaster = ToastNotifier()
		salad_antiforgery = os.getenv('SALAD_ANTIFORGERY')
		salad_authentication = os.getenv('SALAD_AUTHENTICATION')
		if salad_authentication is not None and salad_antiforgery is not None:
			print(' all good!!!!')
		else:
			print(' pls check ur .env file again')
			os.system('pause')
			exit()

	except ModuleNotFoundError:
		print('Missing modules! press any key to install')
		os.system('pause')
		os.system('pip install -r requirements.txt --user')
		time.sleep(5)
		import requests
		from dotenv import load_dotenv
		load_dotenv()
		from win10toast import ToastNotifier
		toaster = ToastNotifier()
		salad_antiforgery = os.getenv('SALAD_ANTIFORGERY')
		salad_authentication = os.getenv('SALAD_AUTHENTICATION')

	cookie = {
		"Salad.Antiforgery": salad_antiforgery,
		"Salad.Authentication": salad_authentication
	}
	try:
		r = requests.get(url='https://app-api.salad.io/api/v1/profile/balance',
						 cookies=cookie, headers=headers)
		if r.status_code != 200:
			print(
				f'{default_colors.WARNING}{default_colors.BOLD}[api] Error! Something went wrong with the salad api! Probably a 401... Check the auth tokens in the .env file{default_colors.ENDC}')
			os.system('pause')
		jason = r.json()
		oldbalance = jason['currentBalance']
		pongbal = oldbalance
		e = 0
	except requests.ConnectionError:
		print(f'{default_colors.WARNING}{default_colors.BOLD}Bad error! Either salad is down or the caveman (SharOfGod) running this doesnt have internet{default_colors.ENDC}')
		enablesalad = False

if enablekey:
	try:
		import keyboard
		from win32gui import GetWindowText, GetForegroundWindow
	except ModuleNotFoundError:
		print('Missing modules! press any key to install')
		os.system('pause')
		os.system('pip install -r requirements.txt --user')
		time.sleep(5)
		import keyboard
		from win32gui import GetWindowText, GetForegroundWindow
rmh = False
asp = 0
while True:
	time.sleep(0.5)
	matches = False
	try:
		with open(path) as f:
			line = f.readlines()
			for i in range(1, limit+1):
				lien = line[-i].replace('\n', '')
				# print('-------------')
				# print(lien, i)
				# print(oldest)
				if lien == oldest:
					matches = True
					oldest = line[-1].replace('\n', '')
					num = i
					break
			if not matches:
				oldest = line[-1].replace('\n', '')
				num = limit+1
			for i in reversed(range(1, num)):
				lien = line[-i].replace('\n', '')
				try:
					if 'Eth: Mining ' in lien:
						cn = lien.split('Eth: Mining ')[1].split(' on')[0]
						fancytype('[info] ' + cn + ' price: $' + str(prices[cn][0]) + ' (' + prices[cn][2] + '$' + str(abs(math.floor(prices[cn][1]*100000)/100000)) + ' from 24h ago)')
				except:
					pass
				if rmh:
					if 'Eth speed: ' in lien:
						sped = float(lien.split('speed: ')[
									 1].split(' MH/s,')[0])
						mhs['counts'] += 1
						mhs['total'] += sped
				if 'Eth: Average speed' in lien:
					asp = float(lien.split('min): ')[1].split(' MH/s')[0])
				if 'shares' and 'time' in lien:
					tme = lien.split('time: ')[1]
				if not coloorswork:
					if 'ETH share found!' in lien:
						fancytype(f'{lien}', notime=True, colors=[
								  'default_colors.OKGREEN', 'default_colors.BOLD'])
					elif 'GPU' in lien:
						fancytype(f'{lien}', notime=True, colors=[
								  'default_colors.OKBLUE', 'default_colors.BOLD'])
					elif 'Eth: Average speed' in lien:
						fancytype(f'{lien}', notime=True, colors=[
								  'default_colors.FAIL', 'default_colors.BOLD'])
					else:
						fancytype(lien, notime=True)
				else:
					found = False
					for blah in coloors['custom_text'].keys():
						if blah in lien:
							fancytype(f'{lien}', notime=True,
									  colors=coloors['custom_text'][blah])
							found = True
							break
					if not found:
						fancytype(lien, notime=True)

		if enablesalad:
			if e >= 10:
				fancytype('[salad] checking balance')
				cookie = {
					"Salad.Antiforgery": salad_antiforgery,
					"Salad.Authentication": salad_authentication
				}
				r = requests.get(
					url='https://app-api.salad.io/api/v1/profile/balance', cookies=cookie, headers=headers)
				if r.status_code != 200:
					print(
						f'{default_colors.WARNING}{default_colors.BOLD}[api] Error! Something went wrong with the salad api! Probably a 401... Check the auth tokens in the .env file{default_colors.ENDC}')
					continue
				jason = r.json()
				if jason['currentBalance'] > oldbalance:
					diff = jason['currentBalance'] - oldbalance
					oldbalance = jason['currentBalance']
					fancytype('[salad] balance increased by $' + str(diff), colors=[
							  'default_colors.OKGREEN', 'default_colors.BOLD', 'default_colors.UNDERLINE'])
					fancytype('[salad] new salad balance: $' + str(jason['currentBalance']), colors=[
							  'default_colors.OKGREEN', 'default_colors.BOLD', 'default_colors.UNDERLINE'])
					if jason['currentBalance'] - pongbal > notifthreshold:
						fancytype('[salad] sending a notification', colors=[
								  'default_colors.OKGREEN', 'default_colors.BOLD', 'default_colors.UNDERLINE'])
						toaster.show_toast("salad log thing", "balance increased by " + str(
							jason['currentBalance'] - pongbal) + ' since last notification!', threaded=True, icon_path=None, duration=3)
						pongbal = jason['currentBalance']
				else:
					fancytype('[salad] Balance didnt change')
				e = 0
			else:
				e += 1

		if enablekey:
			if keyboard.is_pressed('e') and GetWindowText(GetForegroundWindow()) == title:
				print(' Stoped logs')
				print(' You can now type stuff (try "help")')
				while True:
					inp = input(' > ')
					if inp == 'help':
						print(' here is h e l p:\n help - show this\n balance - show balance\n recordmhs - record hashrate to get average later\n rainbow - toggle SHINY\n exit - resume log river')
					elif inp == 'balance':
						if enablesalad:
							r = requests.get(
								url='https://app-api.salad.io/api/v1/profile/balance', cookies=cookie, headers=headers)
							if r.status_code != 200:
								print(
									f'{default_colors.WARNING}{default_colors.BOLD}less bad error! fuck something went wrong with salad api thing probably another 401 go check the auth tokens{default_colors.ENDC}')
								continue
							jason = r.json()
							print(' Balance is $', jason['currentBalance'])
						else:
							print(' You dont have salad balance tracker enabled')
					elif inp == 'rainbow':
						rainbow = not rainbow
						print(rainbow, ' This is extremely buggy so logs will go oof')
					elif inp == 'recordmhs':
						if rmh:
							print('average mh/s:', mhs['total']/mhs['counts'])
						rmh = not rmh
						mhs = {
							"total": 0,
							"counts": 0
						}
						print(rmh, 'ok')
					elif inp == 'exit':
						break

		if presence:
			if int(time.time()) > oldp + 30:
				oldp = int(time.time())
				fancytype('[rpc] updating')
				rpc.update(state = 'MH/s: ' + str(asp), details = 'Chopping for: ' + tme)
			
	except Exception as o:
		print(traceback.format_exc())
		print(f'{default_colors.WARNING}{default_colors.BOLD}Bad error!{default_colors.ENDC}{default_colors.DEFAULT}', str(o))
