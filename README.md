# FuzzyLogicProj
Position control system for a motor DC

## Funcionamiento
El archivo main.py es el que se ejecuta en la ESP32, el código es micropython ¡NO SE EJECUTA EN LA PC!, se ejecuta escribiendo en la terminal:
- ampy --port (puerto com en donde se encuentre conectada la ESP32, ej: com6) put main.py 
- ampy --port (puerto com en donde se encuentre conectada la ESP32, ej: com6) run main.py

El archivo project1.py es el que se ejecuta en la PC, se debe de tener conectado tanto el esp32 como el USB A TTL.
La ejecución mostrara el valor de los puertos ADC y el valor de voltaje que se generara con la señal PWM.

Antes de ejecutar el código instala las librerías requeridas para su ejecución con la siguiente línea:
- pip install -r requirements.txt
