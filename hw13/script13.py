def toCelsium(farengeit):
    return (farengeit - 32) / 1.8


def toFarengeit(celsium):
    return (celsium * 1.8) + 32


print("30 градусов по фаренгейту это {}".format(toCelsium(30)))
print("-1.11 градусов по цельсию это {}".format(toFarengeit(-1.11)))
