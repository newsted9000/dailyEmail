# Imports
import pyautogui
import time
import webbrowser
import datetime
from daily_email_config import *

# Getting to gmail 
pyautogui.PAUSE = 1 	
webbrowser.open("http://gmail.com")
time.sleep(5)


# signing in if necesary
if pyautogui.locateOnScreen(google_chrome) == None: 
	None
else: 
	pyautogui.press('tab')
	pyautogui.press('enter')
	pyautogui.typewrite(gmail_pass)
	pyautogui.press('enter')
	time.sleep(5)

# compose, email destination, and date
c = pyautogui.locateOnScreen(gmail_compose)
pyautogui.click(c[0], c[1])
pyautogui.typewrite(recipient_email)
pyautogui.press('enter')
pyautogui.press('tab')
d = str(datetime.datetime.today())
pyautogui.typewrite(d[:10]) 
pyautogui.press('tab')
e = datetime.datetime.weekday(datetime.datetime.today())

# Personal contents 
if personal == True:

	pyautogui.typewrite(quote_one)
	pyautogui.press(['enter', 'enter'])

	pyautogui.typewrite(quote_two)
	pyautogui.press(['enter', 'enter'])

	pyautogui.typewrite(quote_three)
	pyautogui.press(['enter', 'enter'])

	pyautogui.typewrite(quote_four)
	pyautogui.press(['enter', 'enter'])

	pyautogui.typewrite('Meditate')
	pyautogui.press('enter')
	pyautogui.press('enter')

	# timer 
	pyautogui.hotkey('ctrl', 'k')
	pyautogui.typewrite('https://www.google.com.ar/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=timer')
	pyautogui.press('enter')
	pyautogui.press('enter')
	pyautogui.press('enter')

	pyautogui.typewrite('Morning Pages')
	pyautogui.press('enter')
	pyautogui.press('enter')

	pyautogui.typewrite('Call Grandpa')
	pyautogui.press('enter')
	pyautogui.press('enter')

	pyautogui.typewrite('Anki')
	pyautogui.press('enter')
	pyautogui.press('enter')

	pyautogui.hotkey('ctrl', 'k')
	pyautogui.typewrite(link_one)
	pyautogui.press('enter')
	pyautogui.press('enter')
	pyautogui.press('enter')

	pyautogui.hotkey('ctrl', 'k')
	pyautogui.typewrite(link_two)
	pyautogui.press('enter')
	pyautogui.press('enter')
	pyautogui.press('enter')

	pyautogui.hotkey('ctrl', 'k')
	pyautogui.typewrite(link_three)
	pyautogui.press('enter')
	pyautogui.press('enter')
	pyautogui.press('enter')

	# Links only on specific days of the weex
	# Monday == 0 etc....
	if e == 0: 
		pyautogui.hotkey('ctrl', 'k')
		pyautogui.typewrite(link_four)
		pyautogui.press('enter')
		pyautogui.press('enter')
		pyautogui.press('enter')
	elif e == 1: 
		pyautogui.hotkey('ctrl', 'k')
		pyautogui.typewrite(link_five)
		pyautogui.press('enter')
		pyautogui.press('enter')
		pyautogui.press('enter')
	elif e == 2: 
		pyautogui.hotkey('ctrl', 'k')
		pyautogui.typewrite(link_six)
		pyautogui.press('enter')
		pyautogui.press('enter')
		pyautogui.press('enter')
	elif e == 3: 
		pyautogui.hotkey('ctrl', 'k')
		pyautogui.typewrite(link_four)
		pyautogui.press('enter')
		pyautogui.press('enter')
		pyautogui.press('enter')
	elif e == 4: 
		pyautogui.hotkey('ctrl', 'k')
		pyautogui.typewrite(link_seven)
		pyautogui.press('enter')
		pyautogui.press('enter')
		pyautogui.press('enter')

	elif e == 5: 
		pyautogui.hotkey('ctrl', 'k')
		pyautogui.typewrite(link_eight)
		pyautogui.press('enter')
		pyautogui.press('enter')
		pyautogui.press('enter')
	else:
		pyautogui.hotkey('ctrl', 'k')
		pyautogui.typewrite(link_nine)
		pyautogui.press('enter')
		pyautogui.press('enter')
		pyautogui.press('enter')

	# Messenger link
	pyautogui.hotkey('ctrl', 'k')
	pyautogui.typewrite(link_ten)
	pyautogui.press('enter')
	pyautogui.press('enter')
	pyautogui.press('enter')

if professional == True:

	pyautogui.typewrite(pro_text_one)
	pyautogui.press('enter')

	pyautogui.typewrite(pro_text_two)
	pyautogui.press('enter')
	pyautogui.press('enter')

	pyautogui.typewrite(pro_text_three)
	pyautogui.press('enter')
	pyautogui.press('enter')

	pyautogui.hotkey('ctrl', 'k')
	pyautogui.typewrite(pro_link_two)
	pyautogui.press('enter')
	pyautogui.press('enter')
	pyautogui.press('enter')

	pyautogui.hotkey('ctrl', 'k')
	pyautogui.typewrite(pro_link_three)
	pyautogui.press('enter')
	pyautogui.press('enter')
	pyautogui.press('enter')

	pyautogui.typewrite(pro_text_four)
	pyautogui.press('enter')
	pyautogui.press('enter')

	pyautogui.typewrite(pro_text_five)
	pyautogui.press('enter')
	pyautogui.press('enter')

	pyautogui.hotkey('ctrl', 'k')
	pyautogui.typewrite(pro_link_one)
	pyautogui.press('enter')
	pyautogui.press('enter')
	pyautogui.press('enter')

	

# send email
pyautogui.hotkey('ctrl', 'enter')
time.sleep(3)

# sign in to facebook messenger
if sign_in_messenger == True: 
	
	pyautogui.hotkey('ctrl', 'l')
	pyautogui.typewrite('https://www.messenger.com/')
	pyautogui.press('enter')
	time.sleep(5)
	pyautogui.press('tab')
	pyautogui.press('tab')
	pyautogui.typewrite('CIXCeaoeucC2586')
	pyautogui.press('enter')
	time.sleep(5)

# closing the programs
if close_chrome == True:
	pyautogui.hotkey('alt','f4')
	pyautogui.hotkey('alt','f4')

