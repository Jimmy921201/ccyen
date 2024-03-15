li=[1,2,3,4,5,6,7,8,9]
li=sorted(li,key=lambda x:-x)
print(li)
li2=[('app',15,12),('opp',15,49),('tpp',0,49),('tcp',0,12)]
li2=sorted(li2,key=lambda x:(x[1],x[2]))
print(li2)