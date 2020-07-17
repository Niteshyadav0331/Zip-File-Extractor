from zipfile import ZipFile 

file_name = input("Enter the name of file you want to file in .zip: ")

with ZipFile(file_name, 'r') as zip:
    zip.printdir()

    print('Extracting all the files...')
    zip.extractall()
    print("Done!")