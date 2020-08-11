#!/usr/bin/python3
from webbot import Browser
web = Browser()
web.go_to('https://unidemo.webex.com/meet/isalazar')
#web.go_to('https://unidemo.webex.com/webappng/sites/unidemo/dashboard/pmr/huaman1942?siteurl=unidemo')
web.click("Entrar a la reunión")
#web.go_to('https://unidemo.webex.com/webappng/sites/unidemo/meeting/download/ddc993d54459e2515c68cceb6856bfec?launchApp=true')
for i in range(0,2):
    if(web.exists("IDONTKNOW")):
        web.click("IDK")

web.press(web.Key.ENTER)
for i in range(0,2):
    print(i)
    if(web.exists("IDONTKNOW")):
        web.click("IDK")
web.type('Josue Huaroto\tjosue.huaroto.v@uni.pe')
#for i in range(0,1):
#    if(web.exists("IDONTKNOW")):
#        web.click("IDK")
web.press(web.Key.ENTER)
for i in range(0,7):
    print(i)
    if(web.exists('Saltear')):
        web.click('Saltear')
    else:
        web.press(web.Key.ESCAPE)

for i in range(0,6):
    if(web.exists('Saltear')):
        web.click('Saltear')
    web.press(web.Key.ENTER)
for i in range(0,7):
    print(i)
    if(web.exists('Entrar a reunión')):
        web.click('Entrar a reunión')
    else:
        web.press(web.Key.TAB)
web.press(web.Key.ENTER)


