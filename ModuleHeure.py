from time import*

def HourSup(h1):
    hour = strftime("%H")
    h1 = int(h1)
    hourINT = int(hour)
    if hourINT >= h1:
        return True
    else :
        return False


def HourInf(h1):
    hour = strftime("%H")
    h1 = int(h1)
    hourINT = int(hour)
    if hourINT <= h1:
        return True
    else :
        return False