#!/usr/bin/python
# -*- coding: utf-8 -*

import webapp

class contentApp (webapp.webApp):

    formulario = '<form method="POST"> Pon una URL: <input type="text" name="contenido" value = "http://">' + \
                 '<input type=submit value=Enviar></form> URLs a poder introducir: "http://github.com"' + \
                 '\r\n\r\n"http://gsyc.es"\r\n\r\n"http:/aulavirtual.urjc.es"\r\n\r\ny\r\n\r\n"http://urjc.es"'

    url1='Pincha sobre la URL <a href="http://www.github.com" target="_blank">http://www.github.com</a>'
    url2='Pincha sobre la URL <a href="http://www.gsyc.es" target="_blank">http://www.gsyc.es</a>'
    url3='Pincha sobre la URL <a href="http://www.urjc.es" target="_blank">http://www.urjc.es</a>'
    url4='Pincha sobre la URL <a href="http://www.aulavirtual.urjc.es" target="_blank">http://www.aulavirtual.urjc.es</a>'
    content1 = {'/':formulario,
               '/1': url1,
               '/2': url2,
               '/3': url3,
               '/4': url4
               }

    content2 = {'/http://github.com': 'http://github.com --------> localhost:1235/1',
               '/http://gsyc.es': 'http://gsyc.es --------> localhost:1235/2',
               '/http://urjc.es': 'http://urjc.es --------> localhost:1235/3',
               '/http://aulavirtual.urjc.es': 'http://aulavirtual.urjc.es --------> localhost:1235/4'
               }

    def parse(self, request):

        metodo = request.split(' ', 2)[0]
        recurso = request.split(' ', 2)[1]
        cuerpo = request.split('\r\n\r\n', 1)[1]
        return metodo, recurso, cuerpo

    def process(self, peticion):

        (metodo, recurso, cuerpo) = peticion
        global htmlCode
        if metodo == "GET":
            if recurso in self.content1:
                httpCode = "200 OK"
                htmlBody = "<html><body>" + self.content1[recurso]

            else:
                httpCode = "404 Not Found"
                htmlBody = "No estas pidiendo el recurso correctamente. Prueba otra vez."

        elif metodo == "POST":
            self.content1[recurso] = cuerpo.split('=')[1]
            if recurso in self.content2:
                httpCode = "200 OK"
                htmlBody = "<html><body>" + self.content2[recurso]
            else:
                httpCode = "200 OK"
                htmlBody = "No estas pidiendo una de las URLs de la lista."
        else:
            httpCode = "405 Method Not Allowed"
            htmlBody = "No estas haciendo ni GET ni POST. Prueba otra vez."

        return (httpCode, htmlBody)


if __name__ == "__main__":
        testWebApp = contentApp("localhost", 1235)
