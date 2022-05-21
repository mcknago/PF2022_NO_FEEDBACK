from __future__ import annotations
from abc import ABC, abstractmethod
import numpy as np
import time
import datetime

# Finite State Machine.
class Controller:
    _state = None

    def __init__(self, state: State) -> None:
        self.setState(state)

    # method to change the state of the object
    def setState(self, state: State):

        self._state = state
        self._state.controller = self

    def presentState(self):
        print(f"Controller is in {type(self._state).__name__}")
    
    def returnState(self):
      if type(self._state).__name__ == "firstState":
        return 1
      if type(self._state).__name__ == "secondState":
        return 2
      if type(self._state).__name__ == "thirdState":
        return 3
      if type(self._state).__name__ == "fourthState":
        return 4
      else:
        return 0

    # the methods for executing the controller functionality. These depends on the current state of the object.
    def goTo1(self):
        self._state.goTo1()

    def goTo2(self):
        self._state.goTo2()

    def goTo3(self):
        self._state.goTo3()

    def goTo4(self):
        self._state.goTo4()

# The common state interface for all the states
class State(ABC):
    @property
    def controller(self) -> Controller:
        return self._controller

    @controller.setter
    def controller(self, controller: Controller) -> None:
        self._controller = controller

    @abstractmethod
    def goTo1(self) -> None:
        pass

    @abstractmethod
    def goTo2(self) -> None:
        pass

    @abstractmethod
    def goTo3(self) -> None:
        pass

    @abstractmethod
    def goTo4(self) -> None:
        pass


# The concrete states
class firstState(State):
    def goTo1(self) -> None:
        print("Already in state 1")

    def goTo2(self) -> None:
        print("Controller going to state 2")
        self.controller.setState(secondState())

    def goTo3(self) -> None:
        print("Controller going to state 3")
        self.controller.setState(thirdState())

    def goTo4(self) -> None:
        print("Controller going to state 4")
        self.controller.setState(fourthState())

class secondState(State):
    def goTo1(self) -> None:
        print("Controller going to state 1...")
        self.controller.setState(firstState())

    def goTo2(self) -> None:
        print("Already in state 2")

    def goTo3(self) -> None:
        print("Can't go to state 3, controller is going to state 1")
        self.controller.setState(firstState())

    def goTo4(self) -> None:
        print("Can't go to state 4, controller is going to state 1")
        self.controller.setState(firstState())

class thirdState(State):
    def goTo1(self) -> None:
        print("Controller going to state 1...")
        self.controller.setState(firstState())

    def goTo2(self) -> None:
        print("Can't go to state 2, controller is going to state 1")
        self.controller.setState(firstState())

    def goTo3(self) -> None:
        print("Already in state 3")

    def goTo4(self) -> None:
        print("Can't go to state 4, controller is going to state 1")
        self.controller.setState(firstState())

class fourthState(State):
    def goTo1(self) -> None:
        print("Controller going to state 1...")
        self.controller.setState(firstState())  

    def goTo2(self) -> None:
        print("Can't go to state 2, controller is going to state 1")
        self.controller.setState(firstState())

    def goTo3(self) -> None:
        print("Can't go to state 3, controller is going to state 1")
        self.controller.setState(firstState())

    def goTo4(self) -> None:
      print("Already in state 4")

def ahora():
    ahora_time = datetime.datetime.now()
    ahora_hora = ahora_time.hour
    ahora_minuto = ahora_time.minute
    ahora_segundo = ahora_time.second
    ahora_ya = ahora_hora + (ahora_minuto/60) + (ahora_segundo/3600)
    return ahora_ya

def HR_OSC():                               #Obtener el Flag "HR" del OSC
    # Hora de Interés 10:45 AM a 2:45 PM
    inicio_ventana_interes = 7 + 45/60     # Check WeatherUnderground
    fin_ventana_interes = 14 + 45/60        # Check WeatherUnderground
    # Pedir el tiempo actual
    now_osc = round(ahora(),4)
    
    if (now_osc > inicio_ventana_interes) and (now_osc < fin_ventana_interes):
        HR = 1
    else:
        HR = 0
    return HR

def BATT_OSC(BATT_POW):                     # Obtener el Flag "BATT" del OSC
    if BATT_POW >= 5:                        # Maxima potencia seleccionada
        BATT = 1
    else:
        BATT = 0
    return BATT

def VAC_OSC(VAC_V):                              #Obtener el Flag "VAC" del OSC
    if VAC_V > 100:
        VAC = 1
    else:
        VAC = 0
    return VAC


class arbolDecis:
	def __init__(self):
		self.myController = Controller(firstState())
		print("INICIO DEL ARBOL DE DECISION")
		self.myController.presentState()

	def tomar_decision(self, BATT_F, VAC_OS):
		HR_OS = HR_OSC()
		BATT_OS = BATT_OSC(BATT_F)
		if(self.myController.returnState()==1):
			if (VAC_OS == 0):
				if (BATT_F==1):
				    self.myController.goTo3()
				else:
					if HR_OS == 1:
					    self.myController.goTo2()
					else:
					    self.myController.goTo1()
			else:
				if HR_OS == 1:
				    self.myController.goTo2()
				else:
				    self.myController.goTo4()
		elif(self.myController.returnState()==2):
		    if BATT_OS == 1:
		        self.myController.goTo1()
		    else:
		        self.myController.goTo2()
		elif (self.myController.returnState()==3):
		    if BATT_OS == 1:
		        self.myController.goTo3()
		    else:
		        self.myController.goTo1()
		else:
		    if BATT_OS == 1:
		        self.myController.goTo1()
		    else:
		        self.myController.goTo4()		
		