import sympy as sp 
import matplotlib.pyplot as plt
import numpy as np



x = sp.Symbol('x') #Definerer x som en ukjent 

f_u = sp.E**((-x)/4) #Definerer et ledd i f(x)
f_m = sp.atan(x) #Deffinerer det andre leddet i f(x)

f_x = f_u * f_m #Definerer f(x) som et produkt av f_u og f_m
print("F(x) = ", f_x) #Printer ut f(x)

df = sp.diff(f_x, x) #Bruker sympy til å regne ut den deriverte av f(x)
print("F'(x) = ", df) #Printer ut den deriverte 

#Finner toppunkt og starter med x = 0 og går oppover derifra. 
toppunkt_x = sp.nsolve(df, x, -0) 
toppunkt_y = f_x.subs(x, toppunkt_x) #Her bytter vi ut symbolet x med x-verdien til toppunktet for å finne y-verdien

print("Toppunktet ligger i [", toppunkt_x, ", ", toppunkt_y, "]")

#Konverterer funksjonene til en nummerisk funksjon som kan plottes. X betyr at x-en er variabelen, f_x/df er funksjonene som skal konverteres og nympy spesifiserer at det skal konvereteres til en numpy funksjon. Tidligere lagde vi symbolsk funksjoner, men gjør de her om til nummeriske for å kunne plotte dem
f_nummerisk = sp.lambdify(x, f_x, 'numpy')  
df_nummerisk = sp.lambdify(x, df, 'numpy')

antall_x_veridier = np.linspace(-10, 10, 1000) #Lager 1000 x-verdier mellom -10 og 10

#Sjekker funksjonene for alle 1000 x-verdiene 
y_verider_til_f_x = f_nummerisk(antall_x_veridier)
y_verider_til_df = df_nummerisk(antall_x_veridier)

#Plotter f(x) og f'(x)
plt.plot(antall_x_veridier, y_verider_til_f_x, label = "f(x)")
plt.plot(antall_x_veridier, y_verider_til_df, label = "f'(x)")

#Plotter toppunktet
plt.scatter([toppunkt_x], [toppunkt_y], color = 'red', label = "toppunkt")

#Viser grafen med et rutenett og navn 
plt.grid(True)
plt.legend()
plt.show()

#Resultat: Toppunktet ligger i [ 1.69070815547413 ,  0.679322264945093 ]










