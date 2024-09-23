from ReadList import read_allparts
from GetDirectory import get_directory
from DataCleanse import dataCleanse
from FolderCreation import folderCreation
from FileCompile import fileCompile
from FindParents import findParents
from ItemList import itemListCreator
from NotPacked import notPacked
from InsulationHelper import uaCombined, read_insulation, inpDataCleanse, inpAssyListCreator, inpCombined, inpAssyDataCleanse, read_assyInsulation, inpAssyCompile

def main():
    soNumber = input("SO Number (i.e. 20216): ")
    tankType = input("What type of package (Tank, Clamp, or UA): ")
    
    gasket = False
    pressboard = False
    ssal = False
    StS = False
    tx2 = False
    cubars = False
    cccSteel = True
    insul = True

    if tankType.lower() == 'tank':
        if input("Would you like a Gasket package (Issue # P5G)? (Y/N): ") in ['y', 'Y']:
            gasket = True
        if input("Would you like a Pressboard package (Issue # P8)? (Y/N): ") in ['y', 'Y']:
            pressboard = True
        if input("Would you like a Stainless/Aluminum package (Issue # P3 & P4AL)? (Y/N): ") in ['y', 'Y']:
            ssal = True
        if input("Would you like a Structural Steel package (Issue # P4 & P14)? (Y/N): ") in ['y', 'Y']:
            StS = True

    #if tankType.lower() == 'clamp':
        #if input("Would you like a CCC Assembly Steel Supplier package (Issue # S)? (Y/N): ") in ['y', 'Y']:
        #   cccSteel = True
        #if input("Would you like a INP-CLM-CCC Insulation package (Issue # P)? (Y/N): ") in ['y', 'Y']:
        #    insul = True
    
    if tankType.lower() == 'ua':
        if input("Would you like a TX2 package (Issue # P8)? (Y/N): ") in ['y', 'Y']:
            tx2 = True
        if input("Would you like a CU Bars package (Issue # P4Cu)? (Y/N): ") in ['y', 'Y']:
            cubars = True
    
    if tankType.lower() != 'clamp':
        allPartsDrawing = input("File Name Containing All Parts List (i.e. SM-21043-TA or UA-21043): ")
    else:
        allPartsDrawing = input("File Name of CLM-CCC Drawing Containing All Parts List (i.e. CLM-CCC-21043): ")
        inpDrawing = input("File Name of INP-CLM-CCC Drawing Containing Purchased Parts List (i.e. INP-CLM-CCC-21043): ")

    allPartsPath = get_directory()

    allPartsRawText = read_allparts(allPartsPath, allPartsDrawing)
    
    allPartsDictionaryUnsorted = dataCleanse(allPartsRawText)
    allPartsDictionary = {k: allPartsDictionaryUnsorted[k] for k in sorted(allPartsDictionaryUnsorted)}
    
    allPartsDictionaryWithParents = findParents(allPartsPath, allPartsDictionary, soNumber)

    if tankType.lower() == 'tank':
        ssFolderPath, newMainFolder = folderCreation(soNumber, tankType, 'SS')
        ppFolderPath, newMainFolder = folderCreation(soNumber, tankType, 'PP')

        itemListCreator(allPartsPath, allPartsDrawing, 'Steel Supplier Parts', newMainFolder, soNumber, 'SS', tankType)
        itemListCreator(allPartsPath, allPartsDrawing, 'Parts - SAP', newMainFolder, soNumber, 'PP', tankType)

        if gasket:
            gaFolderPath, newMainFolder = folderCreation(soNumber, tankType, 'GA')
            allPartsDictionaryWithParents = fileCompile(allPartsPath, gaFolderPath, 'p5g', allPartsDictionaryWithParents, soNumber)
            itemListCreator(allPartsPath, allPartsDrawing, '(GASKETS)', newMainFolder, soNumber, 'GA', tankType)
        if pressboard:
            pbFolderPath, newMainFolder = folderCreation(soNumber, tankType, 'PB')
            allPartsDictionaryWithParents = fileCompile(allPartsPath, pbFolderPath, 'p8', allPartsDictionaryWithParents, soNumber)
            itemListCreator(allPartsPath, allPartsDrawing, '(TX2)', newMainFolder, soNumber, 'PB', tankType)
        if ssal:
            ssalFolderPath, newMainFolder = folderCreation(soNumber, tankType, 'SSAL')
            allPartsDictionaryWithParents = fileCompile(allPartsPath, ssalFolderPath, 'p3', allPartsDictionaryWithParents, soNumber)
            allPartsDictionaryWithParents = fileCompile(allPartsPath, ssalFolderPath, 'p4al', allPartsDictionaryWithParents, soNumber)
            itemListCreator(allPartsPath, allPartsDrawing, '& Aluminum)', newMainFolder, soNumber, 'SSAL', tankType)
        if StS:
            stsFolderPath, newMainFolder = folderCreation(soNumber, tankType, 'StS')
            allPartsDictionaryWithParents = fileCompile(allPartsPath, stsFolderPath, 'p4', allPartsDictionaryWithParents, soNumber)
            allPartsDictionaryWithParents = fileCompile(allPartsPath, stsFolderPath, 'p14', allPartsDictionaryWithParents, soNumber)
            itemListCreator(allPartsPath, allPartsDrawing, '(StS)', newMainFolder, soNumber, 'StS', tankType)

        allPartsDictionaryWithParents = fileCompile(allPartsPath, ssFolderPath, 's', allPartsDictionaryWithParents, soNumber)
        allPartsDictionaryWithParents = fileCompile(allPartsPath, ppFolderPath, 'p', allPartsDictionaryWithParents, soNumber)
        notPacked(allPartsDictionaryWithParents, soNumber)

    if tankType.lower() == 'ua':
        ppFolderPath, newMainFolder = folderCreation(soNumber, tankType, 'PP')
        itemListCreator(allPartsPath, allPartsDrawing, 'Parts - SAP', newMainFolder, soNumber, 'PP', tankType)
        
        if tx2:
            tx2FolderPath, newMainFolder = folderCreation(soNumber, tankType, 'TX2')
            allPartsDictionaryWithParents = fileCompile(allPartsPath, tx2FolderPath, 'p8', allPartsDictionaryWithParents, soNumber)
            itemListCreator(allPartsPath, allPartsDrawing, '(TX2)', newMainFolder, soNumber, 'PURCHASE LIST (TX2)', tankType)
            uaCombined(tx2FolderPath, soNumber)
        if cubars:
            cuFolderPath, newMainFolder = folderCreation(soNumber, tankType, 'PP-CU')
            allPartsDictionaryWithParents = fileCompile(allPartsPath, cuFolderPath, 'p4cu', allPartsDictionaryWithParents, soNumber)
            itemListCreator(allPartsPath, allPartsDrawing, '(Cu Bars)', newMainFolder, soNumber, 'PURCHASE LIST (CU BARS)', tankType)

        allPartsDictionaryWithParents = fileCompile(allPartsPath, ppFolderPath, 'p', allPartsDictionaryWithParents, soNumber)

    if tankType.lower() == 'clamp':
        
        ssFolderPath, newMainFolder = folderCreation(soNumber, tankType, 'CLAMP-SS')
        itemListCreator(allPartsPath, allPartsDrawing, 'Steel Supplier Parts', newMainFolder, soNumber, 'SS', tankType)
        allPartsDictionaryWithParents = fileCompile(allPartsPath, ssFolderPath, 's', allPartsDictionaryWithParents, soNumber)
        
        InsulationRawText = read_insulation(allPartsPath, inpDrawing)
    
        inpDictionaryUnsorted = inpDataCleanse(InsulationRawText, soNumber)
        inpDictionary = {k: inpDictionaryUnsorted[k] for k in sorted(inpDictionaryUnsorted)}
    
        inpDictionaryWithParents = findParents(allPartsPath, inpDictionary, soNumber)

        inpFolderPath, newMainFolder = folderCreation(soNumber, tankType, 'INSULATION')
        itemListCreator(allPartsPath, inpDrawing, 'Parts - SAP', newMainFolder, soNumber, 'INSULATION', tankType)
        allPartsDictionaryWithParents = fileCompile(allPartsPath, inpFolderPath, 'p', inpDictionaryWithParents, soNumber)
        
        inpAssyListCreator(allPartsPath, inpDrawing, newMainFolder, soNumber)
        inpAssyFolderPath, newMainFolder = folderCreation(soNumber, tankType, 'INSULATION-ASSY')
        inpCombined(inpFolderPath, soNumber)

        assyInsulationData = read_assyInsulation(allPartsPath, inpDrawing)
        assyInsulationList = inpAssyDataCleanse(assyInsulationData)
        inpAssyCompile(allPartsPath, inpAssyFolderPath, assyInsulationList)

        notPacked(inpDictionaryWithParents, soNumber)



    input("Success! Press any key to close window.")

main()
