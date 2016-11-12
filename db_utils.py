import psycopg2
import pandas as pd
import peewee
from dbmodel import *
from sqlalchemy import create_engine
import config

def map_to_db(mls_df):
    ################################################
    # Uses a pandas dataframe to load information  #
    # into the postgres mls database               #
    ################################################


    mls_df['']

def load_db(csv_file):

    ######################################################################

    #    Function load_db(csv_file) <-- csv file with full path          #
    #    -----------------------------------------------------------     #
    #    Loads csv into database using pandas dataframe                  #

    #        csv_file: full path to csv file that will be loaded         #

    #        - load csv into pandas dataframe                            #
    #        - check for redundant property entries _redundant_record()  #
    #            -- use _update_property(prop_id, df) to update db then  #
    #                return new df with entry removed                    #
    #        - get last prop_id & append to dataframe                    #

    ######################################################################

    #Setup connection to DB using info pulled from config
    post_engine = config.get_post_engine()
    engine = create_engine(post_engine)

    #Read CSV file into dataframe
    df = pd.read_table(csv_file)

    #Get list of addresses from dataframe
    new_df_addr = df.concat(
            [
                df['StreetName'],
                df['StreetNum'],
                df['ZipCode'], axis=1,
                keys=['streetname', 'streetnum', 'zipcode']
            ]
        )

    db_df_addr = pd.read_sql(
            'SELECT streetnum, streetname, zipcode FROM physicaladdr', engine)
        )

    #Find any duplicates within existing database
    non_dup_df = (new_df_addr.streetnum.isin(db_df_addr.streetnum) &
        new_df_addr.streetname.isin(db_df_addr.streetname))

    dups = []
    for a in non_dup_df.iteritems():
        if a[1] == True:
            dups.append(0)

    #Pop out the duplicates
    non_dup_df = df
    for a_dup in dups:
        non_dup_df.drop(non_dup_df.index[a_dup])

    #Get last property_id from property table
    prop_id = get_last_prop_id(engine)

    #Commit net new entries
    non_dup_df.to_sql()
    df_to_sql = non_dup_df.concat(
        [


        ]


    )
    #Update old entries




def get_last_prop_id(engine):
    props = pd.read_sql('SELECT property_id FROM property', engine)
    property_id = 1 + (props.iloc[-1:].index[0])
    return property_id

def _records_to_update(tbl_name, engine, field, value):

    #Set a dataframe based on table
    df = pd.read_sql('SELECT ' + field +' FROM ' + tbl_name, engine)

    #Determine if field / value are part of dataframe
    if df.Series.str.contains(value)[0]:
        return
    else:
        return False


def _update_existing(prop_id, df):
    pass

def make_table_mappings():
    
