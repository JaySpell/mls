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

    #####################################################################

    #    Function load_db                                               #
    #    -----------------------------------------------------------    #
    #    Loads csv into database using pandas dataframe                 #

    #        csv_file: full path to csv file that will be loaded        #

    #        - load csv into pandas a dataframe                         #
    #        - check for redundant property entries _redundant_record() #
    #            -- use _update_property(prop_id, df) to update db then #
    #                return new df with entry removed                   #
    #        - get last prop_id & append to dataframe                   #

    #####################################################################

    #Setup connection to DB using info pulled from config
    post_engine = config.get_post_engine()
    engine = create_engine(post_engine)

    #Get last property_id from property table
    prop_id = get_last_prop_id(engine)




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

def table_mappings(tblname):
    tables = {
        'property': {
            'fields': [
                'Acres', 'AcresDesc', 'Stories', 'BathsFull', 'BathsHalf',
                'Beds', 'BedsMax',
                    ['Bed1Dim', 'Bed2Dim', 'Bed3Dim', 'Bed4Dim', 'Bed5Dim'],
                'BuilderName', 'CounterTops', 'GarageCap', 'Legal',
                'SqFtBldg', 'LotDim', 'RoomBreakfastDim', 'RoomDenDim',
                'RoomKitchenDim', 'RoomLivingDim', 'RoomMediaDim',
                'RoomFamilyDim'
            ],
            'keys': [
                'acres', 'acresdesc', 'stories', 'bathsfull', 'bathshalf',
                'beds', 'bedsmax', 'beddim', 'buildersname', 'countertops',
                'garagecap', 'legal_addr', 'sqftbuilding', 'lotdim',
                'breakfastdim', 'diningdim', 'dendim', 'kitchendim',
                'livingdim', 'mediadim', 'familydim'
            ]

        },
        'prop_other': {
            'fields': [
                'index', 'GolfCourseName', 'HOAMandatory', 'HOAPhone',
                'HOAWebsite', 'Icemaker', 'Diswasher', 'Compactor',
                'CoolSystem', 'HomePhone', 'InternetAddress',
                'LicensedSupervisor', 'Location', 'ManagementCo', 'MapPage',
                'LotSizeSrc', 'LotValue', 'MaintFeePaySchedule',
                'MasterPlannedCommunity', 'MasterPlannedCommunityYN',
                'Microwave', 'Modified', 'NewConstruction', 'NumCars',
                'NewConstructionDesc', 'PoolArea', 'PoolPrivate',
                'PoolPrivateDesc', 'RoomBedDesc', 'Siding', 'TaxAmount',
                'TaxID', 'TaxRate', 'uid', 'UIDPrp', 'UtilityDistrict',
                'VacationRental', 'YearBuiltSrc', 'YearBuiltFlag',
                'WaterAmenity', 'VOW'
            ],
            'keys': [
                'property_id','golfcoursename','hoamandatory','hoaphone',
                'hoawebsite','icemaker','dishwasher','compactor',
                'coolsystem','homephone','internetaddress','licensedsup',
                'location','manageco','mappage','lotsizesrc','lotvalue',
                'maintefeesched','masterplanned','masterplancom','microwave',
                'modified', 'new_construction','numcars','newconstruct_desc',
                'poolarea', 'poolpriv','poolpriv_desc','roombed_desc',
                'siding','taxamount','tax_id','taxrate','uid','uidprp',
                'utildist','vacation_rent','yearbuiltsrc','yearbuiltflag',
                'wateramenity','vow'
            ]
        },
        'prop_geoinfo': {
            'fields': [



            ]
            'keys': [
                'property_id','gpext_geocodeprov','gpext_latitude',
                'section_num','geo_market_area_id','geo_se_id','geo_mid_id',
                'geo_high_id'
            ]
        },
        'physicaladdr': {
            'fields': [

            ]
            'keys': [
                'property_id','physicaladdr_id','state','streetdir',
                'streetname','streetnum','streetnumdis','sub_id',
                'zipcode','zip4'
            ]
        },
        'restrictions': {
            'fields': [],
            'keys': ['restrictions_id','restrictions_desc']
        },
        'prop_restrictions': {
            'fields': ['index', ],
            'keys': ['property_id','restrictions_id']
        },
        'schooldistrict': {
            'fields': [],
            'keys': ['schooldistrict_id','schooldistrict_desc']
        },
        'prop_schooldistrict': {
            'fields': [],
            'keys': ['property_id','schooldistrict_id',
        },
        'watersewer': {
            'fields': [],
            'keys': ['watersewer_id','watersewer_desc' ]

        },
        'prop_watersewer': {
            'fields': [],
            'keys': ['property_id','watersewer_id']
        },
        'streetsurface': {
            'fields': [],
            'keys': ['streetsurface_id','streetsurface_desc']
        },
        'prop_streetsurface': {
            'fields': [],
            'keys': ['property_id','streetsurface_id']
        },
        'exemptions': {
            'fields': [],
            'keys': ['exemptions_id','exemptions_desc']
        },
        'prop_exemptions': {
            'fields': [],
            'keys': ['property_id','exemptions_id']

        },
        'rangetype': {
            'fields': [],
            'keys': ['rangetype_id','rangetype_desc']
        },
        'prop_rangetype': {
            'fields': [],
            'keys': ['property_id','rangetype_id']
        },
        'subdivsion': {
            'fields': [],
            'keys': ['sub_id','sub_desc']
        },
        'garage': {
            'fields': [],
            'keys':['garage_desc_id','garage_desc_name']
        },
        'prop_garage': {
            'fields': [],


        }
        'property_id',
        'garage_desc_id',

        'garagecarport': {
            'fields': [],
            'keys': [
                'property_id', 'garagecarport_id','garagecarport_desc',
                'garage_desc_id'
            ]

        },
        'bath': {
            'fields': [],
            'keys': ['bath_id','bath_desc']
        },
        'prop_bath': {
            'fields': [],
            'keys': ['property_id', 'bath_id']
        },
        'floors': {
            'fields': [],
            'keys': ['floors_id','floors_desc']
        },
        'prop_floors': {
            'fields': [],
            'keys': ['property_id','floors_id']

        },
        'foundation': {
            'fields': [],
            'keys': ['foundation_id','foundation_desc']
        },
        'prop_foundation': {
            'fields': [],
            'keys': ['property_id','foundation_id']
        },
        'geomarketarea': {
            'fields': [],
            'keys': ['geo_market_area_id','geo_market_desc']
        },
        'geoschoolelm': {
            'fields': [],
            'keys': ['geo_se_id','geo_se_desc']
        },
        'geoschoolmid': {
            'fields': [],
            'keys': ['geo_mid_id','geo_mid_desc']
        },
        'geoschoolhigh': {
            'fields': [],
            'keys': ['geo_high_id','geo_high_desc']
        },
        'disclosures': {
            'fields': ['disclosure_id', 'Disclosures'],
            'keys': ['disclosure_id','disclosure_desc']
        },
        'listing_disclosures': {
            'fields': [],
            'keys': ['list_id','disclosure_id']
        },
        'financeavail': {
            'fields': ['financeavail_id', 'FinanceAvail'],
            'keys': ['financeavail_id','financeavail_desc']
        },
        'listing_financeavail': {
            'fields': ['list_id', 'financeavail_id'],
            'keys': ['list_id','financeavail_id']
        },
        'listing': {
            'fields': [
                'list_id', 'property_id', 'MLSNum', 'ListDate', 'ListPrice',
                'ListPriceOrig', 'PhoneApptDesc', 'PhoneAlt', 'PhoneNight',
                'PhotoCount', 'PointsDiscount', 'PendingDate', 'RealRemarks',
                'Remarks', 'RemovalOptDate', 'RepairSeller', 'ShowInstr',
                'TitlePaidBy', 'WebAddress', 'WithdrawnDate',
                'VariableDualRate', 'OffMarketDate', 'OnlineBidding',
                'OnlineBiddingDate', 'AgentList', 'AgenSell', 'AgentWeb'
            ],
            'keys': [
                'list_id', 'property_id', 'mlsnum', 'list_date', 'list_price',
                'list_price_orig', 'phoneapptdesc', 'phone_alt', 'phone_night',
                'photo_count', 'points_discount', 'pendingdate', 'realremark',
                'remarks', 'removaloptdate', 'repairseller', 'showinstruct',
                'title_paid_by', 'webaddr', 'withdrawndate',
                'variable_dual_rate', 'offmarketdate', 'onlinebid',
                'onlinebiddate', 'agentlist', 'agentsell', 'agentweb'
            ]
        },
        'listtype': {
            'fields': ['ltype_id', 'ListType'],
            'keys': ['ltype_id', 'ltype_info']
        },
        'listing_listtype': {
            'fields': ['list_id', 'ltype_id'],
            'keys': ['list_id', 'ltype_id']
        },
        'price': {
            'fields': [
                'price_id', 'list_id', 'PriceSqftList', 'PriceSqFtSold',
                'SalesPrice', 'SellerToClosingCosts'
            ],
            'keys': [
                'price_id', 'list_id', 'pricesqftlist', 'pricesqftsold',
                'sale_price', 'seller_closing_cost'
            ]
        }


    }
