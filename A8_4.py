import threading

def no(i, n):
     for i in range(1,51):
        print(i)

def rev(i,n,j):
     for i in range(50,0,-1):
        print(i)

def main():
  print("Inside no")
  T1 = threading.Thread(target=no,args=(1,51))
  T1.start()


  print("Inside rev no")
  T2 = threading.Thread(target=rev, args=(50,0,-1))
  T2.start()

if __name__=="__main__":
 main()

