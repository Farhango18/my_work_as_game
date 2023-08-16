import random
a=random.randint(1,10000)
s=0
print("be bazi hadse adad khosh amadid")
while True:
    b=int(input("ye adad vared konid:"))
    if a==b:
        print("afrin shoma dorost hads zadid")
        print("teadad khatahaye shoma=",s)
        break
    else:
        try:
            if b<0:
                print("lodfan yek adad mosbat vred konid")
                s+=1
                continue
            elif b>10000:
                print("lodfan adadi bein 10000ta 1 ro entekhab konid")
                s+=1
                continue
            elif b<a:
                print("na adad mored nazare man bozorg tare")
                s+=1
                continue
            else:
                print("na adad mored nazar man kochek tare")
                s+=1
                continue
        except:
            print("lodfan yek adad vared konid")
            s+=1
