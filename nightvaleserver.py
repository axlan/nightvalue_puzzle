#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import re
import os.path
import markovgen
import textimage


magic_words = '(angel)|(mountain)|(wheat)|(computer)'
PORT_NUMBER = 8080

file_ = open('combined')
markov = markovgen.Markov(file_)

triggered = False
triggerTxt = ''

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET2(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write("Hello World !")
		return

	def do_GET(self):
		if triggered:
			re.sub(magic_words,triggerTxt,'[*****]')

			return


		word =  self.path[1:]
		m = re.search('[^a-zA-z]', word)
		if m is not None:
			with open('Access Denied 590x332.jpg', 'rb') as f:
				self.send_response(200)
				self.send_header('Content-type', 'image/jpg')
				self.end_headers()
				self.wfile.write(f.read())
				return

		imagePath = 'out/'+word+'.jpg'
		if not os.path.isfile(imagePath):
			txt = markov.generate_markov_text(100,word)
			textimage.TextImage(txt,imagePath)

		with open(imagePath, 'rb') as f:

			m = re.search(magic_words, txt.lower())
			if m is not None:
				triggered = True
				triggerTxt = txt
				self.send_response(201)
			else:
				self.send_response(200)

			self.send_header('Content-type', 'image/jpg')
			self.end_headers()
			self.wfile.write(f.read())



			return


		#import re
		#m = re.search('(?<=abc)def', 'abcdef')
		#m.group(0)


try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()