#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import re
import os.path
import markovgen
import textimage
from os import curdir, sep


PORT_NUMBER = 1331


class ServerState:
	magic_words = '(angel)|(mountain)|(wheat)|(computer)|(Angel)|(Mountain)|(Wheat)|(Computer)'
	file_ = open('combined')
	markov = markovgen.Markov(file_)
	triggered = False
	triggerWord = ''
	triggerTxt = ''

state = ServerState()


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
		try:

			staticType = False
			if len(self.path) < 2 or self.path.endswith(".html"):
				self.path = '/index.html'
				mimetype='text/html'
				staticType = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				staticType = True
			if self.path.endswith(".png"):
				mimetype='image/png'
				staticType = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				staticType = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				staticType = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				staticType = True
			if staticType:
				#Open the static file requested and send it
				f = open(curdir + sep + self.path) 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
				return


			word =  self.path[1:]
			offset=word.find('?')
			if not offset == -1:
				word = word[:offset]
			m = re.search(state.magic_words, word)
			if m is not None:
				with open('map2.png', 'rb') as f:
					self.send_response(200)
					self.send_header('Content-type', 'image/png')
					self.end_headers()
					self.wfile.write(f.read())
					return

			if state.triggered:
				state.triggered = False
				print 'untriggered'
				imagePath = 'out/redact_'+state.triggerWord+'.png'
				#if not os.path.isfile(imagePath):
				newTxt = re.sub(state.magic_words,'[*****]',state.triggerTxt)
				newTxt='DISREGARD PREVIOUS RESULTS. CORRECTION: . . . . . . .\n'+newTxt
				textimage.TextImage(newTxt,imagePath)
				with open(imagePath, 'rb') as f:
					self.send_response(200)
					self.send_header('Content-type', 'image/png')
					self.end_headers()
					self.wfile.write(f.read())
					return

			m = re.search('[^a-zA-z]', word)
			if m is not None:
				with open('Access Denied 590x332.jpg', 'rb') as f:
					self.send_response(200)
					self.send_header('Content-type', 'image/jpg')
					self.end_headers()
					self.wfile.write(f.read())
					return

			imagePath = 'out/'+word+'.png'
			#if not os.path.isfile(imagePath):
			txt = state.markov.generate_markov_text(100,word)
			textimage.TextImage(txt,imagePath)

			with open(imagePath, 'rb') as f:

				m = re.search(state.magic_words, txt)
				if m is not None:
					print 'triggered'
					state.triggered = True
					state.triggerTxt = txt
					state.triggerWord = word
					self.send_response(201)
				else:
					self.send_response(200)

				self.send_header('Content-type', 'image/png')
				self.end_headers()
				self.wfile.write(f.read())
				return
		except IOError:
			raise
			self.send_error(404,'File Not Found: %s' % self.path)


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