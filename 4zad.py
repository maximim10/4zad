from PIL import Image, ImageDraw
inp=input().split()
try:
    N1=int(inp[0])
except:
    N1=1
try:
    N2=int(inp[1])
except:
    N2=255
try:
    N=int(inp[2])
except:
    N=14
try:
    image_inp=inp[3]
except:
    image_inp="kachok.jpg"
try:
    image_out=inp[4]
except:
    image_out="out.jpg"
try:
    image=Image.open(image_inp)
except:
    print ("Net Faila")
else:
    draw=ImageDraw.Draw(image)
    pix=image.load()
    for i in range (image.size[0]):
        for j in range (image.size[1]):
            a=pix[i,j][0]
            b=pix[i,j][1]
            c=pix[i,j][2]
            if a+b+c>=N1 and a+b+c<=N2:
                draw.point((i,j),(N,N,N))
    image.save(image_out,"jpeg")

    image.show()
