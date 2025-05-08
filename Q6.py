def main():
    print("enter number")
    a=int(input())
    if a>0:
        print("No. is Positive", end= " ")
    elif a<0:
        print("No is Negative", end=" ")
    else:
        print("No is 0")
if __name__=="__main__":
    main()