from sys import stdin
import math

def suma(c1, c2):
    a,b = 0, 0
    a = c1[0]+c2[0]
    b = c1[1]+c2[1]
    return [a,b]
    #print('rta: ( '+str(a)+', '+str(b)+'i )')

def resta(c1, c2):
    a,b = 0, 0
    a = c1[0]-c2[0]
    b = c1[1]-c2[1]
    return [a,b]
    #print('rta: ( '+str(a)+', '+str(b)+'i )')

def mult(c1,c2):
    a,b = 0, 0
    a = (c1[0]*c2[0] - c1[1]*c2[1])
    b = (c1[0]*c2[1] + c1[1]*c2[0])
    return [a,b]
    #print('rta: ( '+str(a)+', '+str(b)+'i )')


def div(c1,c2):
    a,b = 0, 0
    a = (c1[0]*c2[0]+ c1[1]*c2[1])/(c2[0]**2+c2[1]**2)
    b = (c2[0]*c1[1]- c1[0]*c2[1])/(c2[0]**2+c2[1]**2)
    return [a,b]
    #print('rta: ( '+str(a)+', '+str(b)+'i )')

def mod(c1):
    a = c1[0]**2
    b = c1[1]**2
    rta = (a+b)**(1/2)
    return rta
    #print('rta: '+str(rta))

def conj(c1):
    a = c1[0]
    b = -c1[1]
    return [a,b]
    #print('rta: ( '+str(a)+', '+str(b)+'i )')

def pol(c1):
    ang = math.degrees(math.atan(c1[1]/c1[0]))
    p = mod(c1)
    return [p,ang]
    #print('el vector tiene longitud '+str(p)+' desde el origen en un angulo de '+str(ang))
    

def cart(p,ang):
    ang = math.radians(ang)
    a = p*math.cos(ang)
    b = p*math.sin(ang)
    return [a,b]
    #print('rta: ( '+str(a)+', '+str(b)+'i )')



"""def main():
    while True:
        l = stdin.readline().strip() 
        if l == '': break
        c1 = [float(a) for a in l.split()]
        op = stdin.readline().strip()
        l = stdin.readline().strip()
        if l == '': break
        c2 = [float(a) for a in l.split()]
        if op=='+':
            suma(c1,c2)
        elif op=='-':
            resta(c1,c2)
        elif op=='x':
            mult(c1,c2)
        elif op=='/':
            div(c1,c2)
        elif op=='mod':
            mod(c1)
        else:
            break


main()
"""
