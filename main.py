from functions import *

mod_filenames = 'norway_monuments'
mod_version = '1.0'
mod_name = 'Monuments of aaa'
game_version = '1.32.2.0'
file_id = 2540783390
#remember to put in pictures and thumbnail

if __name__ == '__main__':
    f = open('monuments.csv', 'r')
    monuments_raw = []
    for x in f:
        monuments_raw.append(x.split(';'))

    monuments = raw_to_dicts(monuments_raw)
    write_files(mod_name, monuments)
    descriptor_file(mod_version, mod_name, game_version, file_id)