file=open('output.txt','w')
a=input("Enter text to write in the file: ")
file.write(a)
b=input("Enter text to append: ")
file.writelines(b)
print("Chnage in the current file made successfully")
file.close()

file=open('output.txt','r')
print(file.read())
file.close