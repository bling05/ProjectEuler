def factorial(x):  # Recursive function
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)


def pithon():  # arctan Taylor series
    pi = 0
    for i in range(0, 9999):
        pi += ((-1) ** i) * (1 / (2 * i + 1))
    return 4 * pi


pi = pithon()
pistr = str(pi)


def e(x):
    approx = 0
    for i in range(0, 10):
        approx += (x ** i) / (factorial(i))
    return approx


e = e(1)
estr = str(e)


def derivative(exp, x):  # Ex: derivative('sin(x)*(x**2)', 2)
    h = 0.00000001
    exp2 = exp.replace('x', '(x+h)')
    deriv = (eval(exp2) - eval(exp)) / h
    return deriv


def integral(a, b, exp):  # Ex: integral(0,3,'x**3 + 5*(x**2)')
    area = 0
    x = a
    h = 0.00001
    while x <= b:  # Left Riemann Sum
        area += eval(exp) * h
        x += h
    return area


def squart(x):  # Babylonian method
    if x == 0: return 0
    if x < 0:
        return 9999999999
    approx = x / 3
    deg = 100
    for i in range(0, deg):
        approx = (approx + (x / approx)) / 2
    return approx


def sin(x):
    while x > 2 * pi:
        x -= 2 * pi
    while x < 0:
        x += 2 * pi
    approx = 0
    for i in range(0, 10):  # 10th degree polynomial
        approx += (x ** ((2 * i) + 1)) / (factorial((2 * i) + 1) * (-1) ** i)
    return approx


def csc(x):
    return 1 / sin(x)


def cos(x):
    while x > 2 * pi:
        x -= 2 * pi
    while x < 0:
        x += 2 * pi
    approx = 0
    for i in range(0, 10):  # 10th degree polynomial
        approx += (x ** (2 * i)) / (factorial(2 * i)) * ((-1) ** i)
    return approx


def sec(x):
    return 1 / cos(x)


def tan(x):
    return sin(x) / cos(x)


def cot(x):
    return 1 / tan(x)


def arcsin(x):
    if x == 1: return pi/2
    if x == -1: return -pi/2
    approx = 0
    for i in range(0, 10):
        approx += (factorial(2 * i)) * (x ** ((2 * i) + 1)) / (((2 ** i) * (factorial(i))) ** 2) / ((2 * i) + 1)
    return approx


'''def arccsc(x):
    if x == 1: return pi / 2
    if x == -1: return -(pi / 2)
    approx = arcsin(1 / x)
    return approx'''


def arccos(x):
    if x == 1: return 0
    if x == -1: return pi
    approx = pi / 2 - arcsin(x)
    return approx


'''def arcsec(x):
    if x == 1: return 0
    if x == -1: return pi
    approx = arccos(1 / x)
    return approx'''


def arctan(x):
    if x > 1: x = 1
    if x < 1: x = -1
    approx = 0
    for i in range(0, 10):
        approx += (((-1) ** i) * (x ** ((2 * i) + 1))) / ((2 * i) + 1)
    return approx

'''def arccot(x):
    if x == 0: return pi/2
    approx = arctan(1/x)
    return approx'''

def ln(x):
    approx = integral(1, x, '1/x')
    if approx == 0: approx = -99999999
    return approx


def mean(str):  # Ex: mean('5 21 4 49 2 0')
    li = str.split()
    li = [float(i) for i in li]
    average = (sum(li)) / (len(li))
    return average


def median(str):  # Ex: median('5 4 21 9 2 15')
    li = str.split()
    li = sorted([float(i) for i in li])
    index = (len(li) - 1) // 2
    if (len(li) % 2):
        return li[index]
    else:
        return (li[index] + li[index + 1]) / 2


def mode(str):
    li = str.split()
    counts = {}
    for ele in li:
        if ele in counts:
            counts[ele] += 1
        else:
            counts[ele] = 1
    return [key for key in counts.keys() if counts[key] == max(counts.values())]


def nPr(n, r):  # permutation
    answer = factorial(n) / (factorial(n - r))
    return answer


def nCr(n, r):  # combination
    answer = factorial(n) / ((factorial(r)) ** (factorial(n - r)))
    return answer


def VoR(R, a, b):
    R = R.replace('y', 'x')
    R2 = '((' + R + ')' + '**2)'
    vol = pi * (integral(a, b, R2))
    return vol


def VoC(R, A, a, b):
    if A == 'square': A = 'x**2'
    if A == 'semicircle': A = 'pi * (x**2) / 8'
    if A == 'equitriangle': A = '(x**2) * squart(3) / 4'
    A = '(' + A + ')'
    R = R.replace('x', A).replace('y', A)
    vol = integral(a, b, R)
    return vol


def calc(ans):
    if type(ans) is list:
        str = ''
        for a in ans:
            str += a + ' '
        print(str)
        return
    if ans <= 0.00011 and ans >= -0.00011:
        ans = 0
    if ans > 9999999 or ans < -9999999:
        print('undefined')
        return
    print(round(ans, 4))


def sigma(i, n, exp):
    sum = i
    for x in range(i + 1, n + 1):
        sum += eval(exp)
    return sum


def samesign(a, b):
    return a * b >= 0

def zero(exp, a, b):
    tolerance = 0.000001
    fA = eval(exp.replace('x', 'a'))
    fB = eval(exp.replace('x', 'b'))
    if samesign(fA, fB):  # IN CASE OF TOUCHING ZEROES
        print(
            'Although finding "touching zeroes" will be inaccurate and slower, f(x) is still calculated to an accuracy of 10 decimal places!')
        return zero2(exp, a, b)
    while True:
        c = (a + b) / 2
        fC = eval(exp.replace('x', str(c)))
        if samesign(fA, fC):
            a = c
        else:
            b = c
        if abs(b - a) < tolerance: break
    return c


def zero2(exp, a, b):
    temp = a
    while a < b:
        fA = eval(exp.replace('x', str(a)))
        if round(fA, 10) == 0:
            return round(a, 4)
        else:
            a += 0.00001
    a = temp
    while a < b:
        fA = eval(exp.replace('x', str(a)))
        if fA < pow(10, -5) and fA > pow(-10, -5):
            return a
        else:
            a += 0.00001
    return 99999999


import PySimpleGUI as sg

layout = [[sg.Text("Group 1's Calculator")], [sg.Button("               Evaluate!               ")],
          [sg.Button("Differentiate!"), sg.Button("Integrate!")],
          [sg.Button("Mean"), sg.Button("Median"), sg.Button("Mode")],
          [sg.Button("nPr"), sg.Button("nCr"), sg.Button("Summation")],
          [sg.Button("Volume of Revolution"), sg.Button("Volume of Cross-Section")],
          [sg.Button('INSANELY FAST BISECTION METHOD COMPOUND ROOT FINDER™ (IFBMCRFTM)')],
          [sg.Text("Available functions: sin(x), cos(x), tan(x), csc(x), sec(x), cot(x),")],
          [sg.Text("arcsin(x), arccos(x), arctan(x), ln(x), pi, e,  squart(x), factorial(x)")],
          [sg.Text("Example: sin(10) * (3^2) + pi")],
          [sg.Button("allison is cool!"), sg.Button("branton is cool!")], [sg.Button("Close")]]

# Create the window
window = sg.Window(" ", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED or event == 'Close':
        break

    if event == '               Evaluate!               ':
        calc(eval(input('Expression: ').replace('^', '**')))

    if event == 'Differentiate!':
        exp = input('Function: ').lower().replace('^', '**')
        x = eval(input('x = ').replace('e', estr).replace('pi', pistr).replace('^', '**'))
        calc(derivative(exp, x))

    if event == 'Integrate!':
        exp = input('Function: ').lower().replace('^', '**')
        a = eval(input('a = ').replace('e', estr).replace('pi', pistr).replace('^', '**'))
        b = eval(input('b = ').replace('e', estr).replace('pi', pistr).replace('^', '**'))
        calc(integral(a, b, exp))

    if event == 'Mean':
        calc(mean(input('Numbers (ex: 5 2 3 2): ')))
    if event == 'Median':
        calc(median(input('Numbers (ex: 5 2 3 2): ')))
    if event == 'Mode':
        calc(mode(input('Numbers (ex: 5 2 3 2): ')))

    if event == 'nPr':
        n = int(input('n = '))
        r = int(input('r = '))
        calc(nPr(n, r))
    if event == 'nCr':
        n = int(input('n = '))
        r = int(input('r = '))
        calc(nCr(n, r))

    if event == 'Summation':
        i = int(input('Index of summation: '))
        n = int(input('Upper bound: '))
        exp = input('Expression: ').lower().replace('^', '**')
        calc(sigma(i, n, exp))

    if event == 'Volume of Revolution':
        R = input('R (Ex: (x**2) + 3): ').lower().replace('^', '**')
        a = eval(input('a = ').replace('e', estr).replace('pi', pistr).replace('^', '**'))
        b = eval(input('b = ').replace('e', estr).replace('pi', pistr).replace('^', '**'))
        calc(VoR(R, a, b))

    if event == 'Volume of Cross-Section':
        R = input('R (Ex: (x**2) + 3): ').lower().replace('^', '**')
        print('Area templates: square, semicircle, equitriangle')
        A = input('Area of Cross-Section (Ex: x**3): ').lower().replace('^', '**')
        a = eval(input('a = ').replace('e', estr).replace('pi', pistr).replace('^', '**'))
        b = eval(input('b = ').replace('e', estr).replace('pi', pistr).replace('^', '**'))
        calc(VoC(R, A, a, b))

    if event == 'INSANELY FAST BISECTION METHOD COMPOUND ROOT FINDER™ (IFBMCRFTM)':
        exp = input('Function: ').lower().replace('^', '**')
        a = eval(input('a = ').replace('e', estr).replace('pi', pistr).replace('^', '**'))
        b = eval(input('b = ').replace('e', estr).replace('pi', pistr).replace('^', '**'))
        calc(zero(exp, a, b))

    if event == 'allison is cool!':
        print('yeah shes more than cool')
    if event == 'branton is cool!':
        print('the right answer')
window.close()

