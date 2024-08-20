# folder , no. of files. count no. of files and no. of type of files. if zip then invalid.        

import os

def typeOfFile(folder):

    noOfFiles = 0
    typeofFiles = {}

    for file in os.listdir(folder):
        try:
            if not file.endswith(".zip"):
                noOfFiles += 1
                fileType = file.split(".")[-1]
                if fileType in typeofFiles:
                    typeofFiles[fileType] += 1
                else:
                    typeofFiles[fileType] = 1
            else:
                print(f"Inavlid file: {file}")
        except Exception as e:
            print(f"Error processing file {file}: {e}")

    return noOfFiles, typeofFiles


# tables

def writeTableToFile(number, fileName):
  with open(fileName, 'a') as file:
    file.write(f"\nTable of {number}:\n")
    for count in range(1, 11):
        result = number * count
        file.write(f"{number} x {count} = {result}\n")

number = int(input("Enter a number: "))
fileName = "Tables.txt"
writeTableToFile(number, fileName)


# cnic files (files are text files with first 4 digits being cnic)

import os
import csv

def processFiles(folder):
    data = {}
    invalidFiles = []

    for file in os.listdir(folder):
        try:
            cnic = file[:4]
            if not cnic.isdigit():
                continue

            if not file.endswith('.txt'):
                invalidFiles.append(file)
                continue

            if cnic not in data:
                data[cnic] = []
                filePath = os.path.join(folder, file)
                data[cnic].append(filePath)
        except Exception as e:
            print(f"Error processing file {file}: {e}")

    return data, invalidFiles

def createCsv(data, invalidFiles, outputFile):
    with open(outputFile, 'w', newline='') as csvfile:
        fieldnames = ['Cnic', 'File Paths', 'File Count', 'Valid']
        csvWriter = csv.writer(csvfile)
        csvWriter.writerow(fieldnames)

    for cnic, file_paths in data.items():
        csvWriter.writerow([cnic, ', '.join(file_paths), len(file_paths)])

    for file in invalidFiles:
        csvWriter.writerow([file[:4], file, 0, 'Invalid'])

directory = "your_directory_path"
outputFile = "output.csv"

data, invalidFiles = processFiles(directory)
createCsv(data, invalidFiles, outputFile)
