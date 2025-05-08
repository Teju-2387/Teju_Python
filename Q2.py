def Chknum(a):
    if a%2==0:
        print("even")
    else:
        print("odd")
    return a
def main():
    print("enter value")
    no=int(input())
    answer=Chknum(no)
if __name__=="__main__":
    main()


