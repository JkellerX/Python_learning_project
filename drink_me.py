#There is something wrong... 

def drink_me(param):
    info = param + ' glass'
    print(info)
    param = 'empty'

    glass = 'full'
    drink_me(glass)
    print('glass is', glass)