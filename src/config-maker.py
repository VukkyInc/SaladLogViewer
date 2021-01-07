import json
import os

print('gonna try finding colors.json first')
try:
	with open('colors.json') as f:
		js = json.load(f)
	print('ok found it')
except:
	print('hmm something wrong maybe its not there')
	js = {}
while True:
	os.system('cls')
	print('salad log config maker')
	print('-------------------')
	print('1 - edit custom colors')
	print('2 - edit custom text')
	print('3 - save and exit')
	ch = int(input('>>> '))
	if ch == 1:
		while True:
			os.system('cls')
			print('your custom colors:\n')
			if not 'custom_colors' in js:
				js['custom_colors'] = {}
			for name, color in js['custom_colors'].items():
				if '/comment' in name:
					continue
				print(name + ': ' + color + 'Lorem ipsum dolor sit amet...\033[0m\n')
			if len(js['custom_colors']) == 0:
				print('none')
			print('-------------------')
			print('1 - add a color')
			print('2 - remove a color')
			print('3 - back')
			ch2 = int(input('>>> '))
			print('-------------------')
			if ch2 == 1:
				cname = input('what should the name be?\n>>> ')
				print('-------------------')
				cansi = input('what is the ansi color?\nhttp://bit.ly/ansicolors\nexample: \\u001b[31m\n>>> ').encode().decode('unicode-escape')
				# that line above took way too long to figure out...
				js['custom_colors'][cname] = cansi
				print('added that')
			elif ch2 == 2:
				cname = input('what is the name?\n>>> ')
				if cname in js['custom_colors']:
					del js['custom_colors'][cname]
					print('deleted that')
				else:
					print('didnt find that color - is the name correct?')
			elif ch2 == 3:
				break
	elif ch == 2:
		while True:
			os.system('cls')
			print('your custom text:\n(change line color if these words are found in it)\n')
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
			defc = {
				"HEADER": '\033[95m',
				"OKBLUE": '\033[94m',
				"OKGREEN": '\033[92m',
				"WARNING": '\033[93m',
				"FAIL": '\033[91m',
				"ENDC": '\033[0m',
				"BOLD": '\033[1m',
				"UNDERLINE": '\033[4m',
				"DEFAULT": '\033[37;1m'
			}
			class custom_colors:
				pass
			if not 'custom_text' in js:
				js['custom_text'] = {}
			if not 'custom_colors' in js:
				js['custom_colors'] = {}
			for color in js['custom_colors'].keys():
				setattr(custom_colors, color, js['custom_colors'][color])
			for name, colors in js['custom_text'].items():
				if '/comment' in name:
					continue
				fc = ''
				for color in colors:
					fc += eval(color)
				print(fc + '"' + name + '"\033[0m\n')
			if len(js['custom_text']) == 0:
				print('none')

			print('1 - add condition')
			print('2 - remove condition')
			print('3 - back')

			ch2 = int(input('>>> '))

			if ch2 == 1:
				cansi = []
				print('what colors?\ndefault colors:')
				for name, color in defc.items():
					print(name + ': ' + color + 'Lorem ipsum dolor sit amet...\033[0m\n')
				print('your custom colors:\n')
				for name, color in js['custom_colors'].items():
					if '/comment' in name:
						continue
					print(name + ': ' + color + 'Lorem ipsum dolor sit amet...\033[0m\n')
				while True:
					cadd = input('you can add multiple colors (case sensitive!) - continue by typing "next"\n>>> ')
					if cadd != 'next':
						if cadd in js['custom_colors']:
							cansi.append('custom_colors.' + cadd)
							print('added ' + cadd + ' (custom)')
						elif cadd in defc:
							cansi.append('default_colors.' + cadd)
							print('added ' + cadd + ' (default)')
						else:
							print('hmmmm that doesnt look like a color - did u make a mistake?')
					else:
						break
				print('-------------------')
				cname = input('what words would make the line change to that color?\n(case sensitive as well!)\n>>> ')
				# that line above took way too long to figure out...
				js['custom_text'][cname] = cansi
				print('added that')
			elif ch2 == 2:
				cname = input('what are the words?\n>>> ')
				if cname in js['custom_text']:
					del js['custom_text'][cname]
					print('deleted that')
				else:
					print('didnt find that color - is the name correct?')
			elif ch2 == 3:
				break

	elif ch == 3:
		with open('colors.json', 'w+') as f:
			f.write(json.dumps(js, indent=4, sort_keys=True))
		print('saved! bye bye')
		#print(js)
		break