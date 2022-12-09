import numpy as np
from utils import RK4
#La siguiente funcion es una especie de grid search para buscar los mejores hiperparametros
# de la ecuacion diferencial que nos permitan aproximar de mejor manera la solucion del problema
#de optimizacion

def delaunay(k1,Lambda,a,b,xa,xb,vol):

    #extras
    n=len(k1)
    m=len(Lambda)

    for i in range(1,n+1):
        for j in range(1,m+1):

            lam =Lambda[j]
            k=k1[i]
            fun = fun_difEq #funcion de la ecuacion diferencial que resolveremos

            solu=RK4(fun,a, b, alpha=xa, N=1000)[1]
            final=len(solu)

            #verificar que el vector de soluciones no tenga nan's
            if(solu[final]!='nan'):
                #verificar que la condicion final e inicial no sean iguales
                if(xb!=xa):
                    error=abs(solu[final]-xb) #verificamos que el ultimo punto de la solucion este cerca de la condicion final
                    #si cierto, nos quedamos con esta solucion y verificamos que cumple la condicion de volumen
                    if(error<0.4):
                        areas=np.zeros(len(solu))
                        fun = fun_difEq

                        #Verificar que la solucion satisface la condición de volumen
                        integrando=np.pi*solu^2
                        for i in 2,(len(solu)+1):
                            areas[i-1]=0.001*(integrando[i]+integrando[i-1])/2
                            integral=sum(areas[1:len(areas)-1])

                        #calcular error de la integral
                        err_integral=np.abs(integral-vol)
            #si la solucion stisface la condicion de volumen, salvo por un error <2, quedarse con la solucion          
            if(err_integral<2):
                e=error
                err_integral=abs(integral-vol)
                solfinal=solu
                best_hyperparams= lam,k

    return solfinal, e, integral, err_integral, best_hyperparams
