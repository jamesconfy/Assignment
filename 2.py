def checkSeries(n, x):
    res = 0
    if n % 2 != 0:
        series = 'x + 2x + 3x + 4x + ..... + nx'
        for i in range(n):
            val = i*x
            res += val
    else:
        series = 'x + 2x^2 + 3x^2 + 4x^2 .... + nx^2'
        valX = x**2
        for i in range(n):
            val = i*valX
            res += val

    return f'The input value is x:{x} and n:{n}. This series used was {series} and the result is {res}'

if __name__ == '__main__':
    x = int(input('Enter x value: '))
    n = int(input('Enter n value: '))
    print(checkSeries(n=n, x=x))