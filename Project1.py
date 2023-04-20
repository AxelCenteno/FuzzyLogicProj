import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
import collections
import P1_Centeno_Monzalvo as P1
import skfuzzy as fuzz
import serial
import time

serialPort = "COM6"
baudRate = 115200

try:
    ser = serial.Serial(serialPort, baudRate)
except:
    print("Failed to connect on " + str(serialPort))

def obtener_centroide(M,R):
    reference = np.arange(0,360,1)
    motor = np.arange(0,360,1)
    voltage = np.arange(-5,5.1,0.1)

    inicio_R = P1.Trapezoidal(reference,0,0,45,135)
    medio_R = P1.Trapezoidal(reference,90,135,215,270)
    final_R = P1.Trapezoidal(reference,215,270,359,359)

    inicio_M = P1.Trapezoidal(motor,0,0,45,135)
    medio_M = P1.Trapezoidal(motor,90,135,215,270)
    final_M = P1.Trapezoidal(motor,215,270,359,359)

    positive = P1.Triangular(voltage,0,5,5)
    zero = P1.Triangular(voltage,-2.5,0,2.5)
    negative = P1.Triangular(voltage,-5,-5,0)

    rule1 = np.fmin(inicio_R[R],inicio_M[M])
    rule2 = np.fmin(inicio_R[R],medio_M[M])
    rule3 = np.fmin(inicio_R[R],final_M[M])
    rule4 = np.fmin(medio_R[R],inicio_M[M])
    rule5 = np.fmin(medio_R[R],medio_M[M])
    rule6 = np.fmin(medio_R[R],final_M[M])
    rule7 = np.fmin(final_R[R],inicio_M[M])
    rule8 = np.fmin(final_R[R],medio_M[M])
    rule9 = np.fmin(final_R[R],final_M[M])

    positive_rule = np.fmax(rule2,np.fmax(rule3,rule6))
    zero_rule = np.fmax(rule1,np.fmax(rule5,rule9))
    negative_rule = np.fmax(rule4,np.fmax(rule7,rule8))

    cut_positive = np.fmin(positive, np.full(len(positive), positive_rule))
    cut_zero = np.fmin(zero, np.full(len(zero), zero_rule))
    cut_negative = np.fmin(negative, np.full(len(negative), negative_rule))

    finalcut = np.fmax(cut_positive, np.fmax(cut_zero, cut_negative))

    centroid = fuzz.defuzz(voltage,finalcut,'centroid')
    return centroid

def getSerialData(self, samples, numData, serialConnection, lines):
    for i in range(numData):
       value = float(serialConnection.readline().strip())
       data[i].append(value/4096*3.3)
       lines[i].set_data(range(Samples),data[i])

Samples = 500
sampleTime = 10
numData = 2

xmin = 0
xmax = Samples
ymin = 0
ymax = 360
lines = []
data = []

for i in range(numData):
   data.append(collections.deque([0]*Samples, maxlen=Samples))
   lines.append(Line2D([],[],color='blue'))

fig = plt.figure()
ax1 = fig.add_subplot(211, xlim=(xmin, xmax), ylim=(ymin, ymax))
ax1.set_title('Motor')
ax1.set_xlabel('Samples')
ax1.set_ylabel('Grados')
ax1.grid()
ax1.add_line(lines[0])

ax2 = fig.add_subplot(212, xlim=(xmin, xmax), ylim=(ymin, ymax))
ax2.set_title('Referencia')
ax2.set_xlabel('Samples')
ax2.set_ylabel('Grados')
ax2.grid()
ax2.add_line(lines[1])

anim = animation.FuncAnimation(fig, getSerialData, fargs=(Samples, numData, ser, lines), interval=sampleTime)
plt.show()

ser.close()

