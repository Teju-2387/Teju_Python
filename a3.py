def main():
    return vote
def vote(age):
    
    if age>=18:
        print("Elgibile to vote:", end= " ")
        return True
    else:
        print("Not Eligible for  vote:", end= " ")
        return False

a=int(input("enter the age: "))
result=vote(a)

if __name__=="__main__":
    main()