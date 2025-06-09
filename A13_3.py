class Number:

    def __init__(self, No):
        self.No=No
       
    def CheckPrime(self):
         if self.No<1:
             return False
         i=2
         while i <= self.No:
            if self.No % i == 0:
                return False
            i=i+1
            return True            
    
    def ChkPerfect(self,sum):
        sum=0
        for i in range(1, self.No):
            if self.No%i==0:
                sum=sum+i
        return sum==self.No
    
    def Factors(self):
        for i in range(1, self.No+1):
            if self.No%i==0:
                print("Factors are:",i)

    def SumofFactors(self):
        sum=0
        for i in range(1, self.No+1):
            if self.No%i==0:
                sum=sum+i
        print("Sum of Factors are:", sum)


def main():

    N=int(input("enter the Number:"))

    N1=Number(N)
    N2=Number(N)
    N3=Number(N)
    N4=Number(N)

    if N1.CheckPrime():
        print("Number is Prime:")
    else:
        print("Number is Not a Prime:")

    if N2.ChkPerfect(sum):
        print("Number is Perfect:")
    else:
        print("Number is Not a Perfect:")

    N3.Factors()

    N4.SumofFactors()




if __name__=="__main__":
    main()