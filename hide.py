from PIL import Image, ImageDraw 
from random import randint		

def embed_message():	
	
	keys = [] 							# Placeholder for keys
	img = Image.open('cat.jpg') 		# Initialise image object
	draw = ImageDraw.Draw(img)	   		# Initialise canvas
	width = img.size[0]  		   		# Width
	height = img.size[1]		   		# Height	
	pix = img.load()					# Our pixel array
	f = open('keys.txt','w')			# File where we are going to store our keys

	for elem in ([ord(elem) for elem in input("Secret message: ")]):
		key = (randint(1,width-10),randint(1,height-10))
		g, b = pix[key][1:3]
		draw.point(key, (elem,g , b))														
		f.write(str(key)+'\n')								
	
	print('Keys are saved to keys.txt file')
	img.save("secret.png", "PNG")
	f.close()
												
embed_message()