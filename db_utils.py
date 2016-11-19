import psycopg2
import pandas as pd
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.automap import automap_base
import config
import json

def map_to_db(mls_df):
    ################################################
    # Uses a pandas dataframe to load information  #
    # into the postgres mls database               #
    ################################################


    mls_df['']

def load_db(csv_file):

    '''###################################################################

    #    Function load_db(csv_file) <-- csv file with full path          #
    #    -----------------------------------------------------------     #
    #    Loads csv into database using pandas dataframe                  #

    #        csv_file: full path to csv file that will be loaded         #

    #        - load csv into pandas dataframe                            #
    #        - check for redundant property entries _redundant_record()  #
    #            -- use _update_property(prop_id, df) to update db then  #
    #                return new df with entry removed                    #
    #        - get last prop_id & append to dataframe                    #

    ###################################################################'''

    #Setup connection to DB using info pulled from config
    post_engine = config.get_post_engine()
    engine = create_engine(post_engine)

    #SQLAlchemy setup base
    Base = automap_base()
    Base.prepare(engine, reflect=True)

    #Create dictionary of classes
    tbl_class = _create_class_dict(Base.classes)

    #Read CSV file into dataframe
    df = pd.read_table(csv_file)

    #Get list of addresses from dataframe
    non_dup_df = _find_duplicate_records(df, engine)

    #Get last property_id from property table
    prop_id = get_last_prop_id(engine)

    #Commit net new entries
    non_dup_df.to_sql()
    df_to_sql = non_dup_df.concat(
            []
        )
    #Update old entries

    #Create dataframe for each table
    with open('table_mapping.json') as table_mapping:
        all_tables = json.load(table_mapping)
        for table in all_tables.items():
            table = pd.dataframe()


def _get_create_pkid(to, s, q_field, q_str, t_pk):
    ######################################################################

    #    Function _get_create_pkid - gets primary key of table from      #
    #                                field being queried                 #
    #    -----------------------------------------------------------     #
    #    Inputs: to = tableobject instantiaed from SQLAlchemy classes    #
    #            s = SQLAlchemy session                                  #
    #            q_field = query field / table column to search on       #
    #            q_str = the record you are looking for                  #
    #            t_pk = name of the table primary key                    #
    #    Returns: primary key id of record                               #

    ######################################################################
    q_dict = {q_field: q_str}
    q_it = (
            s.query(getattr(to, q_field)).
            filter(getattr(to, q_field) == q_str).first()
        )

    if q_it:
        c_id = s.query(to).filter_by(**q_dict).first()
        return getattr(c_id, t_pk)
    else:
        c_id = _get_last_id(s,to,t_pk) + 1
        q_dict[t_pk] = c_id
        add_it = to(**q_dict)
        s.add(add_it)
        s.commit()
        return c_id

def _create_class_dict(groupofclasses):
    ######################################################################

    #    Function _create_class_dict <-- Base.classes input              #
    #    -----------------------------------------------------------     #
    #    Takes group of base classes from SQLAlchemy automap             #
    #    returns a dictionary with a entry for table name and            #
    #    a instanstiated class                                           #

    ######################################################################
	a_dict = {}
	for a_class in groupofclasses:
		a_dict[a_class.__table__.name] = a_class
	return a_dict

def _find_duplicate_records(df, engine):
    ######################################################################

    #    Function _find_duplicate_records <-- dataframe / engine         #
    #    -----------------------------------------------------------     #
    #    Takes a dataframe and find duplicates within database           #
    #    ***specific to mls database - would need modification***        #
    #    ***for re-use                                        ***        #

    ######################################################################

    #Set new dataframe by concat of existing
    new_df_addr = df.concat(
            [
                df['StreetName'],
                df['StreetNum'],
                df['ZipCode'], axis=1,
                keys=['streetname', 'streetnum', 'zipcode']
            ]
        )

    #Set a new dataframe based on the database table
    db_df_addr = pd.read_sql(
            'SELECT streetnum, streetname, zipcode FROM physicaladdr', engine)
        )

    #Find any duplicates within existing database
    '''ToDo add better searching (ST, Street, all upper etc...)'''

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

    return non_dup_df

def _update_table(tblname, uid_field, linking_id):
    #Update the table with the field from query & prop_id or listing_id
    pass

def _get_last_id(s, to, t_id):
    results = (
            s.execute(s.query(to).filter(
                getattr(to, t_id) == s.query(func.max(
                    getattr(to, t_id)))
            ))
        )
    return results.fetchall()[0][0]

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
