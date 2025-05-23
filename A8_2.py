import threading

def evenfactor(i, n):
      sum=0
      for i in range(1,11):
        
        if i%2==0:
            sum=sum+i
      print("even numbers sum is:", sum)

def oddfactor(i, n):
    sum=0
    for i in range(1,11):
         
         if i%2!=0:
            sum=sum+i
    print("odd numbers sum is:", sum)

def main():
  print("Inside evenfactor:")
  T1 = threading.Thread(target=evenfactor,args=(1,11))
  T1.start()

  print("Inside ODDFactor Thread:")
  T2 = threading.Thread(target=oddfactor, args=(1,11))
  T2.start()

if __name__=="__main__":
    main()

