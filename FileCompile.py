import shutil
import os

def fileCompile(source, ssPath, ppPath, itemMap, soNumber):

    for key, value in itemMap.items():

        itemNumber = value['drawing'].lower()
        issueCode = value['issue'].lower()
        
        pdfName = itemNumber + '.pdf'
        dxfName = itemNumber + '.dxf'
        multiDxfName = itemNumber + '_'
        spiPath = "C:\\Users\\stefa\\OneDrive\\Desktop\\PTI Test\\20216\\20216 SPI"

        if soNumber in itemNumber:
            if 's' in issueCode:
                for root, dirs, files in os.walk(source):
                    for file in files:
                        if (pdfName in file) or (dxfName in file) or (multiDxfName in file):
                            source_file = os.path.join(root, file)
                            dest_file = os.path.join(ssPath, file)
                            shutil.copy2(source_file, dest_file)
            if 'p' in issueCode:
                for root, dirs, files in os.walk(source):
                    for file in files:
                        if (pdfName in file) or (dxfName in file) or (multiDxfName in file):
                            source_file = os.path.join(root, file)
                            dest_file = os.path.join(ppPath, file)
                            shutil.copy2(source_file, dest_file)

        if 'spi' in itemNumber:
            if 's' in issueCode:
                for root, dirs, files in os.walk(spiPath):
                    for file in files:
                        if (itemNumber in file):
                            source_file = os.path.join(root, file)
                            dest_file = os.path.join(ssPath, file)
                            shutil.copy2(source_file, dest_file)
            if 'p' in issueCode:
                for root, dirs, files in os.walk(spiPath):
                    for file in files:
                        if (itemNumber in file):
                            source_file = os.path.join(root, file)
                            dest_file = os.path.join(ppPath, file)
                            shutil.copy2(source_file, dest_file)