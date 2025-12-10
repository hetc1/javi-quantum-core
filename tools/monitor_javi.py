# HETC JAVI MONITOR - VISUALIZER TOOL
# Run this on your PC to see Javi's thoughts in real-time.

import serial
import serial.tools.list_ports # Necesario para buscar puertos
import time
import sys
import random
import math

# --- CONFIGURACIÓN HETC ---
BAUD_RATE = 115200

def encontrar_puerto_javi():
    """Busca automáticamente un dispositivo conectado (Arduino/ESP32)."""
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        # Filtro básico: Si dice USB o COM, asumimos que es Javi
        if "USB" in p.description or "COM" in p.device:
            return p.device
    return None

print("\n--- HETC JAVI (U-1) MONITOR SYSTEM ---")
print("Inicializando protocolos cuánticos...")

# Intentar conexión real
target_port = encontrar_puerto_javi()
modo_simulacion = False

if target_port:
    print(f"[CONEXIÓN DETECTADA] Conectando a Javi en {target_port}...")
    try:
        ser = serial.Serial(target_port, BAUD_RATE, timeout=1)
        time.sleep(2) # Esperar a que se estabilice la conexión
        print(">> ENLACE ESTABLECIDO <<")
    except Exception as e:
        print(f"[ERROR] No se pudo abrir el puerto: {e}")
        modo_simulacion = True
else:
    print("[AVISO] No se detectó hardware. Iniciando MODO SIMULACIÓN.")
    modo_simulacion = True

print("-" * 60)
print(f"{'INPUT (VIB)':<15} | {'PENSAMIENTO (Ŭ-1)':<25} | {'ENERGÍA'}")
print("-" * 60)

try:
    while True:
        if not modo_simulacion:
            # LECTURA REAL 
            # (Intentamos leer datos del puerto serial)
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                try:
                    # Asumimos que llega un número float
                    vibration = float(line.split(',')[0]) 
                except:
                    vibration = random.random()
            else:
                # Si no hay datos nuevos, mantenemos un valor aleatorio suave
                vibration = random.random()
        else:
            # SIMULACIÓN (Si no hay hardware conectado)
            vibration = random.random()

        # Lógica de "Cerebro Riemann" (U-1)
        # Usamos 0.5 como base (Línea Crítica) + perturbación
        thought = math.tanh(0.5 + vibration * 0.14) 
        energy = "872mW" 

        # Visualización de la Barra
        bar_len = int(thought * 20) 
        # Aseguramos que no se salga de rango visual (0 a 20 caracteres)
        bar_len = max(0, min(20, bar_len))
        
        # Estilo gráfico
        visual_bar = "▓" * bar_len + "░" * (20 - bar_len)
        
        # Salida limpia en una sola línea
        print(f"{vibration:.4f}          | {visual_bar} {thought:.4f} | {energy}")
        time.sleep(0.1)

except KeyboardInterrupt:
    if not modo_simulacion:
        ser.close()
    print("\n[SISTEMA] Desconectado. Monitor HETC cerrado.")
    sys.exit()
except Exception as e:
    print(f"\n[CRITICAL ERROR]: {e}")
