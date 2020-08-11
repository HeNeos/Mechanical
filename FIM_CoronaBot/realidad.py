#!/usr/bin/python3
from webbot import Browser
import time
name = "Josue Huaroto"
email = "josue.huaroto.v@uni.pe"
link = "https://unidemo.webex.com/unidemo/e.php?MTID=m4ff5ebd3849b3d6b4608d8efecc23c2a"
T = 117*60 #TOTAL TIME, 117 mins

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
web.type(data)
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
