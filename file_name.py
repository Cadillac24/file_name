import os

path = os.getcwd() + "\\"

method = int(input('''Enter the name changing method:
1. order
2. random\n'''))

target_format = input("what file formats you want to change? ")
if (target_format[0] != "."):
    target_format = "." + target_format

all_file_formats = []

#check for all file formats
#check for dup names
#random -> numbers / letters
#orer -> letters

def changeName(og_name, name, format):
    # file_format = "." + og_name.split(".")[1]

    if (file_format == target_format):
        os.rename(path+og_name, path+name+file_format)
        print(og_name + " -> changed -> " + name+file_format)
    else:
        print(og_name + " skipped")



if (method == 1):
    first_number = int(input("enter the number you want to start from: "))
    name = first_number 
    file_format = ""

    for i in os.listdir(path):
        file_format = "." + i.split(".")[1]

        while (os.path.exists(path+str(name)+file_format)):
            print(str(name)+file_format + " already exists")
            name += 1

        changeName(i, str(name), file_format)

        name += 1
        
elif (method == 2):
    pass
else:
    print("Error!")