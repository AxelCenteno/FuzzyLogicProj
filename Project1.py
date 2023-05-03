import numpy as np
import skfuzzy as fuzz
import serial
import time


serialPort = "COM6"
serialPort2 = "COM8"
baudRate = 115200

try:
    ser = serial.Serial(serialPort, baudRate)
    print("Connected to " + str(serialPort))
except:
    print("Failed to connect on " + str(serialPort))

try:
    ser2 = serial.Serial(serialPort2, baudRate)
    print("Connected to " + str(serialPort2))
except:
    print("Failed to connect on " + str(serialPort2))

reference = np.linspace(0, 359, 360)
motor = np.linspace(0, 359, 360)
voltage = np.linspace(-5, 5, 101)
print(voltage[-1])

# Definir funciones de membresía difusas
inicio_R = fuzz.trapmf(reference, [0, 0, 90, 180])
medio_R = fuzz.trimf(reference, [90, 180, 270])
final_R = fuzz.trapmf(reference, [180, 270, 359, 359])

inicio_M = fuzz.trapmf(motor, [0, 0, 90, 180])
medio_M = fuzz.trimf(motor, [90, 180, 270])
final_M = fuzz.trapmf(motor, [180, 270, 359, 359])

positive_mf = fuzz.trapmf(voltage, [0, 2, 5, 5])
zero_mf = fuzz.trimf(voltage, [-2, 0, 2])
negative_mf = fuzz.trapmf(voltage, [-5, -5, -2, 0])

def obtener_centroide(M,R):
    # Calcular reglas difusas
    rule1 = np.fmin(inicio_R[R], inicio_M[M])
    rule2 = np.fmin(inicio_R[R], medio_M[M])
    rule3 = np.fmin(inicio_R[R], final_M[M])
    rule4 = np.fmin(medio_R[R], inicio_M[M])
    rule5 = np.fmin(medio_R[R], medio_M[M])
    rule6 = np.fmin(medio_R[R], final_M[M])
    rule7 = np.fmin(final_R[R], inicio_M[M])
    rule8 = np.fmin(final_R[R], medio_M[M])
    rule9 = np.fmin(final_R[R], final_M[M])

    # Calcular conjuntos difusos cortados
    cut_positive = np.fmin(positive_mf, np.fmax(np.fmax(rule2, rule3), rule6))
    cut_zero = np.fmin(zero_mf, np.fmax(np.fmax(rule1, rule5), rule9))
    cut_negative = np.fmin(negative_mf, np.fmax(np.fmax(rule4, rule7), rule8))

    # Combinar conjuntos difusos cortados
    finalcut = np.fmax(cut_positive, np.fmax(cut_zero, cut_negative))

    # Calcular centroide del conjunto difuso resultante
    centroid = fuzz.defuzz(voltage, finalcut, 'centroid')
    return centroid

def getSerialData(self):
    if self[0].inWaiting() > 0:
        try: 
            [M,R] = self[0].readline().strip().decode('utf-8').split(',')
        except:
            [M,R] = [0,0]
        centroid = (round(obtener_centroide(int(M),int(R)),3))
        ser2.write(str(centroid).encode('utf-8'))
        print(M,R)
        print(centroid)
    else:
        print("No data")

if __name__ == "__main__":
    for i in range(1000):
        getSerialData([ser,ser2])
        time.sleep(0.1)
    ser.close()
    time.sleep(2)

# Cerrar comunicación serial

 
    