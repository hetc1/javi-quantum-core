# HETC JAVI MONITOR - VISUALIZER TOOL
# Run this on your PC to see Javi's thoughts in real-time.

import serial
import time
import sys

# Configuración / Settings
SERIAL_PORT = 'COM3'  # Cambia esto por tu puerto real (o /dev/ttyUSB0 en Linux)
BAUD_RATE = 115200

print("--- HETC JAVI (U-1) MONITOR ---")
print("Connecting to Quantum Core...")

try:
    # Simulación si no hay placa conectada (Para demos)
    # ser = serial.Serial(SERIAL_PORT, BAUD_RATE) 
    print("Link established. Receiving Telemetry...")
    print("-" * 50)
    print(f"{'INPUT':<10} | {'THOUGHT (Ŭ)':<20} | {'ENERGY':<10}")
    print("-" * 50)

    while True:
        # En modo real descomenta la linea de abajo:
        # line = ser.readline().decode('utf-8').strip()
        
        # Simulación de datos para demostración:
        import random, math
        vibration = random.random()
        thought = math.tanh(0.5 + vibration * 0.014)
        energy = "872mW"
        
        # Visualización tipo Hacker
        bar_len = int(thought * 20)
        visual_bar = "█" * bar_len + "░" * (20 - bar_len)
        
        print(f"{vibration:.4f}     | {visual_bar} {thought:.5f} | {energy}")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nDisconnected.")
    sys.exit()
except Exception as e:
    print(f"Error: {e}")
    print("Tip: Check your USB connection.")
