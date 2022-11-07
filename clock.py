h=int(input("hour="))
m=int(input("min="))
if 0<=h<=24 and 0<=m<60:
    if h>12:
        h-=12
    if m==0:
        f=60
    else:
        f=m
    a=h*30 #a being the angle that the hour hand covers, *30 is because an hour hand number to it's next hour hand number covers 30 degrees
    b=f*6 #b being the angle that the minute hand covers, *6 becasue a minute hand number to it's next minute hand number covers 6 degrees
    c=abs(b-a)
    d=m*(1/2) # *1/2 cause a minute hand to it's next minute hand covers half a degree
    e=abs(c-d)
    print("angle between the hands=",str(e)+" degrees")
else:
    print("niggah, that's invalid")
