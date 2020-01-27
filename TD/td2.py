val = "*+7"
ops = ['*', '+']


def operator(index):
    return val[index] in ops


def cal(index):
    return


def eval(op, index):
    if val[index+1] not in ops and val[index+2] not in ops:
        return val[index+1] + val[index+2] 
    if val[index+1] in ops and val[index+2] in ops:
        return eval(val[index+1], index+1) + eval(val[index+2], index+2)
    if val[index+1] in ops:
        return eval(val[index+1], index+1) + val[index+2], index+2
    if val[index+2] in ops:
        return eval(val[index+2], index+2) + val[index+1], index+1
