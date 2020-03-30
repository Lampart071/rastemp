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


while True:
    for index, device_file in enumerate(device_files):
        print('SENSOR: ' + str(index) + '  ' + str(read_temp_raw(device_file)))
    time.sleep(4)
    print('\n')