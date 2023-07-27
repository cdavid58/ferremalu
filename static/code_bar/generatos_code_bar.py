import os, img2pdf
def Generador():
    try:
    	imagenes_jpg = [archivo for archivo in os.listdir('/home/ferremalu/') if archivo.endswith(".jpg")]
    	with open("/home/ferremalu/ferremalu/static/documento.pdf", "wb") as documento:
    		documento.write(img2pdf.convert(imagenes_jpg))
    	for i in imagenes_jpg:
    		os.remove(os.remove('/home/ferremalu/'+i))
    	return True
    except Exception as e:
        return str(e)


