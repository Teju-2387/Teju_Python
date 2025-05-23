import threading


def even(i, n):
     for i in range(1,11):
        if i%2==0:
           print("even numbers:", i)

def odd(i, n):
     for i in range(1,11):
        if i%2!=0:
           print("odd numbers:", i)

def main():
  print("Inside even")
  T1 = threading.Thread(target=even,args=(1,11))
  T1.start()
  print("Inside ODD Thread")
  T2 = threading.Thread(target=odd, args=(1,11))
  T2.start()

   

if __name__=="__main__":
 main()

