#!/usr/bin/python3
from webbot import Browser
web = Browser()
web.go_to('http://www.earpunifim.com/')
web.type("YOUR_CODE", into="Usuario UNI")
web.type("YOUR_PASSWORD", into="Password")
web.press(web.Key.ENTER)
web.click("Mi Asistencia", id="asistencia_alumno_utfim")
T = 116*60
t = time.time()
while  True:
	if time.time()-t >= T:
		web.quit()
		break
	if web.exists(css_selector=".mdl-button.mdl-js-button.mdl-button--raised.mdl-js-ripple-effect.btnMarcar.mdl-button--colored"):
		web.click(css_selector=".mdl-button.mdl-js-button.mdl-button--raised.mdl-js-ripple-effect.btnMarcar.mdl-button--colored", number = cont)
		print("YES :)")
		web.go_to('http://www.earpunifim.com/departamento/asistencia/alumno') 
