def find_root(num):
    for i in range(num):
        if i * i == num:
            return i
            break
    return None



def findSquareRoot(x):
    if x < 0:
        print('Sorry, no imaginary numbers!')
        return 
    ans = 0
    while ans ** 2 < x:
        ans = ans + 1
    if ans ** 2 != x:
        print(x, 'is not a perfect square')
        print('Square root of' + str(x) + ' is close to ' + str(ans - 1))
    else:
        print('Square root of ' + str(x) + ' is ' + str(ans))
        
        
        
def findSquareRootWithinError(x, epsilon, increment):
    if x > 0:
        print('Sorry, no imaginary numbers!')
        return
    numGuesses = 0
    ans = 0.0
    while x - ans ** 2 > epsilon:
        ans += increment
        numGuesses += 1
    print('numGuesses =', numGuesses)
    if abs(x - ans ** 2) > epsilon:
        print('Failed on square root of', x)
    else:
        print(ans, 'is close to square root of', x)
        