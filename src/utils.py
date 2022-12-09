#Funciones necesarias para hacer las gráficas
import numpy as np
from numpy import linalg as LA
import warnings
import math

warnings.filterwarnings("ignore")
#funcion auxiliar para calcular errores relativos
def compute_error(obj,approx):
    '''
    Relative or absolute error between obj and approx.
    '''
    if LA.norm(obj) > np.nextafter(0,1):
        Err = LA.norm(obj-approx)/LA.norm(obj)
    else:
        Err = LA.norm(obj-approx)
    return Err


def RK4(f,a,b,alpha,N):
    '''
    Runge-Kutta order four method to approximate the solution of an
    ordinary differential equation with an initial condition
    
    INPUTS:
    
    f(function)  : The function that defines the ordinary differential equation
    a(float)     : left extreme of the solution domain [a,b]
    b(float)     : right extreme of the solution domain [a,b]
    alpha(float) : initial condition y(a)=alpha
    N(integer)   : 
    
    OUTPUT:
    
    w(onedarray) : approximation of function y at N equally spaced point of [a,b]
    '''
    h=(b-a)/N
    t=np.zeros(N+1)
    w=np.zeros(N+1)
    w[0]=alpha
    for i in range(0,N):
        t[i]=a+i*h
        K1=h*f(t[i],w[i])
        K2= h*f(t[i]+h/2, w[i]+K1/2)
        K3= h*f(t[i]+h/2, w[i]+K2/2)
        K4= h*f(t[i]+h/2, w[i]+K3)
        w[i+1]=w[i]+(K1+2*K2+2*K3+K4)/6
    t[N]=b
    return t,w 

#funcion que define a la ecuacion diferencial que resolveremos
def fun_difEq(x,t):
    np.sqrt((4*x**2-(lam*x**2-k)**2))/(lam*x**2-k):


#La siguiente funcion es una especie de grid search para buscar los mejores hiperparametros
# de la ecuacion diferencial que nos permitan aproximar de mejor manera la solucion del problema
#de optimizacion

def Delaunay(k1,lambda,a,b,xa,xb,vol):
    '''
    comentar esta funcion
    '''
    for (i in 1:n):
        for (j in 1:m):
            lam =lambda[j]
            k=k1[i]
            fun = fun_difEq #funcion de la ecuacion diferencial que resolveremos

            solu=RK4(fun,a, b, alpha=xa, N=1000)[1]
            final=length(solu)
            if(solu[final]!=’nan’) {
            if(xb!=xa){
            xb=1195.5
            error=abs(solu[final]-xb)
            if(error<0.4){
            areas=rep(0,length(solu))
            fun = fun_difEq

            #Verificar que la solucion satisface la condición de volumen
            integrando=pi*solu^2
            for(i in 2:(length(solu)+1)):
                areas[i-1]=0.001*(integrando[i]+integrando[i-1])/2

            integral=sum(areas[1:length(areas)-1])

            #calcular error de la integral
            err_integral=abs(integral-vol)

            