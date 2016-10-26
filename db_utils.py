import psycopg2
import pandas as pd
import peewee
from dbmodel import *
import config

def map_to_db(mls_df):
    ################################################
    # Uses a pandas dataframe to load information  #
    # into the postgres mls database               #
    ################################################


    mls_df['']

def load_db(csv_file):

    ####################################################################
    #    Function load_db
    #    -----------------------------------------------------------
    #    Loads csv into database using pandas dataframe

    #        csv_file: full path to csv file that will be loaded

    #        - load csv into pandas a dataframe
    #        - check for redundant property entries _redundant_record()
    #            -- use _update_property(prop_id, df) to update db then
    #                return new df with entry removed
    #        - get last prop_id & append to dataframe

    ####################################################################

def get_last_prop_id():
    post_engine = config.get_post_engine()
    engine = create_engine('')
    props = pd.read_sql('SELECT property_id FROM property', engine)
    property_id = 1 + (props.iloc[-1:].index[0])
    return property_id


def _find_record(tbl_name, info):
    pass

def _update_existing(prop_id, df):
    pass
