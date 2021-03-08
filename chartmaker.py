from PIL import Image, ImageDraw
from PIL import ImageFont
import requests
import math

def radchar(data:dict,size:tuple,textcolour):
    #setup
    radarchart=Image.new("RGBA",size)
    rw,rh=radarchart.size
    chart=Image.new("RGBA",(rw,rh))
    fnt = ImageFont.truetype("arial", rw//20)

    #math
    ox,oy=rw//2,rh//2
    coords=[(0,-1),(0.86, -0.5),(0.86,0.5),(0,1),(-0.86, 0.5),(-0.86,-0.5)]
    text_coords=[(fnt.size*-1.5,-fnt.size),(0,-fnt.size),(0,0),(fnt.size*-1.25,0),(fnt.size*-3,0),(fnt.size*-3,-fnt.size)]
    max_radius=rw//3
    level=max_radius//5

    #draws hexagons
    draw = ImageDraw.Draw(radarchart)
    draw2 = ImageDraw.Draw(chart)
    for radius in range(max_radius,0,-level+1):
        coords2=[(ox+(i[0]*radius),oy+(i[1]*radius)) for i in coords]
        draw.polygon(coords2, fill=(0,0,0,127), outline="white")

    #creates purple hexagon to display data
    display_coords=[]
    data={key:int(value) for key,value in data.items()}
    max_value=5#max(list(data.values()))
    #maps coordinates
    for key,value in data.items():
        index=list(data).index(key)
        v=int(max_radius*(value/max_value))
        display_coords.append((ox+(coords[index][0]*v),oy+(coords[index][1]*v)))
        pointx,pointy=(coords[index][0]*max_radius)+text_coords[index][0], (coords[index][1]*max_radius)+text_coords[index][1]
        #adds in labels for data
        draw.text((ox+pointx,oy+pointy), key.title(), font=fnt, fill=textcolour)

    #draws data hexagon
    draw2.polygon(display_coords, fill=(255,0,255,127), outline="red")
    radarchart.paste(chart, mask=chart)
    
    return radarchart

#radarchart.save("radarchart.png", "PNG", quality=70)

def make_chart(name:str,image_url:str,data:dict):
    #creates background image 
    main_img=Image.new("RGBA",(1080,1080),"lightgrey")
    draw = ImageDraw.Draw(main_img)

    draw.rectangle(((30, 30), (1050, 650)), outline="black",width=3, fill="white")

    #gets image of character from url
    dis_image=Image.open(requests.get(image_url, stream=True).raw)
    dis_image.putalpha(255)
    dis_image.thumbnail((1014, 614),Image.ANTIALIAS)

    #creates rader chart image from chartmaker.py
    radarchart=radchar(data,(1050//2,1080-660),"black")

    #sets where to place image of character
    dis_coords=((1080//2)-(dis_image.width//2),(683//2)-(dis_image.height//2))

    #puts image together
    main_img.paste(dis_image, dis_coords, mask=dis_image)
    main_img.paste(radarchart, (1050//4,660), mask=radarchart)

    #saves image
    #main_img.save(f"charts/{name}.png", "PNG", quality=70)
    return main_img