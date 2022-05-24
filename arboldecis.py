import time
import random

class arbolDecis:
    def tomar_decision(self,ESTADO,BATT,SERVICIO):
        time_sleep=10
        if ESTADO==1:
            state=int(random.randint(1,4))
        elif ESTADO==2:
            state=int(random.randint(1,2))
        elif ESTADO==3:
            state=int(random.randint(1,2))
            if state==2:
                state=3
        elif ESTADO==4:
            state=int(random.randint(1,2))
            if state==2:
                state=4
        return state,time_sleep
