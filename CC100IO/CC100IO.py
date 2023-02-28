# Created by Konrad Holsmölle
# konrad.holsmoelle@wago.com

# Modified by Sascha Hahn, Bjarne Zaremba
# sascha.hahn@wago.com
# bjarne.zaermba@wago.com

# Control of input and output from https://github.com/WAGO/cc100-howtos/blob/main/HowTo_Access_Onboard_IO/accessIO_CC100.py

import Cal
import logging
from enum import Enum

# Enum Types for the inputs and outputs:
DigitalOutputs = Enum("", ["DO1", "DO2", "DO3" , "DO4"])
DO1 = DigitalOutputs.DO1
DO2 = DigitalOutputs.DO2
DO3 = DigitalOutputs.DO3
DO4 = DigitalOutputs.DO4

DigitalInputs = Enum("", ["DI1", "DI2", "DI3" , "DI4" , "DI5" , "DI6" , "DI7" , "DI8"])
DI1 = DigitalInputs.DI1
DI2 = DigitalInputs.DI2
DI3 = DigitalInputs.DI3
DI4 = DigitalInputs.DI4
DI5 = DigitalInputs.DI5
DI6 = DigitalInputs.DI6
DI7 = DigitalInputs.DI7
DI8 = DigitalInputs.DI8

AnalogOutputs = Enum("", ["AO1", "AO2"])
AO1 = AnalogOutputs.AO1
AO2 = AnalogOutputs.AO2

AnalogInputs = Enum("", ["AI1", "AI2"])
AI1 = AnalogInputs.AI1
AI2 = AnalogInputs.AI2

# Functions to control and read the inputs and outputs.
def digitalWrite(output: DigitalOutputs, value: bool):
    """
    value: Value which the selected output should be set to
    output: Digital output to be switched

    Function switches the output to the specified value.
    Function does not check the current value of the output
    Function returns True when value is written, returns False when an Error occured
    """

    # Check if the type of the input is correct
    if(type(output) == DigitalOutputs & type(value) == bool):

        # Changing value to the desired Integer
        if output == DO1:
            output = 1
        elif output == DO2:
            output = 2
        elif output == DO3:
            output = 3
        elif output == DO4:
            output = 4

        # Reading the outputs current state to calculate the new value in the file
        path ="/home/ea/dout/DOUT_DATA"
        file = open(path, "r")
        currentValue = int(file.read())
        file.close()

        # Addition or rather subtraction to the current state to switch the corresponding output
        # Least Significant Bit corresponds to digital output 1, the 4th bit corresponds to output 8
        # A number from 0 to 15 is written to the file
        if output == 1:
            if value:
                currentValue += 1
            else:
                currentValue -= 1
        elif output == 2:
            if value:
                currentValue += 2
            else:
                currentValue -= 2
        elif output == 3:
            if value:
                currentValue += 4
            else:
                currentValue -= 4
        elif output == 4:
            if value:
                currentValue += 8
            else:
                currentValue -= 8

        # Writes the calculated value for the new configuration to the file on the CC100
        file = open(path, "w")
        file.write(str(currentValue))
        file.close()
        # Returns True after completion
        return True
    else:
        logging.warning("output is not of type DigitalOutputs or value is not of type bool")
        return False

def analogWrite(output: AnalogOutputs, voltage: int):
    """
    voltage: Voltage which the selected output should be set to
    output: Analog output to be switched

    Function switches the output to the specified voltage
    Function does not check the current value of the output
    Function returns True wenn value is written, returns False when an Error occured
    """
    # Check if the type of the input and voltage is correct
    if(type(output) == AnalogOutputs & type(voltage) == int):

        # Check if voltage is in the range of 0 to 10000
        if(voltage >= 0 & voltage <= 10000):

            # Changing voltage to the desired Integer
            if output == AO1:
                output = 1
            elif output == AO2:
                output = 2
            

            # Calibration with Cal.py
            voltage = Cal.calibrateOut(voltage, output)
            if voltage < 0:
                voltage = 0

            # Activates the analog outputs on the CC100 by writing
            # Temporary: What is this for????'###############################################################################
            #################################################################################################################

            path = "/home/ea/anout/40017000.dac:dac@1/iio:device0/out_voltage1_powerdown"
            file = open(path, "w")
            file.write("0")
            file.close()

            path = "/home/ea/anout/40017000.dac:dac@2/iio:device1/out_voltage2_powerdown"
            file = open(path, "w")
            file.write("0")
            file.close()

            # Writes the voltage, taken from the calibration for the corresponding output,
            # for the voltage to the file for the output
            # When turning off, a zero is written to the file
            if output == 1:
                path="/home/ea/anout/40017000.dac:dac@1/iio:device0/out_voltage1_raw"
                file = open(path, "w")
                file.write(str(voltage))
                file.close()

            elif output == 2:
                path="/home/ea/anout/40017000.dac:dac@2/iio:device1/out_voltage2_raw"
                file=open(path, "w")
                file.write(str(voltage))
                file.close()
            
            # Returns True after completion
            return True

        else:
            logging.warning("voltege is not in the range of 0 to 10000")
            return False
    else:
        logging.warning("output is not of type AnalogOutputs or voltage is not of type int")
        return False

def digitalRead(input: DigitalInputs):
    """
    input: Digital input to be switched

    Function reads the input
    Function does not check the current value of the output
    Returns True or False depending on the value
    """

    # Check if the type of the input is correct
    if(type(input) == DigitalInputs):

        # Changing input to the desired Integer
        if input == DI1:
            input = 1
        if input == DI2:
            input = 2
        if input == DI3:
            input = 3
        if input == DI4:
            input = 4
        if input == DI5:
            input = 5
        if input == DI6:
            input = 6
        if input == DI7:
            input = 7
        if input == DI8:
            input = 8
        
        # Reads the state of the digital inputs on the CC100
        path = "/home/ea/din/din"
        datei = open (path, "r")
        value = datei.readline()
        datei.close()

        # Formats the current state into an 8-digit binary code
        value = int(value)
        value0B = format(value, "08b")
        
        # Calculates the position of the bit from the desired input
        inputBit = 8 - input

        # Returns the value of the state of the desired input
        # Note: Last index(read from left to right) is the Least Significant Bit.
        if int(value0B[inputBit]) == 1:
            return True
        else:
            return False
    else:
	    raise TypeError("output is not of type DigitalInputs")


def analogRead(input: AnalogInputs):
    """
    input: Analog input to be switched

    Function reads the input and returns the calibrated value in mV as an Integer.
    """

    # Check if the type of the input is correct
    if(type(input) == AnalogInputs):

        # Changing input to the desired Integer
        if input == AI1:
            input = 1
        elif input == AI2:
            input = 2

        # Reads the state of the analog input on the CC100
        if input == 1:
            path="/home/ea/anin/48003000.adc:adc@100/iio:device3/in_voltage3_raw"
        elif input == 2:
            path="/home/ea/anin/48003000.adc:adc@100/iio:device3/in_voltage0_raw"

        file = open(path, "r")
        voltage = int(file.readline())
        file.close()

        # Calibrates the value and returns it
        return(Cal.calibrateIn(voltage, input))
    else:
	    raise TypeError("iEingang is not of type AnalogInputs")

def digitalReadWait(input: DigitalInputs, value: bool):
    """
    input: Digital input to be checked
    value: State to be queried at the input

    Reads the specified input until the desired state is reached,
    by another Function or external factors and then returns True
    Function runs until the state is reached.
    """

    # Check if the type of the input is correct
    if(type(input) == DigitalInputs & type(value) == bool):

        # Changing output to the desired Integer
        if input == DI1:
            input = 1
        if input == DI2:
            input = 2
        if input == DI3:
            input = 3
        if input == DI4:
            input = 4
        if input == DI5:
            input = 5
        if input == DI6:
            input = 6
        if input == DI7:
            input = 7
        if input == DI8:
            input = 8

        # Converts the given bool into a number
        if value:
            value = 1
        else:
            value = 0

        # Checks the input as long as it reaches the given state
        # Then ends the loop and returns True
        eingangSchleife = True
        while eingangSchleife:
            if digitalRead(input) == value:
                eingangSchleife = False
                return True
    else:
	    raise TypeError("input is not of type DigitalInputs")
