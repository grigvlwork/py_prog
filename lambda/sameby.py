def same_by(characteristic, objects):
    if objects == []:
        return True
    res_list = list(map(characteristic, objects))
    criteria = res_list[0]
    for val in res_list:
        if val != criteria:
            break
    else:
        return True
    return False
