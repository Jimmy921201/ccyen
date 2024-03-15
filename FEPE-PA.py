try:
   while True:
       n=int(input())
       if n==0:
           break
       xylist=[]
       for i in range(n):
           x,y=map(int,input().split())
           xylist.append(y) 
       xylist.sort()    
       if len(xylist)%2==1:
           ans1=(xylist[len(xylist)//2])
       else:
           ans1=(xylist[len(xylist)//2-1])
       ans=0
       for j in range(len(xylist)):
           ans+=abs((xylist[j])-ans1)
       print(ans1,ans)        
                 
       
       
          
except EOFError:
    pass                    
           
        
           