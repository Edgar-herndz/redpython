import nmap
import matplotlib.pyplot as plt
import psutil
from tkinter import Tk, Label, Entry, Button
from datetime import datetime

def scan_ips():
    nm = nmap.PortScanner()
    ip = ip_entry.get()
    nm.scan(hosts=ip, arguments='-sn')
 
    ips = []
    states = []
    bandwidths = []

    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            ips.append(host)
            states.append(nm[host].state())
            bandwidths.append(get_bandwidth(host))

    plot_ips(ips, states, bandwidths)

def get_bandwidth(ip):
    start_time = datetime.now()
    for i in range(1000000):
        # Simulación de operación para medir el ancho de banda
        pass
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    bandwidth = 1000000 / elapsed_time.total_seconds()  # Cálculo del ancho de banda
    return bandwidth

def plot_ips(ips, states, bandwidths):
    colors = {'up': 'green', 'down': 'red', 'unknown': 'gray'}
    bar_colors = [colors[state] for state in states]

    plt.figure(figsize=(12, 6))
    plt.bar(ips, bandwidths, color=bar_colors)
    plt.xlabel('IP')
    plt.ylabel('Ancho de Banda (operaciones/segundo)')
    plt.title('Escaneo de IPs')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Interfaz gráfica
root = Tk()
root.title('Escáner de IPs')

# Etiqueta y campo de entrada para la IP
ip_label = Label(root, text='Introduce la IP:')
ip_label.pack()
ip_entry = Entry(root)
ip_entry.pack()

# Botón para iniciar el escaneo
scan_button = Button(root, text='Escanear', command=scan_ips)
scan_button.pack()

root.mainloop()