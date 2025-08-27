import numpy as np
import pandas as pd
import argparse
import statsmodels.api as sm
import sys
import os
import matplotlib.pyplot as plt

#*------------------------------------------------------------------------------------------------
#* Almacena dataset histórico
#*------------------------------------------------------------------------------------------------
data = {
    'LOC': [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    'Esfuerzo': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
}

#*------------------------------------------------------------------------------------------------
#* Inicialización del programa
#*------------------------------------------------------------------------------------------------
version="7.1"
linear=False
exponential=False
os.system('cls')

#*------------------------------------------------------------------------------------------------
#* Procesa argumentos
#*------------------------------------------------------------------------------------------------
ap = argparse.ArgumentParser()

ap.add_argument("-v", "--version", required=False, help="version", action="store_true")
ap.add_argument("-x", "--exponential", required=False, help="Exponential model", action="store_true")
ap.add_argument("-l", "--linear", required=False, help="Linear model", action="store_true")
ap.add_argument("-p", "--predict", type=int, help="Predecir esfuerzo para LOC dado")

args = vars(ap.parse_args())

if args['version'] == True:
   print("Program %s version %s" % (sys.argv[0],version))
   sys.exit(0)

if args['linear'] == True:
   print("Program %s version %s" % (sys.argv[0],version))
   print("Linear correlation model selected")
   linear=True

if args['exponential'] == True:
   print("Program %s version %s" % (sys.argv[0],version))
   print("Exponential correlation model selected")
   exponential=True

if linear==False and exponential==False:
   print("Program %s version %s" % (sys.argv[0],version))
   print("Debe indicar modelo lineal (-l) o exponencial (-x) o ambos")

#*-----------------------------------------------------------------------------------------------
#* Definir dataset y procesar correlación entre LOC (complejidad) y Esfuerzo (PM)
#*-----------------------------------------------------------------------------------------------
df = pd.DataFrame(data)
correlation = df['LOC'].corr(df['Esfuerzo'])

#*------------------------------------------------------------------------------------------------
#* Procesa modelo lineal, usa numpy polyfit()
#*------------------------------------------------------------------------------------------------
if linear==True:
   a, b = np.polyfit(df['LOC'], df['Esfuerzo'], 1)
   R = np.corrcoef(df['LOC'], df['Esfuerzo'])
   r_value = R[0,1]**2

   print("Modelo lineal E=%.6f + %.6f*LOC" % (b,a))
   print("El R-squared=%.4f (lineal)" % (r_value))

   lbl=("modelo lineal (R-Sq=%.2f)" % (r_value))
   plt.plot(df['LOC'], a*df['LOC']+b,label=lbl,color='red')

   # Predicción si se pide
   if args['predict']:
       loc_pred = args['predict']
       esfuerzo_pred = a*loc_pred + b
       print(f"Predicción lineal para LOC={loc_pred}: {esfuerzo_pred:.2f} PM")
       plt.scatter([loc_pred], [esfuerzo_pred], color='blue', marker='x', s=120,
                   label=f"Predicción LOC={loc_pred}")

#*------------------------------------------------------------------------------------------------
#* procesa modelo exponencial utiliza OLS fit()
#*------------------------------------------------------------------------------------------------
if exponential==True:
   df['logEsfuerzo']=np.log(df['Esfuerzo'])
   df['logLOC']=np.log(df['LOC'])

   X = df['logLOC']
   Y = df['logEsfuerzo']
   X = sm.add_constant(X)  # Añadir una constante para el intercepto

   mx= sm.OLS(Y, X).fit()
   print(mx.summary())

   k=np.exp(mx.params['const'])
   b=mx.params['logLOC']

   print("Modelo exponencial E=%.6f*(LOC^%.6f)" % (k,b))
   print("El R-squared=%.2f (exponencial)" % (mx.rsquared))

   lbl=("modelo exponencial (R-Sq=%.2f)" % (mx.rsquared))
   plt.plot(df['LOC'], k*(df['LOC']**b),label=lbl,color='green')

   # Predicción si se pide
   if args['predict']:
       loc_pred = args['predict']
       esfuerzo_pred = k*(loc_pred**b)
       print(f"Predicción exponencial para LOC={loc_pred}: {esfuerzo_pred:.2f} PM")
       plt.scatter([loc_pred], [esfuerzo_pred], color='blue', marker='x', s=120,
                   label=f"Predicción LOC={loc_pred}")

#*------------------------------------------------------------------------------------------------
#* Hace plot del dataset histórico
#*------------------------------------------------------------------------------------------------
plt.scatter(df['LOC'], df['Esfuerzo'], label='Datos históricos')
plt.xlabel('Complejidad [LOC]')
plt.ylabel('Esfuerzo (persona-mes)')
plt.legend()
plt.show()

