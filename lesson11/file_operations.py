


# file_path = "example.txt"
# print(content)
#
# file.close()


import os


with open('example.txt', 'w') as file:
    file.write('Hello World!')

lines = ['Hello world!\n', 'Wlcome to python!\n']
with open('example.txt', 'w') as file:
    file.writelines(lines)

with open('example.txt', 'r')as file:
    file.seek(0)
    data = file.read()
    print(data)

if os.path.exists('example.txt'):
    print('File exists')

with open('example.txt', "a") as file:
    file.write('New data appended')

data = b"This is some binary data"
with open('example.bin', "wb") as file:
    file.write(data)

with open('example.bin', "rb") as binary_file:
    data = binary_file.read()