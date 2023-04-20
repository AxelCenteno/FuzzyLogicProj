from machine import Pin, ADC
import time

# Crear instancia de ADC
motor = ADC(Pin(36))
reference = ADC(Pin(39))

while True:
    # Leer el valor del ADC
    valor_motor = motor.read()
    valor_reference = reference.read()

    # Imprimir el valor leído
    print(str(valor_motor),",",str(valor_reference))

    # Esperar un segundo antes de leer nuevamente
    time.sleep(0.1)