# name = input("What's your name? ")
# print("Hello,", name)

# a = 1.1
# b = 2.2
# z = a + b
# print(round(z))
# x = 10000.31
# print(f'{x:,.2f}')

# num = 2/3
# print(round(num, 20))

def main():
    triangle(5)
    print(gen(5))

def triangle(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end='')
        print("\n")

def gen(n):
    # return None
    return 

main()