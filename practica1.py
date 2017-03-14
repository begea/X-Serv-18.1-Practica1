#!/usr/bin/python3

import webapp
import urllib.parse

class contentApp (webapp.webApp):

    formulario = '<form method="POST"> Pon una URL: <input type="text" name="contenido" value = "http://">' + \
                 '<input type=submit value=Enviar></form>'

    content = {'/': formulario,
               }

    diccionario1 = {}
    diccionario2 = {}
    secuencia = 0

    def parse(self, request):

            metodo = request.split(' ', 1)[0]
            recurso = request.split(' ', 2)[1]

            if metodo == "PUT":
                cuerpo = request.split('=')[-1]
            elif metodo == "POST":
                cuerpo = request.split('=')[-1]
            else:
                cuerpo = ""
            return (metodo, recurso, cuerpo)

    def process(self, peticion):

        (metodo, recurso, cuerpo) = peticion
        global htmlCode
        if metodo == "GET":
            if recurso in self.content:
                httpCode = "200 OK"
                htmlBody = "<html><body><h1>Acortador de URLs</h1>" + self.content[recurso] + "</body></html>"

                #for i in self.diccionario1:
                    #htmlBody = htmlBody + i + ": " + self.diccionario1[i] + "<br>"

            else:
                try:
                    recurso = recurso[1:]
                    numero = int(recurso[1:])
                    try:

                        httpCode = " 302 Found\nLocation: http://" + self.diccionario2[numero]
                        htmlBody = ""
                    except KeyError:
                        httpCode = "404 Not Found"
                        htmlBody = "<html><body>Recurso no disponible" + self.formulario + "</body></html>"
                except ValueError:
                        httpCode = "404 Not Found"
                        htmlBody = "<html><body>Recurso no disponible." + self.formulario + "</body></html>"


        elif metodo == "POST":

            if cuerpo == "":
                httpCode = "404"
                htmlBody = "<html><body>Not Found"+self.formulario+" </body></html>"
            else:
                if cuerpo in self.diccionario1:
                    httpCode = "200 OK"
                    htmlBody = "<html><body><a href= http://localhost:1235/" + str(self.diccionario1[cuerpo])+"> http://localhost:1235/" + str(self.diccionario1[cuerpo]) +"</a></body></html>"

                else:
                    self.secuencia = self.secuencia + 1
                    self.diccionario1[cuerpo] = self.secuencia
                    self.diccionario2[self.secuencia] = cuerpo
                    httpCode = "200 OK"
                    htmlBody = "<html><body><a href= http://localhost:1235/"+ str(self.diccionario1[cuerpo])+"> http://localhost:1235/"+ str(self.diccionario1[cuerpo])+ "</a></body></html>"

        else:
            httpCode = "405 Method Not Allowed"
            htmlBody = "No estas haciendo ni GET ni POST. Prueba otra vez."

        return (httpCode, htmlBody)


if __name__ == "__main__":
        testWebApp = contentApp("localhost", 1235)
