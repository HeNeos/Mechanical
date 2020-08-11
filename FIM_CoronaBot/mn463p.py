#!/usr/bin/python3
from webbot import Browser
import time
name = "Josue Huaroto"
email = "josue.huaroto.v@uni.pe"
link = "https://unidemo.webex.com/meet/isalazar"
T = 177*60 #TOTAL TIME, 177 mins

info = name + '\t' + email

to = time.time()
web = Browser()
web.go_to(link)
web.click("Entrar a la reunión")

def _try():	
	if web.exists('This is not a real button'):
		return False
	else:
		return True		

for i in range(0,2):
    _try()
web.press(web.Key.ENTER)

for i in range(0,2):
    _try()
web.type(info)
web.press(web.Key.ENTER)

for i in range(0,2):
    if _try():
        web.press(web.Key.ESCAPE)

for i in range(0,2):
    _try()
    web.press(web.Key.ENTER)


#DEBUG >:V

for i in range(0,3):
    if _try():
        web.press(web.Key.TAB)
web.press(web.Key.ENTER)
for i in range(0,5):
    if _try():
        web.press(web.Key.TAB)
web.press(web.Key.ENTER)


while(True):
    if((time.time()-to)%600 == 0):
        print((time.time()-to)/60, "minutes")
    if(time.time()-to >= T):
        web.quit()
        break
