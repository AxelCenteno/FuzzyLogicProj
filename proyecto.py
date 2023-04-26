from machine import Pin, ADC, UART
import time

# Crear instancia de ADC
motor = ADC(Pin(36))
reference = ADC(Pin(39))

uart = UART(0, 9600) #Configurar UART en el puerto 0 con una velocidad de 115200 baudios
i=0
while i < 1000:
    # Leer el valor del ADC
    valor_motor = motor.read()
    valor_reference = reference.read()

    # Imprimir el valor leído
    print(int(valor_motor/11.4) ,",", int(valor_reference/11.4))

    time.sleep(0.1)
    i += 1