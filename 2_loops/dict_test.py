a = {
    1: "one",
    2: "two"
}

print(a[1])

friends = {
    'Nine': 'MAN',
    'Tor': 'MAN',
    'Kate': 'WOMAN',
    'Park': 'MAN'
}

print(friends['Park'])

for key, value in friends.items():
    print(f'{key} -> {value}')

# -------------------
print()
students = [
    {'name': 'Nine', 'age': '20', 'gender': 'man'},
    {'name': 'Macaurin', 'age': '8', 'gender': 'woman'},
    {'name': 'John', 'age': '60', 'gender': 'man'},
]

for std in students:
    print(f'{std['name']}, {std['age']}, {std['gender']}')