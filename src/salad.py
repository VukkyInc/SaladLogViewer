

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

enablesalad = True # set to true if u wanna see balance updates in logs

title = 'fancy salad miner logs'

notifthreshold = 0.0001 # ping when balance changes by this

# settings end (shark make this in a json file idiot)

import os
import time
import traceback

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

with open(path) as f:
	oldest = f.readlines()[-1]

if enablesalad:
	try:
		import requests
		from dotenv import load_dotenv
		load_dotenv()
		from datetime import datetime
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
		print('not found a few modules pls approve admin prompt to install')
		os.system('pause')
		os.system(""" powershell "start cmd -Verb runAs -Argumentlist '/c', 'cd', '""" + os.path.abspath(os.getcwd()) +"""', '&', 'pip', 'install', '-r', 'requirements.txt'" """)
		time.sleep(5)
		import requests
		from dotenv import load_dotenv
		load_dotenv()
		from datetime import datetime
		from win10toast import ToastNotifier
		toaster = ToastNotifier()
		salad_antiforgery = os.getenv('SALAD_ANTIFORGERY')
		salad_authentication = os.getenv('SALAD_AUTHENTICATION')

	cookie = {
		"Salad.Antiforgery": salad_antiforgery,
		"Salad.Authentication": salad_authentication
	}
	r = requests.get(url = 'https://app-api.salad.io/api/v1/profile/balance', cookies = cookie)
	if r.status_code != 200:
		print(f'{bcolors.WARNING}{bcolors.BOLD}less bad error! fuck something went wrong with salad api thing probably another 401 go check the auth tokens{bcolors.ENDC}')
		os.system('pause')
	jason = r.json()
	oldbalance = jason['currentBalance']
	pongbal = oldbalance
	e = 0

def fancytype(words, notime=False, colors=[]):
	words = ' ' + words
	for color in colors:
		words = color + words
	if not notime:
		words = timenow() + ' ' + words
	strin = ''
	for let in words:
		strin = strin + let
		print(strin, end='\r')
		time.sleep(0.0078125)
	print(words + bcolors.ENDC + bcolors.DEFAULT)

def timenow():
	return '[' + str(datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]) + ']'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DEFAULT = '\033[37;1m'

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
				if 'ETH share found!' in lien:
					fancytype(f'{lien}', notime=True, colors=[bcolors.OKGREEN, bcolors.BOLD])
				elif 'GPU1:' in lien:
					fancytype(f'{lien}', notime=True, colors=[bcolors.OKBLUE, bcolors.BOLD])
				elif 'Eth: Average speed' in lien:
					fancytype(f'{lien}', notime=True, colors=[bcolors.FAIL, bcolors.BOLD])
				else:
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
					print(f'{bcolors.WARNING}{bcolors.BOLD}less bad error! fuck something went wrong with salad api thing probably another 401 go check the auth tokens{bcolors.ENDC}')
					continue
				jason = r.json()
				if jason['currentBalance'] > oldbalance:
					diff = jason['currentBalance'] - oldbalance
					oldbalance = jason['currentBalance']
					fancytype('[salad] balance increased by $' + str(diff), colors=[bcolors.OKGREEN, bcolors.BOLD, bcolors.UNDERLINE])
					fancytype('[salad] new salad balance: $' + str(jason['currentBalance']), colors=[bcolors.OKGREEN, bcolors.BOLD, bcolors.UNDERLINE])
					if jason['currentBalance'] - pongbal > notifthreshold:
						fancytype('[salad] sending a notification', colors=[bcolors.OKGREEN, bcolors.BOLD, bcolors.UNDERLINE])
						toaster.show_toast("salad log thing", "balance increased by " + str(jason['currentBalance'] - pongbal) + ' since last notification!', threaded=True, icon_path=None, duration=3)
						pongbal = jason['currentBalance']
				else:
					fancytype('[salad] balance didnt change')
				e = 0
			else:
				e += 1
	except Exception as o:
		print(traceback.format_exc())
		print(f'{bcolors.WARNING}{bcolors.BOLD}bad bad error!{bcolors.ENDC}{bcolors.DEFAULT}', str(o))
