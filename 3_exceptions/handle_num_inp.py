def main():
    x = get_int("what's x? ")
    print(f"x is {x}")

def get_int(prompt):
    # try if succeed -> do else block
    # if try-fail -> then do except block
    while True:
        # handle ValueError
        try:
            print()
            x = int(input(prompt))
        except ValueError:
            print("Invalid type for input please enter whole number.")
        else:
            return x

main()