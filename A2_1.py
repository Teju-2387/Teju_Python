
import Airthematic

def main():
    print("enter number 1")
    v1=int(input())

    print("enter number 2")
    v2=int(input())


    ans=Airthematic.Multiplication(v1, v2)
    ans2=Airthematic.Sub(v1, v2)
    ans3=Airthematic.Div(v1, v2)
    ans4=Airthematic.Add(v1,v2)
    
    print("multiplication of two no", ans)
    print("Sub  of two no", ans2)
    print("Division of two no", ans3)
    print("Addition is:", ans4)

if __name__=="__main__":
    main()