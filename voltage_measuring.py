# Corresponding code part from Arduino IDE
"""
#include <mcp342x.h> # import library
MCP342X adc;

nplc = 1  # assign NPLC variable to 1 or 5 or 10
int potPin = A0  # analog port A0 read data from potentiometer
int potVal;  # variable for storing data from potPin port
int DL = 100;  # delay time in ms between readings
void setup() {
    adc.begin();  # Initialize the ADC
    adc.setNPLC(nplc);  # set NPLC
    pinMode(potPin, INPUT);  # set working mode for port - Input data
    Serial.begin(115200);  # set baud rate for data transfer - 14400 byte or 9600
}

void loop() {
    potVal=analogRead(potPin);  # write measured values from potPin to potVal variable
    Serial.print(potVal); # send data from potVal to print from new line
    Serial.println(“,”);
    Serial.println(nplc);
    delay(DL);  # set delay time equal to DL variable
"""


import time
import serial
arduinoData = serial.Serial("com3", "115200")  # creating an object to read data from.
# With respective port and same baud rate we use in Arduino IDE

time.sleep(1)  # set timer to give some time for com port to initialize
max_binary = 1023  # max binary value from arduino ADC
set_voltage = 3.3  # max voltage readings for our case
voltage_conversion_coefficient = 3.3 / (1023 + 1)  # adding one as count starts from 0 

while True:  # reading data from serial port
    while arduinoData.in_waiting == 0:  # checking if there is any data on the port
        pass
    dataPacket = arduinoData.readline()  # reading data from port if there is some
    dataPacket = str(dataPacket, "utf-8")  # get voltage binary readings
    dataPacket = dataPacket.rstrip("\r\n")  # get rid of new lines we should delete carriage and \n
    dataPacket.split(",")  # get list of string values (voltage and NPLC)
    voltage_data = int(dataPacket[0])  # get binary voltage data
    NPLC_data = int(dataPacket[1])  # get NPLC settings
    voltage = voltage_data * voltage_conversion_coefficient  # convert readings from binary to volts
    voltage = round(voltage, 3)  # round answer to 3 digits after coma
    print(f"{voltage} v    NPLC-{NPLC_data}")  # output in convenient format
