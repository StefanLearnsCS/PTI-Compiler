import os

def findParents(source, itemMap, soNumber):
    
    updatedMap = itemMap

    for key, value in itemMap.items():

        itemNumber = value['drawing'].lower()
        
        pdfName = itemNumber + '.pdf'
        dxfName = itemNumber + '.dxf'
        multiDxfName = itemNumber + '_'

        found = 0
        relDrawing = 0

        if soNumber in itemNumber:
            relDrawing = 1
            for root, dirs, files in os.walk(source):
                for file in files:
                    if (pdfName in file) or (dxfName in file) or (multiDxfName in file):
                        found = 1
        
        keyTraverse = key - 1

        if relDrawing == 1:
            while found == 0 and keyTraverse > 1:
                if 'M' in itemMap[keyTraverse]['issue']:
                    useDrawing = input('Could not find drawing for ' + itemNumber + '. Would you like to use parent assembly drawing [' + itemMap[keyTraverse]['drawing'] + '] instead? (Y/N)')
                    if useDrawing == 'y' or useDrawing == 'Y':
                        updatedMap[key]['drawing'] = itemMap[keyTraverse]['drawing']
                        found = 1
                    else:
                        break
                else:
                    keyTraverse -= 1

    return updatedMap