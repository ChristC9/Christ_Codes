fav_sports={"Ko Ko":"Football","Ma Ma":"Swimming","Mg Mg":"Tennis"}

fav_sports['Su Su']="Baseball"
print(fav_sports)

del fav_sports["Ko Ko"]
print(fav_sports)

fav_sports["Ma Ma"]="VolleyBall"
print(fav_sports)

print(fav_sports["Su Su"])
print(fav_sports["Mg Mg"])

for k,v in fav_sports.items():
    print(k,v,sep=',')

print(*fav_sports.items(),sep=',')

for kv in fav_sports.items():
    print(kv[0])