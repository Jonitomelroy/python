import math
x=[]
y=[]
sx=0
sx2=0
sy=0
sy2=0
sxy=0
n=int(input("enter the n value:"))
# creating the table
for i in range(1,n+1):
        ent_x=int(input(f"enter x{i} value:"))
        ent_y=int(input(f"enter y{i} value:"))
        col=[]
        x.append(ent_x)
        y.append(ent_y)
        sx+=ent_x
        sy+=ent_y
        sx2+=ent_x**2
        sy2+=ent_y**2
        sxy+=ent_x*ent_y

print("the entered values of x and y","\n")
print("x",x)
print("y",y,"\n")

#checking if it is a positive correlation or no correlation or negivite correlation
r1=(n*(sxy)-(sx)*(sy))
r2=math.sqrt((n*(sx2)-(sx**2))*(n*(sy2)-(sy**2)))
if (r1 or r2)==0:
    print("The correlation coefficient is 0 and no correlation")
else:
    r3=r1/r2
    if r3>0:
     print ("the correlation coefficient is",r3,"\n","and it is a positive correlation")
    else:
        print ("the correlation coefficient is",r3,"\n","and it is anegivite correlation")


        

