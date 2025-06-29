def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def inputt():
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    return num1,num2

def main():
    while True:
        print("**********Calculator**********\n1. Addition(+)\n2. Subtraction(-)\n3. Multiplication(*)\n4. Division(/)\n5. Exit")
        choice = input("Choose an operation: ")

        if choice == '5':
            print("Exiting Calculator!\n")
            break

        if choice in ['1','2','3','4']:
            n1,n2 = inputt()
        
            if choice == '1':
                print(add(n1,n2))
        
            elif choice == '2':
                print(sub(n1,n2))
        
            elif choice == '3':
                print(mul(n1,n2))
        
            elif choice == '4':
                print(div(n1,n2))
        else:
            print("Invalid Choice! Try again!\n")

if __name__ == "__main__":
    main()
