from PIL import Image, ImageFont,ImageDraw


def WordWrap(txt,wrapCount):
	wrapped=''
	words=txt.split()
	count=0
	for word in words:
		wrapped=wrapped+" "+word
		if count > 0 and count%wrapCount == 0:
			wrapped=wrapped+"\n"
		count=count+1
	return wrapped

def TextImage(txt,outfile):
	image = Image.new("RGBA", (800,400), (0,0,0))
	usr_font = ImageFont.truetype("BN-BlurryDay.ttf", 24)
	d_usr = ImageDraw.Draw(image)
	d_usr = d_usr.text((0,0), WordWrap(txt,10),(255,255,255), font=usr_font)

	image.save(outfile, "JPEG")

