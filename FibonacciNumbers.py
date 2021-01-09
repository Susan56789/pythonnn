n=eval(input("How many numbers should I print?"))

t1=0;
t2=1;


for i in range(n):
    print(t1);
			
    sum=t1+t2;
    t1=t2;
    t2=sum;
   
