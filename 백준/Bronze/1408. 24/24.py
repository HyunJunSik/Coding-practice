t1,t2=0,0
for i,j in zip(map(int,input().split(":")),map(int,input().split(":"))):
    t1=t1*60+i
    t2=t2*60+j
t2=t2-t1 if t2>t1 else t2-t1+24*3600
print("%02d:%02d:%02d"%(t2//3600,t2//60%60,t2%60))