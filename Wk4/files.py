file = open("python.txt", "w")
name = str(input("Write your Name: "))
content = file.write("Hello, my name is "+ name )




try:
    value = str(input("Write the file name: "))               
    file = open(f"{value}.txt", "r")
    content = file.read()

    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    file.close()