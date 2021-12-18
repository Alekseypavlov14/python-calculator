def program():
    expression = input().replace(' ', '')

    # const symbols
    numSymbols = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.')
    ops = ('+', '-', '*', '/')

    # pluses and minuses
    lastOps = []
    for symbol in expression:
        if symbol == '+' or symbol == '-':
            lastOps.append(symbol)

    # get sub expression
    subexp = expression.replace('+', ' ').replace('-', ' ')

    # get monomials
    monomials = subexp.split(" ")

    def step(monomials):
        newMon = ''
        newMonomials = []

        for monomial in monomials:
            numbers = []
            newOps = []
            if '*' in monomial or '/' in monomial:
                # get numbers
                numbers = monomial.replace('*', ' ').replace('/', ' ').split(' ')

                # get ops
                ops = list(monomial.replace('0', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '').replace('.', ''))

                # solve
                i = 0
                
                for op in ops:
                    a = numbers[i]
                    b = numbers[i + 1]
                    c = 0
                    if ops[0] == '*':
                        c = float(a) * float(b)
                    elif ops[0] == '/':
                        c = float(a) / float(b)
                    else:
                        print('Unexpected operator: ', op)

                    # remake numbers[]
                    numbers = ' '.join(numbers).replace(str(a) + ' ' + str(b), str(c), 1).split(' ')
                    # remake ops[]
                    ops.pop(i)
                    newOps = ''.join(ops)
                    
            else:
                numbers.append(monomial)
                newOps = []
            # set monomials again
            j = 0
            
            for oper in newOps:
                newMon = newMon + numbers[j] + newOps[j]
                j += 1
            newMon = newMon + numbers[-1]
            
            newMonomials.append(newMon)
            newMon = ''

        monomials = newMonomials

        return monomials



    index = 1
    while True:
        monomials = step(monomials)
        
        if '*' in ' '.join(monomials) or '/' in ' '.join(monomials):
            index += 1
            continue
        else:
            break

    # final solve
    I = 0
    for op in lastOps:
        a = monomials[I]
        b = monomials[I + 1]
        c = 0
        if op == '+':
            c = float(a) + float(b)
        elif op == '-':
            c = float(a) - float(b)
        else:
            print('Unexpected operator: ', op)

        # remake numbers[]
        monomials = ' '.join(monomials).replace(str(a) + ' ' + str(b), str(c), 1).split(' ')
        # remake ops[]
        list(lastOps).pop(I)
        lastOps = ''.join(lastOps)

    print(str(monomials[0]) + '\n')

while True:
    program()