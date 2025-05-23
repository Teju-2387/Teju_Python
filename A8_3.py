import threading

def small():
    lower=0
    n=str(input("enter a string:"))
    for i in n:
      if(i.islower()):
          lower+=1
      return lower
    print("count is:", lower)

def capital():
    upper=0
    n=str(input("enter a string:"))
    for i in n:
      if(i.isupper()):
            upper+=1
      return upper
    print("count is:", upper)


def digit():
    dig=0
    n=str(input("enter a string:"))
    for i in n:
      if(i.isdigit()):
            dig+=1
      return dig
    print("count is:", dig)

def main():

    print("inside SMALL:")
    T1 = threading.Thread(target=small,args=())
    T1.start()

    print("CAPITAL:")
    T2 = threading.Thread(target=capital,args=())
    T2.start()
    
    print("DIGIT:")
    T3 = threading.Thread(target=digit,args=())
    T3.start()

if __name__=="__main__":
    main()
    