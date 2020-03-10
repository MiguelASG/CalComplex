from sys import stdin
import math

def suma(c1, c2):
    a,b = 0, 0
    a = c1[0]+c2[0]
    b = c1[1]+c2[1]
    return [a,b]

def resta(c1, c2):
    a,b = 0, 0
    a = c1[0]-c2[0]
    b = c1[1]-c2[1]
    return [a,b]

def mult(c1,c2):
    a,b = 0, 0
    a = (c1[0]*c2[0] - c1[1]*c2[1])
    b = (c1[0]*c2[1] + c1[1]*c2[0])
    return [a,b]


def div(c1,c2):
    a,b = 0, 0
    if c2[0]==c2[1]==0: return "imposible"
    a = (c1[0]*c2[0]+ c1[1]*c2[1])/(c2[0]**2+c2[1]**2)
    b = (c2[0]*c1[1]- c1[0]*c2[1])/(c2[0]**2+c2[1]**2)
    return [a,b]

def mod(c1):
    a = c1[0]**2
    b = c1[1]**2
    rta = (a+b)**(1/2)
    return rta

def conj(c1):
    a = c1[0]
    b = -c1[1]
    return [a,b]

def pol(c1):
    if c1[0]==0: return "imposible"
    ang = math.degrees(math.atan(c1[1]/c1[0]))
    p = mod(c1)
    return [p,ang]
    
    

def cart(p,ang):
    ang = math.radians(ang)
    a = p*math.cos(ang)
    b = p*math.sin(ang)
    return [a,b]

def fase(c1):
    f = pol(c1)
    return (f[1]%91)


def sumvect(v1,v2):
    sol = []
    if len(v1)!=len(v2):
        return "imposible"
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
        return "imposible"
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
    res = [[0 for i in range(len(m1[0]))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res[j][i] = m1[i][j]
    return res

def conjmv(m1):
    res = [[0 for i in range(len(m1))] for j in range(len(m1[0]))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res[i][j] = conj(m[i][j])
    return res

def adjunta(m1):
    res = transpuesta(conjmv(m1))
    return res

def accion(m,v):
    if (len(m[0])!=len(v)): return "imposible" 
    else:
        return multmatr(m,v)

def innervec(v1,v2):
    if len(v1)!=len(v2):return "imposible"
    else:
        s = [0,0]
        for i in range(len(v2)):
            s = suma(s,mult(v2[i],v1[i]))
    return s

def normavec(v):
    s = [0,0]
    for i in range(len(v)):
        s = suma(s,mult(v[i],conj(v[i])))
    s = math.sqrt(s[0])
    return s

def distanciavec(v1,v2):
    s = [0,0]
    if len(v1)!=len(v2): return  "imposible"
    for i in range(len(v1)):
        s = suma(s,mult(conj(resta(v1[i],v2[i])), resta(v1[i], v2[i])))
    s = math.sqrt(s[0])
    return s

def matuni(m):
    if len(m)!=len(m[0]): return "imposible"
    iden = [[[1,0] if i==j else [0,0] for i in range(len(m))]for j in range(len(m))]
    a,b = [0,0],[0,0]
    a = mulmatr(m,adjunta(m))
    b = mulmatr(adjunta(m),m)
    if a==b==iden: True
    return False

def hermitian(m):
    a = adjunta(m)
    if m == a: return True
    return False

def protens(m1,m2):
    res = [[0 for i in range(len(m1)*len(m2))] for j in range(len(m1[0])*len(m2[0]))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            for k in range(len(m2)):
                for l in range(len(m2[0])):
                    res[len(m2)*i+k][len(m2[0])*j+l] = mult(m1[i][j],m2[k][l])
    return res

def mulmatr(m1,m2):
    if(len(m1[0])!=len(m2)): return "imposible"
    sol = [[0 for i in range(len(m1))] for j in range(len(m2[0]))]
    for l in range(len(m2[0])):
        for i in range(len(m1)):
            su = [0,0]
            for j in range(len(m1[0])):
                su = suma(su,mult(m1[i][j],m2[j][l]))
            sol[i][l] = su
    return sol
                
            
def probabilidad(v):
    s = 0
    l = []
    for i in v:
        s += i[0]**2+(i[1]**2)
        l.append(i[0]**2+i[1]**2)
    s = math.sqrt(s)
    for i in range(len(l)):
        l[i] = l[i]/(s**2)
    return l
                
                


"""
def main():
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
"""
