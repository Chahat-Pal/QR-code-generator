import qrcode
url=input("enter any url here : ")
filename=input("enter file name you want to save it as : ")
if not(filename.endswith(".png")):
    filename = filename + ".png"
    
img = qrcode.make(url)
img.save(filename)
  