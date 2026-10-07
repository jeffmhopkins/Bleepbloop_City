"""Draw the storage hall item-flow diagram (assets/storage-hall-flow.png).

Schematic of Jeffrey's hall layout (plans/storage-layout.md): shulker unloader at
the center of Machinery feeding the router below it, dump barrels to the right,
smelter loop on the left, U-shaped under-floor item stream, potion line to the
golem gallery. Each wing is a hallway with a chest wall on both sides,
each backed by its own service gap. Not to scale. Needs Pillow and the DejaVu fonts.
Run: python3 tools/storage_hall_flow.py
"""
from PIL import Image, ImageDraw, ImageFont
import math, os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','assets','storage-hall-flow.png')
S=2; W,H=1600,1180
im=Image.new('RGB',(W*S,H*S),(250,250,247)); d=ImageDraw.Draw(im)
def f(sz,b=True): return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if b else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',int(sz*S))
def rect(x0,y0,x1,y1,fill,ol=(30,30,30),w=2): d.rectangle([x0*S,y0*S,x1*S,y1*S],fill=fill,outline=ol,width=int(w*S))
def text(x,y,t,sz=16,b=True,c=(20,20,20)): d.text((x*S,y*S),t,font=f(sz,b),fill=c,anchor='mm')
def line(pts,c,w=4,dash=None):
    if not dash: d.line([(x*S,y*S) for x,y in pts],fill=c,width=int(w*S),joint='curve'); return
    for (x0,y0),(x1,y1) in zip(pts,pts[1:]):
        L=math.hypot(x1-x0,y1-y0); n=int(L//dash)
        for i in range(0,n,2):
            a=i/n; b=min((i+1)/n,1); d.line([((x0+(x1-x0)*a)*S,(y0+(y1-y0)*a)*S),((x0+(x1-x0)*b)*S,(y0+(y1-y0)*b)*S)],fill=c,width=int(w*S))
def head(x0,y0,x1,y1,c,s=12):
    a=math.atan2(y1-y0,x1-x0)
    p=[(x1,y1),(x1-s*math.cos(a-0.45),y1-s*math.sin(a-0.45)),(x1-s*math.cos(a+0.45),y1-s*math.sin(a+0.45))]
    d.polygon([(x*S,y*S) for x,y in p],fill=c)
def arrow(pts,c,w=4,dash=None,mid=False):
    line(pts,c,w,dash); (x0,y0),(x1,y1)=pts[-2],pts[-1]; head(x0,y0,x1,y1,c)
ORANGE=(235,120,0); GREEN=(20,140,70); RED=(200,30,30); GREY=(90,90,90)
text(W/2,32,'Storage hall: item flow and final wing contents (schematic, not to scale)',24)
# machinery band
MY0,MY1=70,250
rect(80,MY0,1520,MY1,(205,214,245))
text(250,86,'MACHINERY (back section)',15,c=(30,50,140))
def box(x0,x1,t,sub=None,fill=(255,255,255),y0=110,y1=200):
    rect(x0,y0,x1,y1,fill); m=(y0+y1)/2
    text((x0+x1)/2,m-10 if sub else m,t,15)
    if sub: text((x0+x1)/2,m+13,sub,12,False)
box(110,330,'Auto smelter','furnaces, smokers, blast',fill=(255,235,215))
box(705,895,'Shulker unloader','center of back',fill=(235,220,250),y0=98,y1=148)
box(705,895,'ROUTER','splits items',fill=(255,225,170),y0=172,y1=228)
box(935,1095,'Input','dump barrels',fill=(230,245,255))
box(1120,1250,'Intake','unstackables',fill=(240,240,240))
box(1290,1400,'Overflow','end of stream',fill=(240,240,240))
box(1420,1505,'Lava','junk only',fill=(255,200,180))
arrow([(800,148),(800,172)],ORANGE)
arrow([(935,200),(895,200)],ORANGE)
arrow([(705,186),(330,186)],RED,3); text(515,176,'raw ore / raw food',11,False,RED)
arrow([(330,214),(705,214)],RED,3); text(515,226,'ingots / cooked food back',11,False,RED)
text(515,130,'room for more machines',13,False,GREY)
# wings
LX0,LX1,AX0,AX1,RX0,RX1=80,680,680,920,920,1520
# (y0, y1, wing + build stage, final groups, DC-eq and growth room, colour)
bands=[(250,450,'Back-left · Stage 5','Decorative (colors & finishes) · Nether · End','18.5 DC-eq + 3.5 growth room',(140,60,155)),
       (450,650,'Mid-left · Stage 3','Ores & metals · Copper · Redstone','16 DC-eq + 6 growth room',(210,20,45)),
       (650,850,'Front-left · Stage 1','Stone family','17 DC-eq + 5 growth room',(20,150,60))]
right_bands=[(250,450,'Back-right · Stage 5','Mob drops · Tools, armor & enchanting · Transport','16 DC-eq + 6 growth room',(140,60,155)),
       (450,650,'Mid-right · Stage 3','Wood family · Decorative (build blocks)','17.5 DC-eq + 4.5 growth room',(210,20,45)),
       (650,850,'Front-right · Stage 2','Farming & food · Brewing (Dome end)','18 DC-eq + 4 growth room',(240,170,0))]
def tint(c,a=0.78): return tuple(int(v+(255-v)*a) for v in c)
def band(x0,x1,y0,y1,label,sub,cap,col,side):
    rect(x0,y0,x1,y1,tint(col))
    rect(x0,y0,x1,y0+36,(70,70,75)); rect(x0,y1-36,x1,y1,(70,70,75))
    text((x0+x1)/2,y0+9,'service gap + hopper filters',9,False,(220,220,220))
    text((x0+x1)/2,y1-9,'service gap + hopper filters',9,False,(220,220,220))
    n=int((x1-x0-30)//30)
    for cy0 in (y0+39,y1-63):
        for i in range(n):
            cx=x0+18+i*30; rect(cx,cy0,cx+24,cy0+24,(170,110,50),(80,50,20),1.5)
    rect(x0,y0,x1,y1,None,(30,30,30),2.5)
    text((x0+x1)/2,y0+80,label,19,c=col if sum(col)<500 else (130,90,0))
    text((x0+x1)/2,y0+104,sub,13,True,(40,40,40))
    text((x0+x1)/2,y0+122,cap,11,False,(70,70,70))
    ya,yb=y0+22,y1-22
    if side=='L':
        tx,ex=AX0+20,x0+10
    else:
        tx,ex=AX1-20,x1-10
    arrow([(tx,ya),(ex,ya)],ORANGE,3); line([(ex,ya),(ex,yb)],ORANGE,3,dash=6); arrow([(ex,yb),(tx,yb)],ORANGE,3)
for y0,y1,l,s,k,c in bands: band(LX0,LX1,y0,y1,l,s,k,c,'L')
for y0,y1,l,s,k,c in right_bands: band(RX0,RX1,y0,y1,l,s,k,c,'R')
# aisle
rect(AX0,250,AX1,850,(236,236,230))
text(800,560,'CENTRAL',14,c=GREY); text(800,580,'AISLE',14,c=GREY)
# trunk U: router down left, across under dome, up right to overflow
arrow([(760,228),(760,250)],ORANGE)
line([(760,250),(700,250),(700,860)],ORANGE,5)
line([(900,860),(900,240)],ORANGE,5)
arrow([(900,240),(1345,240),(1345,200)],ORANGE,5)
for y in (420,620,820): head(700,y-20,700,y,ORANGE,13)
for y in (640,440,300): head(900,y+20,900,y,ORANGE,13)
arrow([(1400,155),(1420,155)],GREY,3)
# golem line
arrow([(830,228),(830,250),(830,712)],GREEN,3,dash=8)
text(842,690,'',1)
# dome
cx,cy,r=800,860,150
d.ellipse([(cx-r)*S,(cy-r)*S,(cx+r)*S,(cy+r)*S],fill=(205,225,240),outline=(30,30,30),width=3*S)
text(cx,cy-72,'DOME',20,c=(20,40,70))
text(cx,cy-48,'Stage 4: golem gallery',13,False,(20,40,70))
line([(700,860),(900,860)],ORANGE,5,dash=10)
arrow([(830,712),(830,742),(812,742)],GREEN,3,dash=6)

# copper input chest + display chests ring
rect(786,728,812,754,(200,120,70),(90,50,20),1.5); text(760,741,'copper chest',10,False)
for k in range(9):
    a=math.radians(200+k*(140/8)); x=cx+105*math.cos(a); y=cy+105*math.sin(a)*-1
for k in range(9):
    a=math.radians(160-k*(140/8)); x=cx+108*math.cos(a); y=cy-108*math.sin(a)*-1
for k in range(9):
    a=math.radians(30+k*(120/8)); x=cx+112*math.cos(a); y=cy+112*math.sin(a)
    rect(x-11,y-11,x+11,y+11,(170,110,50),(80,50,20),1.2)
text(cx,cy+30,'display chests (sealed with glass)',11,False,(20,40,70))
text(842,330,'potions',11,False,GREEN)
text(W/2,1035,'FRONT / ENTRANCE',16,c=GREY)
# legend
ly=1080
def leg(x,c,t,dash=None):
    arrow([(x,ly),(x+50,ly)],c,4,dash); text(x+60,ly,'',1); d.text(((x+60)*S,ly*S),t,font=f(13,False),fill=(30,30,30),anchor='lm')
leg(90,ORANGE,'Main item stream (under floor; dashed = crosses under dome)')
leg(640,RED,'Smelter loop')
leg(830,GREEN,'Potion line to golem gallery',dash=8)
d.text((90*S,1120*S),'Each wing is a hallway with chest walls on both sides; its branch runs out behind one wall and back behind the other. Unsorted items continue along the stream; anything left ends in Overflow, and only junk goes to Lava.',font=f(12,False),fill=(60,60,60),anchor='lm')
d.text((90*S,1145*S),'Gallery overflow goes to the main Overflow, never back to the Router. Stage = the order each wing is built; contents = the finished hall.',font=f(12,False),fill=(60,60,60),anchor='lm')
im.resize((W,H),Image.LANCZOS).save(OUT)
