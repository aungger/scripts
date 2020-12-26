# 96 wells plate
# 96 wells 1 - 12 (columns) a-h (rows)
# show the 96 well plates, with x's on the used wells (lina will pick which well she so desires)
# sometimes lina will have to run multiple 96 plates, to reduce stress/time she would request to multiple the results because she is unable to do math
# stains constant 1/200
# PI constant 1/400

# Lina will speificy volume with the same units (micro liter -> ul)
# 1000 microliters = 1ml -> when volume is over 1000 convert it to ml's for lina's
# number = volume * number of wells lina specifies -> give this number to lina
# number * either stain or PI constant -> give this number to lina

STAINS = 0.005;
PI = 0.0025;
ROWS = ['label', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];

def stainsConversion (plateVolume):
    value = plateVolume * STAINS;
    print('\nStains: ' + str(value) + '\n');

def piConversion (plateVolume):
    value = plateVolume * PI;
    print('\nPI: ' + str(value) + '\n');

def getUnits (plateVolume):
    if(plateVolume >= 1000):
        value = plateVolume/1000;
        return str(value) + ' ml';
    else:
        return 'ul';

def makePlates ():
    for char in ROWS:
        for entry in range (0, 13):
            if(char == 'label'):
                print('\t| ' + str(entry) + ' |'),;
                if(entry == 12):
                    print('\n');
            else:
                if(entry == 0):
                    print('\t| ' + char + ' |'),;
                elif(entry == 12):
                    print('\t| x |'),;
                    print('\n');
                else:
                    print('\t| x |'),;

makePlates();
volume = raw_input('\nWell volume (ul): ');
wells = raw_input('Number of wells: ');
plateVolume = int(volume) * int(wells); # add decimals?
getUnits = getUnits(plateVolume);
print('\nplate Volume: ' + str(plateVolume) + ' (' + getUnits + ') '+ '\n');

stainsOrPI = raw_input('Stains or PI or Both (1: stains, 2: PI, 3 both): '); # add forloop so if lina enters wrong key she doesn't have to start over....
if(stainsOrPI == str(1)):
    stainsConversion(plateVolume);
elif(stainsOrPI == str(2)):
    piConversion(plateVolume);
elif(stainsOrPI == str(3)):
    stainsConversion(plateVolume);
    piConversion(plateVolume);
else:
    print('wrong input');
