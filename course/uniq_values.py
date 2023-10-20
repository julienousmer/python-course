def keepUniqueValue(datas):
    finalDatas = []
    isIn = False
    for data in datas:
        for finalData in finalDatas:
            if data == finalData:
                isIn = True
        if isIn == False:
            finalDatas.append(data)
        isIn = False
    return finalDatas

print(keepUniqueValue([1, 5, 7, 1, 5, 11, 25, 1, 18, 17, 7]))
