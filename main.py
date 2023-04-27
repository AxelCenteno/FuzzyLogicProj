from machine import Pin, ADC, UART, PWM
import time

# Crear instancia de ADC
frequency = 5000

motor = ADC(Pin(36)) #Configurar el pin 36 como la referencia ADC del motor
reference = ADC(Pin(39)) #Configurar el pin 39 como la referencia ADC del sensor de referencia
horario = PWM(Pin(2), frequency) #Configurar el pin 2 como salida PWM
a_horario = PWM(Pin(4), frequency) #Configurar el pin 4 como salida PWM
led = Pin(5, Pin.OUT) #Configurar el pin 5 como salida
#led1 = Pin(2, Pin.OUT) #Configurar el pin 2 como salida
#led2 = Pin(4, Pin.OUT) #Configurar el pin 4 como salida
uart = UART(2, 115200) #Configurar UART en el puerto 2 con una velocidad de 115200 baudios


while True:
    # Leer el valor de los ADC
    valor_motor = motor.read()
    valor_reference = reference.read()

    # Imprimir el valor leído para que lo lea la comunicación serial
    print(int(valor_motor/11.4) ,",", int(valor_reference/11.4))
    if uart.any() > 0: #Si hay datos en el UART
        pwm = float(uart.read()) #Leer el dato
        if pwm > 0: #Si el dato es positivo gira sentido horario
            horario.duty(int(1023*pwm/5))
            a_horario.duty(0)
        else: #Si el dato es negativo gira sentido antihorario
            horario.duty(0)
            a_horario.duty(int(-1023*pwm/5))

    time.sleep(0.3) #Esperar 0.1 segundos
