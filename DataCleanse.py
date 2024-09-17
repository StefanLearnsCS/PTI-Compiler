
def dataCleanse(rawText):
    lines = rawText.strip().split('\n')

    partsMap = {}

    for line in lines:
        parts = line.split()
        
        if parts[0].isdigit():
            partsMap[int(parts[0])] = {'drawing': parts[2], 'issue': parts[-1], 'packed': False}

    return partsMap