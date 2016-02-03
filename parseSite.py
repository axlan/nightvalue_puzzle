from lxml import html
import sys
from unidecode import unidecode

print 'Parsing:', str(sys.argv[1])



with open(sys.argv[1], 'r') as myfile:
	data=myfile.read()

tree = html.fromstring(data)

#<meta property="og:description" content="
transcript = tree.xpath('//meta[@property="og:description"]/@content')


#h= HTMLParser.HTMLParser()
#transcript=h.unescape(transcript)

#<div id="footer-end"
#text = tree.xpath('//div[@id="footer-end"]/text()')

with open(sys.argv[2], 'w') as myfile:
	#myfile.write(transcript[0].encode('ascii', errors='backslashreplace'))
	myfile.write(unidecode(transcript[0]))