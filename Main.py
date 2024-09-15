from ReadList import read_allparts
from GetDirectory import get_directory
from DataCleanse import dataCleanse
from FolderCreation import folderCreation
from FileCompile import fileCompile
from FindParents import findParents
from ItemList import itemListCreator

def main():
    soNumber = input("SO Number (i.e. 20216): ")
    tankType = input("What type of package (Tank, Clamp, or UA): ")

    allPartsPath = get_directory()
    allPartsDrawing = input("File Name Containing All Parts List (i.e. PM-#####-TA): ")

    allPartsRawText = read_allparts(allPartsPath, allPartsDrawing)
    
    allPartsDictionaryUnsorted = dataCleanse(allPartsRawText)
    allPartsDictionary = {k: allPartsDictionaryUnsorted[k] for k in sorted(allPartsDictionaryUnsorted)}
    
    allPartsDictionaryWithParents = findParents(allPartsPath, allPartsDictionary, soNumber)

    ssFolderPath, ppFolderPath, newMainFolder = folderCreation(soNumber, tankType)

    fileCompile(allPartsPath, ssFolderPath, ppFolderPath, allPartsDictionaryWithParents, soNumber)

    itemListCreator(allPartsPath, allPartsDrawing, 'Steel Supplier Parts', newMainFolder, soNumber, 'SS')
    itemListCreator(allPartsPath, allPartsDrawing, 'Parts - SAP', newMainFolder, soNumber, 'PP')

main()