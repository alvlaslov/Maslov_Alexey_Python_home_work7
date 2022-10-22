import data_generation as dg
import user_interface as ui
import logger as lg
import controller
import os.path

if not os.path.exists('contacts.csv'):
    dg.get_contacts()
lg.write_log('Open the directory')
controller.init_data_base('contacts.csv')
ui.ls_directory()