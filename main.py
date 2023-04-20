from machine import Pin, ADC, UART
import time

# Crear instancia de ADC
motor = ADC(Pin(36))
reference = ADC(Pin(39))


uart = UART(0, 115200) #Configurar UART en el puerto 0 con una velocidad de 115200 baudios

while True:
    # Leer el valor del ADC
    valor_motor = motor.read()
    valor_reference = reference.read()

    # Imprimir el valor leído
    print(str(int(valor_motor/11.4)))
    print(str(int(valor_reference/11.4)))
    # Esperar un segundo antes de leer nuevamente
    time.sleep(0.1)