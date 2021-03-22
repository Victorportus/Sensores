# Se crea codigo para poder leer la informacion de sensor de temperatura y humedad DHT22 leyendolo desde Raspberry pi 4.
# Se conetcta al pin 7 GPIO4 de la board.
# Se usa repositorio adafruit para poder leer la informacion del sensor. Esta debe ser instalada desde consola "sudo pip3 install adafruit-circuitpython-dht"

# El sensor DHT22, prporciona datos de tiempo y temperatura cada 2 segundos, por esto se debe dar un delay de teimpo para que no genere errores
import time
# Para leer los datos de sistema de un archivo exixstente deemos importar la libreria de os
import os
import board
import adafruit_dht
# Para poder interactuar con archivos .csv se debe importar esta libreria
import csv

# Se establece coneccion con el dispositivo, el cual esta conectado al pin GPIO4
dhtDevice = adafruit_dht.DHT22(board.D4)



# Se mira el tamano del archivo, en caso de que sea 0, se almacenan los datos de informacion de la tabla
header = ["Date","Time","Temperature","Humidity"]
f = open("data.csv", 'a')
writer = csv.writer(f)
if os.stat("data.csv").st_size == 0:
    writer.writerow(header)
f.close()



i = 0
while i < 10:
    try: 
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        data = (time.strftime("%m/%d/%y"), time.strftime("%H:%M"), temperature_c, humidity)
        f = open("data.csv", 'a')
        writer = csv.writer(f)
        writer.writerow(data)
        f.close()
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        
    time.sleep(2.0)

    i = i+1


f = open("data.csv", "r")
print(f.read())


dhtDevice.exit()

