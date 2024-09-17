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
    
    gasket = False
    pressboard = False
    ssal = False
    StS = False

    if tankType == 'Tank' or tankType == 'tank':
        if input("Would you like a Gasket package (Issue # P5G)? (Y/N): ") in ['y', 'Y']:
            gasket = True
        if input("Would you like a Pressboard package (Issue # P8)? (Y/N): ") in ['y', 'Y']:
            pressboard = True
        if input("Would you like a Stainless/Aluminum package (Issue # P3 & P4AL)? (Y/N): ") in ['y', 'Y']:
            ssal = True
        if input("Would you like a Structural Steel package (Issue # P4 & P14)? (Y/N): ") in ['y', 'Y']:
            StS = True

    allPartsPath = get_directory()
    allPartsDrawing = input("File Name Containing All Parts List (i.e. PM-#####-TA): ")

    allPartsRawText = read_allparts(allPartsPath, allPartsDrawing)
    
    allPartsDictionaryUnsorted = dataCleanse(allPartsRawText)
    allPartsDictionary = {k: allPartsDictionaryUnsorted[k] for k in sorted(allPartsDictionaryUnsorted)}
    
    allPartsDictionaryWithParents = findParents(allPartsPath, allPartsDictionary, soNumber)

    ssFolderPath, newMainFolder = folderCreation(soNumber, tankType, 'SS')
    ppFolderPath, newMainFolder = folderCreation(soNumber, tankType, 'PP')

    fileCompile(allPartsPath, ssFolderPath, 's', allPartsDictionaryWithParents, soNumber)
    fileCompile(allPartsPath, ppFolderPath, 'p', allPartsDictionaryWithParents, soNumber)

    itemListCreator(allPartsPath, allPartsDrawing, 'Steel Supplier Parts', newMainFolder, soNumber, 'SS')
    itemListCreator(allPartsPath, allPartsDrawing, 'Parts - SAP', newMainFolder, soNumber, 'PP')

    if gasket:
        gaFolderPath, newMainFolder = folderCreation(soNumber, tankType, 'GA')
        fileCompile(allPartsPath, gaFolderPath, 'p5g', allPartsDictionaryWithParents, soNumber)
        itemListCreator(allPartsPath, allPartsDrawing, '(GASKETS)', newMainFolder, soNumber, 'GA')

    input("Success! Press any key to close window.")

main()