def notPacked(itemMap, soNumber):
    print('Items that were not placed in any packages:')
    print()
    for key, value in itemMap.items():
        if not value['packed'] and ('spi' in value['drawing'] or soNumber in value['drawing']):
            print(value['drawing'] + ' - Issue Code: ' + value['issue'])