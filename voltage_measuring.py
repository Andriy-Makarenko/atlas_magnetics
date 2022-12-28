import time
import serial
arduinoData = serial.Serial("com3", "115200")  # creating an object to read data from.
# With respective port Arduino connected to from Arduino IDE settings and same baud rate as we use in Arduino

time.sleep(1)  # set timer to give some time for com port to initialize
max_binary = 1023  # max binary value from arduino potentiometer
set_voltage = 3.3  # max power output for our case of the arduino board
voltage_conversion_coefficient = 3.3 / (1023 + 1)  # adding one as count starts from 0 

while True:  # reading data from serial port
    while arduinoData.in_waiting == 0:  # checking if there is any data on the port
        pass
    dataPacket = arduinoData.readline()  # reading data from port if there is some
    dataPacket = str(dataPacket, "utf-8")  # get voltage binary readings
    dataPacket = dataPacket.rstrip("\r\n")  # get rid of new lines we should delete carriage and
    dataPacket.split(",")  # get list of string values (voltage and NPLC)
    voltage_data = int(dataPacket[0])  # get binary voltage data
    NPLC_data = int(dataPacket[1])  # get NPLC settings
    voltage = voltage_data * voltage_conversion_coefficient  # convert readings from binary to volts
    voltage = round(voltage, 3)  # round answer to 3 digits after coma
    print(f"{voltage} v    NPLC-{NPLC}")  # now looks like  we want to get only readings
