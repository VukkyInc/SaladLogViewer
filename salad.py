
# made this to track my salad mining hashrate in real time!

import os
import time
import traceback
try:
	from win32gui import GetWindowText, GetForegroundWindow
	if GetWindowText(GetForegroundWindow()) == '': # force cmd.exe usage
		os.system('start py salad.py')
		exit()
except ModuleNotFoundError:
	pass
os.system('title fancy salad miner logs')
limit = 10
path = os.getenv('APPDATA')
path = path + '/salad/logs/main.log'
with open(path) as f:
	oldest = f.readlines()[-1]
print(oldest)
enablesalad = True # set to true if u wanna see balance updates in logs
if enablesalad:
	import requests
	from dotenv import load_dotenv
	load_dotenv()
	from datetime import datetime
	oldbalance = 0
	e = 0
def fancytype(words):
	words = ' ' + words
	strin = ''
	for let in words:
		strin = strin + let
		print(strin, end='\r')
		time.sleep(0.0078125)
	print(words)
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
				if lien != oldest:
					if 'ETH share found!' in lien:
						fancytype(f'{bcolors.OKGREEN}{bcolors.BOLD}{lien}{bcolors.ENDC}{bcolors.DEFAULT}')
					elif 'GPU1:' in lien:
						fancytype(f'{bcolors.OKBLUE}{bcolors.BOLD}{lien}{bcolors.ENDC}{bcolors.DEFAULT}')
					elif 'Eth: Average speed' in lien:
						fancytype(f'{bcolors.FAIL}{bcolors.BOLD}{lien}{bcolors.ENDC}{bcolors.DEFAULT}')
					else:
						fancytype(lien)
				else:
					matches = True
					oldest = line[-1].replace('\n', '')
					break
			if not matches:
				oldest = line[-1].replace('\n', '')
		if enablesalad:
			if e >= 10:
				fancytype('[' + str(datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]) + ']' + ' [salad] checking balance')
				salad_antiforgery = os.getenv('SALAD_ANTIFORGERY')
				salad_authentication = os.getenv('SALAD_AUTHENTICATION')
				cookie = {
					"Salad.AntiForgery": salad_antiforgery,
					"Salad.Authentication": salad_authentication
				}
				r = requests.get(url = 'https://app-api.salad.io/api/v1/profile/balance', cookies = cookie)
				if r.status_code != 200:
					print(f'{bcolors.WARNING}{bcolors.BOLD}not a miner error! fuck something went wrong with salad api thing probably another 401 go check the auth tokens{bcolors.ENDC}')
					continue
				jason = r.json()
				if jason['currentBalance'] > oldbalance:
					diff = jason['currentBalance'] - oldbalance
					oldbalance = jason['currentBalance']
					strn = bcolors.OKGREEN + bcolors.BOLD + bcolors.UNDERLINE + '[' + str(datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]) + ']' + \
						' [salad] balance increased by $' + str(diff) + bcolors.ENDC + bcolors.DEFAULT
					fancytype(strn)
				else:
					fancytype('[' + str(datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]) + ']' + ' [salad] balance didnt change')
				e = 0
			else:
				e += 1
	except Exception as o:
		print(traceback.format_exc())
		print(f'{bcolors.WARNING}{bcolors.BOLD}not a miner error!{bcolors.ENDC}{bcolors.DEFAULT}', str(o))