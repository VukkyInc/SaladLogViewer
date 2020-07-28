

# made this to track my salad mining hashrate in real time!

# readme starts

# shitty code i know

# how to get enablesalad to work:
# 1: go to app.salad.io
# 2: click on lock near url
# 3: go to cookies
# 4: open app-api.salad.io folder
# 5: copy salad.antiforgery and salad.authentication into a ".env" file like this:
# SALAD_ANTIFORGERY='antiforgery goes here'
# SALAD_AUTHENTICATION='authentication goes here'
# 6: make sure salad.py is in same folder as the .env
# 7: try starting
# 8: pray that it works
# if it works: yay!
# if it doesnt: fuck! dm SharkOfGod#8424

# readme ends

# settings begin

import json
import os
import time
import traceback
try:
	with open('colors.json') as f:
		coloors = json.load(f)
	coloorswork = True
	enablesalad = coloors['settings']['enable_salad_balance_tracker']
	title = coloors['settings']['window_title']
	notifthreshold = coloors['settings']['balance_notification_every']
	class custom_colors:
		pass
	for color in coloors['custom_colors'].keys():
		setattr(custom_colors, color, coloors['custom_colors'][color])
except Exception as e:
	print(traceback.format_exc())
	print('colors.json error using defaults')
	coloorswork = False
	enablesalad = False # balance updates in logs
	title = 'fancy salad miner logs'
	notifthreshold = 1 # ping when balance changes by this

# settings end (shark made settings in a json file therefore he is no longer an idiot)

# try:
# 	from win32gui import GetWindowText, GetForegroundWindow
# 	if GetWindowText(GetForegroundWindow()) == '': # force cmd.exe usage
# 		os.system('start py salad.py')
# 		exit()
# except ModuleNotFoundError:
# 	pass

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

def fancytype(words, notime=False, colors=[]):
	colorwords = ''
	for color in colors:
		colorwords = eval(color) + colorwords
	if not notime:
		words = ' ' + colorwords + timenow() + ' ' + words
	else:
		words = ' ' + colorwords + words
	strin = ''
	for let in words:
		strin = strin + let
		print(strin, end='\r')
		time.sleep(0.0078125)
	print(words + default_colors.ENDC + default_colors.DEFAULT)

with open(path) as f:
	oldest = f.readlines()[-1]

from datetime import datetime

if enablesalad:
	try:
		import requests
		from dotenv import load_dotenv
		load_dotenv()
		from win10toast import ToastNotifier
		toaster = ToastNotifier()
		salad_antiforgery = os.getenv('SALAD_ANTIFORGERY')
		salad_authentication = os.getenv('SALAD_AUTHENTICATION')
		if salad_authentication is not None and salad_antiforgery is not None:
			print('all good!!!!')
		else:
			print('pls check ur .env file again')
			os.system('pause')
			exit()

	except ModuleNotFoundError:
		print('not found a few modules press any key to install')
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
		r = requests.get(url = 'https://app-api.salad.io/api/v1/profile/balance', cookies = cookie)
		if r.status_code != 200:
			print(f'{default_colors.WARNING}{default_colors.BOLD}less bad error! fuck something went wrong with salad api thing probably another 401 go check the auth tokens{default_colors.ENDC}')
			os.system('pause')
		jason = r.json()
		oldbalance = jason['currentBalance']
		pongbal = oldbalance
		e = 0
	except requests.ConnectionError:
		print(f'{default_colors.WARNING}{default_colors.BOLD}bad bad error! either salad is down or the caveman running this doesnt have internet{default_colors.ENDC}')
		enablesalad = False

def timenow():
	return '[' + str(datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]) + ']'

def updatever(): # absolutely not copy pasted from my bots code
	if os.path.isfile('noupdate.txt'):
		fancytype('[update] noupdate')
		return
	try:
		import requests
	except ModuleNotFoundError:
		fancytype('[update] requests is required to update!')
		return
	try:
		with open('version.txt') as f:
			ver = int(f.read())
		chver = requests.get(url = 'http://api.shruc.ml/saladlog/version', params = {})
		chver = chver.text.replace('\n', '')
		chver = chver.replace('"', '')
		if int(chver) > ver:
			fancytype('[update] update available! press any key or create a noupdate.txt file and restart')
			os.system('pause')
			time.sleep(1)
			with open('temp.py', 'w+') as f:
				file = __file__.replace('\\', '/')
				print(file)
				comd = 'print("hold on im updating myself lmao")\nimport time\nimport requests\nr = requests.get(url = "http://api.shruc.ml/saladlog/download", params = {})\nwith open("' + file + '", "w+") as f:\n\tf.write(r.text)\nr = requests.get(url = "http://api.shruc.ml/saladlog/version", params = {})\nwith open("version.txt", "w+") as f:\n\tf.write("'+ chver +'")\ntime.sleep(1)\nimport os\nos.system(\'start cmd /c "del temp.py & start py ' + file + '\')'
				f.write(comd)
			os.system('start cmd /c py temp.py')
			os.system('exit')
			exit()
		else:
			fancytype('[update] up to date!')
	except requests.ConnectionError as e:
		print('website went poo >:C')
	except Exception as e:
		print(str(e))
		print('if this is ur first time running this thing then ignore')
		with open('version.txt', 'w+') as f:
			f.write('1')

updatever()
while True:
	time.sleep(0.5)
	matches = False
	try:
		with open(path) as f:
			line = f.readlines()
			for i in range(1, limit+1):
				lien = line[-i].replace('\n', '')
				#print('-------------')
				#print(lien, i)
				#print(oldest)
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
				if not coloorswork:
					if 'ETH share found!' in lien:
						fancytype(f'{lien}', notime=True, colors=['default_colors.OKGREEN', 'default_colors.BOLD'])
					elif 'GPU' in lien:
						fancytype(f'{lien}', notime=True, colors=['default_colors.OKBLUE', 'default_colors.BOLD'])
					elif 'Eth: Average speed' in lien:
						fancytype(f'{lien}', notime=True, colors=['default_colors.FAIL', 'default_colors.BOLD'])
					else:
						fancytype(lien, notime=True)
				else:
					found = False
					for blah in coloors['custom_text'].keys():
						if blah in lien:
							fancytype(f'{lien}', notime=True, colors=coloors['custom_text'][blah])
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
				r = requests.get(url = 'https://app-api.salad.io/api/v1/profile/balance', cookies = cookie)
				if r.status_code != 200:
					print(f'{default_colors.WARNING}{default_colors.BOLD}less bad error! fuck something went wrong with salad api thing probably another 401 go check the auth tokens{default_colors.ENDC}')
					continue
				jason = r.json()
				if jason['currentBalance'] > oldbalance:
					diff = jason['currentBalance'] - oldbalance
					oldbalance = jason['currentBalance']
					fancytype('[salad] balance increased by $' + str(diff), colors=['default_colors.OKGREEN', 'default_colors.BOLD', 'default_colors.UNDERLINE'])
					fancytype('[salad] new salad balance: $' + str(jason['currentBalance']), colors=['default_colors.OKGREEN', 'default_colors.BOLD', 'default_colors.UNDERLINE'])
					if jason['currentBalance'] - pongbal > notifthreshold:
						fancytype('[salad] sending a notification', colors=['default_colors.OKGREEN', 'default_colors.BOLD', 'default_colors.UNDERLINE'])
						toaster.show_toast("salad log thing", "balance increased by " + str(jason['currentBalance'] - pongbal) + ' since last notification!', threaded=True, icon_path=None, duration=3)
						pongbal = jason['currentBalance']
				else:
					fancytype('[salad] balance didnt change')
				e = 0
			else:
				e += 1
	except Exception as o:
		print(traceback.format_exc())
		print(f'{default_colors.WARNING}{default_colors.BOLD}bad bad error!{default_colors.ENDC}{default_colors.DEFAULT}', str(o))
