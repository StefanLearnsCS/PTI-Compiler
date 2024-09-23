import shutil
import os

def fileCompile(source, folderPath, iCode, itemMap, soNumber):

    updatedMap = itemMap
    spiPath1 = "Z:\\SHOP_SALES_ORDER\\SPI PARTS\\SPI PARTS"
    spiPath2 = "Z:\\SHOP_SALES_ORDER\\SPI PARTS\\SPI SAP PARTS"

    for key, value in updatedMap.items():

        itemNumber = value['drawing'].lower()
        issueCode = value['issue'].lower()
        
        pdfName = itemNumber + '.pdf'
        dxfName = itemNumber + '.dxf'
        multiDxfName = itemNumber + '_'

        if iCode.lower() == 's' or not value['packed']:

            if soNumber in itemNumber:
                if iCode in issueCode:
                    for root, dirs, files in os.walk(source):
                        for file in files:
                            if (pdfName in file) or (dxfName in file) or (multiDxfName in file):
                                source_file = os.path.join(root, file)
                                dest_file = os.path.join(folderPath, file)
                                shutil.copy2(source_file, dest_file)
                                updatedMap[key]["packed"] = True

            if 'spi' in itemNumber.lower():
                if iCode in issueCode:
                    for root, dirs, files in os.walk(spiPath1):
                        for file in files:
                            if (multiDxfName.lower() in file.lower()):
                                source_file = os.path.join(root, file)
                                dest_file = os.path.join(folderPath, file)
                                shutil.copy2(source_file, dest_file)
                                updatedMap[key]["packed"] = True
                    for root, dirs, files in os.walk(spiPath2):
                        for file in files:
                            if (multiDxfName.lower() in file.lower()):
                                source_file = os.path.join(root, file)
                                dest_file = os.path.join(folderPath, file)
                                shutil.copy2(source_file, dest_file)
                                updatedMap[key]["packed"] = True
    
    return updatedMap
