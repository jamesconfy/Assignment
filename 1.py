def convertTime(val):
    hour, min = val//60, val%60
    return hour, min

def getTime(n=100):
    val = 0.5 + (n-1)*0.625
    hour, min = convertTime(val)
    if hour:
        return f'Running time in hour is {hour}'
    else:
        return f'Running time in minutes is {min}'

if __name__ == '__main__':
#    print(convertTime(130))
    print(getTime())