
# settings begin

import random
from datetime import datetime
import json
import os
import time
try:
	import requests
except ImportError:
	print('not found a few modules press any key to install')
	os.system('pause')
	os.system('pip install -r requirements.txt --user')
import traceback
import math
rainbow = False
try:
	with open('colors.json') as f:
		coloors = json.load(f)
	coloorswork = True
	title = coloors['settings']['window_title']
	presence = coloors['settings']['experimental_discord_presence']
	prmsgs = coloors['settings']['presence_messages']
	pclient = coloors['settings']['presence_client_id']
	typewriteroff = coloors['settings']['disable_typewriter']
	class custom_colors:
		pass
	for color in coloors['custom_colors'].keys():
		setattr(custom_colors, color, coloors['custom_colors'][color])
except Exception as e:
	print(traceback.format_exc())
	print('colors.json error using defaults')
	coloorswork = False
	presence = False
	title = 'fancy salad miner logs'
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
			newwords = newwords + eval('default_colors.rainbow_' + str(random.randint(1,6))) + letter
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
	print('[news] ' + r.text[1:-2])
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

with open(path) as f:
	oldest = f.readlines()[-1]

rmh = False
asp = 0
di = 0
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
		if presence:
			if int(time.time()) > oldp + 30:
				oldp = int(time.time())
				fancytype('[rpc] updating')
				hrs = tme.split(':')[0]
				mins = tme.split(':')[1]
				secs = int(hrs) * 3600 + int(mins) * 60
				now = int(time.time())
				diff = now - secs
				rpc.update(state = 'mh/s: ' + str(asp), details = prmsgs[di], start = diff)
				di += 1
				if di >= len(prmsgs):
					di = 0

	except Exception as o:
		print(traceback.format_exc())
		print(f'{default_colors.WARNING}{default_colors.BOLD}Bad error!{default_colors.ENDC}{default_colors.DEFAULT}', str(o))
