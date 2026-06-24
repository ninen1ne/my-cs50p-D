def main():
    print_square(5)

def print_row(width):
    # print("?" * width)
    for _ in range(width):
        print("?", end="")

def print_col(height):
    # print("*\n" * height)
    for _ in range(height):
        print("*")

def print_square(size):
    for _ in range(size):
        print_row(size)
        print()

# extract problems into function each responsible
# for only one thing and we can abstraction it implementation
# in main we don't care how each func implement :D
main()