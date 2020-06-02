#!/usr/bin/python3
from webbot import Browser
web = Browser()
web.go_to('http://www.earpunifim.com/')
web.type("YOUR_CODE", into="Usuario UNI")
web.type("YOUR_PASSWORD", into="Password")
web.press(web.Key.ENTER)
web.click("Mi Asistencia", id="asistencia_alumno_utfim")
cont = 1
while cont < 10:
    if web.exists(css_selector=".mdl-button.mdl-js-button.mdl-button--raised.mdl-js-ripple-effect.btnMarcar.mdl-button--colored"):
        web.click(css_selector=".mdl-button.mdl-js-button.mdl-button--raised.mdl-js-ripple-effect.btnMarcar.mdl-button--colored", number = cont)
        print("YES :)")
        web.go_to('http://www.earpunifim.com/departamento/asistencia/alumno') 
        cont += 1
web.quit()
