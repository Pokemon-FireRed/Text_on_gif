from PIL import Image, ImageDraw, ImageSequence, ImageFont
import io,sys,os
import glob

path = str(sys.argv[1])
text = str(sys.argv[2])
speed = int(sys.argv[3])
im = Image.open(path)

font = ImageFont.truetype("impact.ttf",26)
  
i = 0
pathnogif = path.replace(".gif","")
try:
    while 1:
        #im.putpalette(mypalette)
        new_im = Image.new("RGBA", im.size)
        new_im.paste(im)
        d = ImageDraw.Draw(new_im)
        d.text((10,10), text,fill=(255,255,255),align='center',font=font)
        new_im.save(pathnogif+"_"+str(i)+'.png')

        i += 1
        im.seek(im.tell() + 1)
except EOFError:
        pass

fp_in = pathnogif + "_*.png"
print(fp_in)
mypalette = im.getpalette()
imgs = (Image.open(f) for f in sorted(glob.glob(fp_in)))
img = next(imgs)  # extract first image from iterator
img.save(fp=pathnogif+"_mod.gif", format='GIF', append_images=imgs,
         save_all=True, duration=speed, loop=0, transparency=0, disposal=2)

for nbr in range(i):
    os.remove(pathnogif+'_'+str(nbr)+'.png')