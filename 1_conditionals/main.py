import random

def is_even(num):
    # return True if num % 2 == 0 else False
    return num % 2 == 0

print(is_even(10))
print(is_even(11))

# --------------------
def grade(score):
    if(score < 0 or score > 100):
        return
    
    if(score > 80):
        print("A")
    elif(score > 50):
        print("Yoll")
    else:
        print("Fail")


# --------------------
names = ['Wasin', 'Nine', 'Tor', 'Park', 'Aom', 'Prach']
choice = random.choice(names)

print(f'helo {choice} ', end='')
match choice:
    case 'Wasin' | 'Park' | 'Tor' | 'Nine':
        print("From KMITL")
    case 'Aom' | 'Prach':
        print("From KU")
    case _:
        # default
        pass

