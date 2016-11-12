import sys
import config
import mech_it
import db_utils

def main(*args, **kwargs):

    ######################################################################
    #                        MLS DATA LOAD                               #
    #   -----------------------------------------------------------      #
    #       Program will load info from downloaded MLS data  into DB     #
    #    -----------------------------------------------------------     #

    #        * Pull info using mech_it.mls_data()                        #
    #        * Load information into Postgress database                  #
    #              db_utils.load_db(csv_file)                            #
    ######################################################################

    #Pull config information from config.py
    config_info = {
            'l_url': config.get_l_url(),
            'q_url': config.get_q_url(),
            'cs_url': config.get_cs_url(),
            'user': config.get_user(),
            'password': config.get_password(),
            'folder_out': config.get_folder_out(),
        }

    #Get mls data using mech_it
    mech_it.get_mls_data(config_info)

    ''' ToDo -- add filename pull '''

    #Load data into database
    db_utils.load_db(filename)

if __name__ == '__main__':
    main()
