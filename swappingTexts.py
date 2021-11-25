def swapFileData():
    file = input("Enter the first file: ")
    file2 = input("Enter the second file: ")

    with open('file.txt', 'r') as file:
        data_a = file.read()

    with open('file2.txt', 'r') as file2:
        data_b = file2.read()

    with open('file.txt', 'w') as a:
        a.write(data_b)

    with open('file2.txt', 'w') as b:
        b.write(data_a)

swapFileData()