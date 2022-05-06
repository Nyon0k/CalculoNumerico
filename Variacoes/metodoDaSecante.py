#python 3
#David Turati
#davidturati@gmail.com
#metodo da secante
import math

def funcao(x): 				#funcao principal
	return (x*(math.log10(x)))-1  	#altere a funcao aqui

def novox(x0,x1):			#novo valor de x 
	return (x0*funcao(x1) - x1*funcao(x0)) / (funcao(x1) - funcao(x0))

def secante(x,y):
	#primeira itercao fora do loop
	er=10**-3				#erro dado, altere o erro aqui
	k=0						#numero de iteracoes
	xka=x 					#valor de x
	fx=funcao(xka)			#valor da funcao
	print(k,xka,fx)			#imprime valores

	er=5*10**-4				#erro dado, altere o erro aqui
	k=k+1					#numero de iteracoes
	xkp=y 					#valor de x
	fx=funcao(xkp)			#valor da funcao
	print(k,xkp,fx)			#imprime valores
	
	while(abs(fx)>er):		#verifica erro
		k=k+1 				#incrementa iteracao
		nxk=novox(xka,xkp)  #novo valor de x
		fx=funcao(nxk)      #calcula nova funcao
		xka=xkp             #novo valor para xka, (Xk-1)
		xkp=nxk				#novo valor para xkp, (Xk-2)
		print(k,nxk,fx)		#imprime valores
	

secante(0,1)				#intervalo dado