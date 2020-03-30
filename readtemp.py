import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_files = glob.glob(base_dir + '28*' + '/w1_slave')


def read_temp_raw(folder):
    f = open(folder, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp(folder):
    lines = read_temp_raw(folder)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        #        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c


while True:
    for index, device_file in enumerate(device_files):
        print('SENSOR: ' + str(index) + '  ' + str(read_temp(device_file)))
    print('\n')
    time.sleep(1)
