

touru=100
shouru=101

def lilv_7(touru, shouru):
    return ((shouru - touru) / touru) * 365 / 7

def shouyi_7(touru, lilv):
    return touru * lilv / 100 / 360

print(lilv_7(100, 101))

print(shouyi_7(207736.15, 2.99))