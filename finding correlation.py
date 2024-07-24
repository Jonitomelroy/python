import math
z=[]
sx=0
sx2=0
sy=0
sy2=0
sxy=0
n=int(input("enter the n value:"))
# creating the table
for i in range(0,n):
        ent_x=int(input("enter x value:"))
        ent_y=int(input("enter y value:"))
        col=[]
        x=ent_x
        y=ent_y
        x2=ent_x**2
        y2=ent_y**2
        xy=ent_x*ent_y
        col.extend((ent_x,ent_y,x2,y2,xy))
        sx+=x
        sx2+=x2
        sy+=y
        sy2+=y2
        sxy+=xy
        z.append(col)
col=[]
col.extend((sx,sy,sx2,sy2,sxy))
z.append(col)

for pr in z:
    print(pr)
    
#displaying the table
print("     "," x"," y"," x2","y2"," xy")
count=0
for pri in z:
    count+=1
    if count>n:
        k="total"
    else:
        k="     "
    print(k,pri)
print("")

#checking if it is a positive correlation or no correlation or negivite correlation
r1=(n*(sxy)-(sx)*(sy))
r2=math.sqrt((n*(sx2)-(sx**2))*(n*(sy2)-(sy**2)))
if (r1 or r2)==0:
    print("no correlation")
else:
    r3=r1/r2
    if r3>0:
     print ("positive correlation",r3)
    else:
        print ("negivite correlation",r3)
