from file_handle import read_file, write_file

# username = input("What's your name? ")
# write_file('names', 'txt', username)

content = read_file('names', 'txt')
print(content)