from PIL import Image
n = 1
folder = "badapple"

for k in range(1, 6572, 5):
    name = str(k)
    if k < 1000:
        if k < 100:
            if k < 10:
                 name = "000"+name
            else:
                 name = "00" + name
        else:
            name = "0"+name
    # i = Image.open(folder+"/ezgif-frame-"+name+".png")
    i = Image.open(folder+"/0"+name+".png")
    i = i.resize((128, 64), Image.NEAREST)
    thresh = 125
    fn = lambda x: 0 if x > thresh else 255
    i = i.convert('L').point(fn,mode='1')
    i.save(folder+"-pbm/"+str(n) + ".pbm")
    n += 1


