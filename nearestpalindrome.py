num=int(input("Enter number:"));
while True:
    s=str(num);
    rev=s[::-1];
    if int(rev)==num:
        print(rev);
        break;
    num+=1;
