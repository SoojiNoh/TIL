from PIL import Image

images_names = list(map(lambda x: str(x)+'.jpg', ["{0:03}".format(i) for i in range(1, 218)]))
images = list(map(lambda img: Image.open(img), images_names)) 
images = list(map(lambda img: img.convert('RGB'), images))

images[0].save('/Users/soojinoh/Documents/Documents_Sooji/SSAFY/TIL/algorithm/result.pdf',save_all=True, append_images=images)
