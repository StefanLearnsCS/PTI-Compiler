from ReadList import read_allparts
from GetDirectory import get_directory

def main():
    allPartsPath = get_directory()
    allPartsDrawing = input("File Name Containing All Parts List (i.e. PM-#####-TA): ")

    print(read_allparts(allPartsPath, allPartsDrawing))

main()