import re

def run(s):

    for i in s:
        username, other = i.split('@')    
        dominio, extension = other.split('.')
        
        print(i)
        if username == 'juan':
            print('Es un username valido')
        else:
            print('No es un username valido')

        if dominio == 'gmail':
            print('Es una extensión valido')
        else:
            print('No es una extensión valido')

        if len(extension)<=3 and len(extension)>0:
            print('Es una extensión valida')
        else:
            print('No es un extensión valida')
        print('')
    print(sorted(s))
if __name__ == '__main__':
    s = ['juan@gmail.com', 'felipe@hotmail.com', 'juan@stere.como']
    
    run(s)