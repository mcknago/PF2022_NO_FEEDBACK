import time
import random

class arbolDecision:
    def tomar_decision(self,BATT,SERVICIO):
        time_sleep=10
        print(f'Arbol:El Servicio es {SERVICIO} Potencia PROMEDIO es: {BATT}')
        state=int(random.randint(0,4))
        print(f'Arbol: El estado es {state} y el tiempo es {time_sleep}')
        return state,time_sleep
