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
    #print('el vector tiene longitud '+str(p)+' desde el origen en un angulo de '+str(ang))
    return [p,ang]
    
    

def cart(p,ang):
    ang = math.radians(ang)
    a = p*math.cos(ang)
    b = p*math.sin(ang)
    return [a,b]
    #print('rta: ( '+str(a)+', '+str(b)+'i )')

def fase(c1):
    f = pol(c1)
    return (f[1]%91)


def sumvect(v1,v2):
    sol = []
    if len(v1)!=len(v2):
        return
    else:
        for i in range(len(v1)):
            sol.append(suma(v1[i],v2[i]))
    return sol

def invect(v1):
    sol = []
    for i in range(len(v1)):
        sol.append([-v1[i][0],-v1[i][1]])
    return sol

def escxvec(es,v1):
    sol = []
    for i in range(len(v1)):
        sol.append([es*v1[i][0],es*v1[i][1]])
    return sol

def sumatriz(m1,m2):
    sol = []
    if (len(m1)!=len(m2)) or (len(m1[0])!=len(m2[0])):
        return 
    else:
        for i in range(len(m1)):
            sol.append(list())
            sol[i]=sumvect(m1[i],m2[i])
    return sol

def invmatriz(m1):
    sol = []
    for i in range(len(m1)):
        sol.append(list())
        sol[i]=invect(m1[i])
    return sol

def escxmatr(e, m):
    sol = []
    for i in range(len(m)):
        sol.append(list())
        sol[i]=escxvec(e,m[i])
    return sol


def transpuesta(m1):
    res = [[0 for i in range(len(m1[0])] for j in range(len(m1)]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res[j][i] = m1[i][j]
    return res

def conjmv(m1):
    res = [[0 for i in range(len(m1)] for j in range(len(m1[0])]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res[i][j] = conj(m[i][j])
    return res

def adjunta(m1):
    res = transpuesta(conjmv(m1))
    return res


def protens(m1,m2):
    res = [[0 for i in range(len(m1)*len(m2))] for j in range(len(m1[0])*len(m2[0]))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            for k in range(len(m2)):
                for l in range(len(m2[0])):
                    res[len(m2)*i+k][len(m2[0])*j+l] = mult(m1[i][j],m2[k][l])
    return res

def mulmatr(m1,m2):
    if(len(m1[0])!=len(m2)): return
    sol = [[0 for i in range(len(m1))] for j in range(len(m2[0]))]
    for l in range(len(m2[0])):
        for i in range(len(m1)):
            su = [0,0]
            for j in range(len(m1[0])):
                su = suma(su,mult(m1[i][j],m2[j][l]))
            sol[i][l] = su
    return sol
                
            
                
                


"""print(invect([[1,2],[2,3]]))
print(escxvec(5,[[1,2],[2,3]]))
print(sumatriz([[[1,2],[2,3]],[[4,5],[6,7]]],[[[9,8],[8,7]],[[5,4],[1,0]]]))
print(invmatriz([[[1,2],[2,3]],[[4,5],[6,7]]]))
print(escxmatr(5,[[[1,2],[2,3]],[[4,5],[6,7]]]))
print(protens([[[1,2],[2,3]],[[4,5],[6,7]]],[[[9,8],[8,7]],[[5,4],[1,0]]]))
"""




def main():
    """
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
            """
    H = escxmatr(1/(2**(1/2)),[[[1,0],[1,0]],[[1,0],[-1,0]]])
    X = [[[0,0],[1,0]],[[1,0],[0,0]]]
    #print(H)
    M1 = protens(H,H)
    M2 = protens(H,X)
    for i in M1:
        print(i)
    #print(M2)
    print()
    print(mulmatr([[[1,2],[2,3],[3,5]],[[4,5],[6,7],[4,7]]],[[[1,2],[2,3]],[[4,5],[6,7]],[[6,1],[1,2]]]))

main()

