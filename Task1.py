# 1) Scenario 1: File does exist
# file1=open('sample.txt', 'r')
# print(file1.read())
# file1.close()

# 2) Scenario 2: File doesn't exist
try:
                file1=open('sample.txt', 'r')
                print(file1.read())
except:
        print("The file 'sample.txt' doesn't exist")