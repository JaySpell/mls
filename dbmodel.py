from peewee import *

database = PostgresqlDatabase('mls', **{'user': 'postgres'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Bath(BaseModel):
    bath_desc = CharField(null=True)
    bath = PrimaryKeyField(db_column='bath_id')

    class Meta:
        db_table = 'bath'

class Disclosures(BaseModel):
    disclosure_desc = CharField(null=True)
    disclosure = PrimaryKeyField(db_column='disclosure_id')

    class Meta:
        db_table = 'disclosures'

class Exemptions(BaseModel):
    exemptions_desc = CharField(null=True)
    exemptions = PrimaryKeyField(db_column='exemptions_id')

    class Meta:
        db_table = 'exemptions'

class Financeavail(BaseModel):
    financeavail_desc = CharField(null=True)
    financeavail = PrimaryKeyField(db_column='financeavail_id')

    class Meta:
        db_table = 'financeavail'

class Floors(BaseModel):
    floors_desc = CharField(null=True)
    floors = PrimaryKeyField(db_column='floors_id')

    class Meta:
        db_table = 'floors'

class Foundation(BaseModel):
    foundation_desc = CharField(null=True)
    foundation = PrimaryKeyField(db_column='foundation_id')

    class Meta:
        db_table = 'foundation'

class Garagecarport(BaseModel):
    garagecarport_desc = CharField(null=True)
    garagecarport = PrimaryKeyField(db_column='garagecarport_id')

    class Meta:
        db_table = 'garagecarport'

class Geomarketarea(BaseModel):
    geo_market_area = PrimaryKeyField(db_column='geo_market_area_id')
    geo_market_desc = CharField(null=True)

    class Meta:
        db_table = 'geomarketarea'

class Geoschoolelm(BaseModel):
    geo_se_desc = CharField(null=True)
    geo_se = PrimaryKeyField(db_column='geo_se_id')

    class Meta:
        db_table = 'geoschoolelm'

class Geoschoolhigh(BaseModel):
    geo_high_desc = CharField(null=True)
    geo_high = PrimaryKeyField(db_column='geo_high_id')

    class Meta:
        db_table = 'geoschoolhigh'

class Geoschoolmid(BaseModel):
    geo_mid_desc = CharField(null=True)
    geo_mid = PrimaryKeyField(db_column='geo_mid_id')

    class Meta:
        db_table = 'geoschoolmid'

class Property(BaseModel):
    acres = DecimalField(null=True)
    acresdesc = CharField(null=True)
    bathsfull = IntegerField(null=True)
    bathshalf = IntegerField(null=True)
    beddim = UnknownField(null=True)  # ARRAY
    beds = IntegerField(null=True)
    bedsmax = IntegerField(null=True)
    breakfastdim = CharField(null=True)
    buildersname = CharField(null=True)
    countertops = CharField(null=True)
    dendim = CharField(null=True)
    diningdim = CharField(null=True)
    familydim = CharField(null=True)
    garagecap = IntegerField(null=True)
    kitchendim = CharField(null=True)
    legal_addr = CharField(null=True)
    livingdim = CharField(null=True)
    lotdim = CharField(null=True)
    mediadim = CharField(null=True)
    property = BigIntegerField(db_column='property_id', primary_key=True)
    sqftbuilding = IntegerField(null=True)
    stories = FloatField(null=True)

    class Meta:
        db_table = 'property'

class Listing(BaseModel):
    agentlist = CharField(null=True)
    agentsell = CharField(null=True)
    agentweb = CharField(null=True)
    list_date = DateField(null=True)
    list = BigIntegerField(db_column='list_id', primary_key=True)
    list_price = FloatField(null=True)
    list_price_orig = FloatField(null=True)
    mlsnum = IntegerField(null=True)
    offmarketdate = DateField(null=True)
    onlinebid = BooleanField(null=True)
    onlinebiddate = DateField(null=True)
    pendingdate = DateField(null=True)
    phone_alt = CharField(null=True)
    phone_night = CharField(null=True)
    phoneapptdesc = CharField(null=True)
    photo_count = IntegerField(null=True)
    points_discount = IntegerField(null=True)
    property = ForeignKeyField(db_column='property_id', rel_model=Property, to_field='property')
    realremark = CharField(null=True)
    remarks = CharField(null=True)
    removaloptdate = DateField(null=True)
    repairseller = IntegerField(null=True)
    showinstruct = CharField(null=True)
    title_paid_by = CharField(null=True)
    variable_dual_rate = BooleanField(null=True)
    webaddr = CharField(null=True)
    withdrawndate = DateField(null=True)

    class Meta:
        db_table = 'listing'

class Listtype(BaseModel):
    ltype = PrimaryKeyField(db_column='ltype_id')
    ltype_info = CharField(null=True)

    class Meta:
        db_table = 'listtype'

class ListingListtype(BaseModel):
    listing = ForeignKeyField(db_column='listing_id', rel_model=Listing, to_field='list')
    ltype = ForeignKeyField(db_column='ltype_id', rel_model=Listtype, to_field='ltype')

    class Meta:
        db_table = 'listing_listtype'
        indexes = (
            (('listing', 'ltype'), True),
        )
        primary_key = CompositeKey('listing', 'ltype')

class Subdivsion(BaseModel):
    sub_desc = CharField(null=True)
    sub = PrimaryKeyField(db_column='sub_id')

    class Meta:
        db_table = 'subdivsion'

class Physicaladdr(BaseModel):
    physicaladdr = IntegerField(db_column='physicaladdr_id')
    property = ForeignKeyField(db_column='property_id', rel_model=Property, to_field='property')
    state = IntegerField(null=True)
    streetdir = CharField(null=True)
    streetname = CharField(null=True)
    streetnum = BigIntegerField(null=True)
    streetnumdis = IntegerField(null=True)
    sub = ForeignKeyField(db_column='sub_id', rel_model=Subdivsion, to_field='sub')
    zip4 = IntegerField(null=True)
    zipcode = BigIntegerField(null=True)

    class Meta:
        db_table = 'physicaladdr'
        indexes = (
            (('property', 'physicaladdr'), True),
        )
        primary_key = CompositeKey('physicaladdr', 'property')

class Price(BaseModel):
    list = ForeignKeyField(db_column='list_id', rel_model=Listing, to_field='list')
    price = BigIntegerField(db_column='price_id', primary_key=True)
    pricesqftlist = FloatField(null=True)
    pricesqftsold = FloatField(null=True)
    sale_price = BigIntegerField(null=True)
    seller_closing_cost = BigIntegerField(null=True)

    class Meta:
        db_table = 'price'

class PropBath(BaseModel):
    bath = ForeignKeyField(db_column='bath_id', rel_model=Bath, to_field='bath')
    property = ForeignKeyField(db_column='property_id', rel_model=Property, to_field='property')

    class Meta:
        db_table = 'prop_bath'
        indexes = (
            (('property', 'bath'), True),
        )
        primary_key = CompositeKey('bath', 'property')

class PropExemptions(BaseModel):
    exemptions = ForeignKeyField(db_column='exemptions_id', rel_model=Exemptions, to_field='exemptions')
    property = ForeignKeyField(db_column='property_id', rel_model=Property, to_field='property')

    class Meta:
        db_table = 'prop_exemptions'
        indexes = (
            (('property', 'exemptions'), True),
        )
        primary_key = CompositeKey('exemptions', 'property')

class PropFloors(BaseModel):
    floors = ForeignKeyField(db_column='floors_id', rel_model=Floors, to_field='floors')
    property = ForeignKeyField(db_column='property_id', rel_model=Property, to_field='property')

    class Meta:
        db_table = 'prop_floors'
        indexes = (
            (('property', 'floors'), True),
        )
        primary_key = CompositeKey('floors', 'property')

class PropFoundation(BaseModel):
    foundation = ForeignKeyField(db_column='foundation_id', rel_model=Foundation, to_field='foundation')
    property = ForeignKeyField(db_column='property_id', rel_model=Property, to_field='property')

    class Meta:
        db_table = 'prop_foundation'
        indexes = (
            (('property', 'foundation'), True),
        )
        primary_key = CompositeKey('foundation', 'property')

class PropGaragecarport(BaseModel):
    garage_desc = ForeignKeyField(db_column='garage_desc_id', rel_model=Garagecarport, to_field='garagecarport')
    property = ForeignKeyField(db_column='property_id', rel_model=Property, to_field='property')

    class Meta:
        db_table = 'prop_garagecarport'
        indexes = (
            (('property', 'garage_desc'), True),
        )
        primary_key = CompositeKey('garage_desc', 'property')

class PropGeoinfo(BaseModel):
    geo_high = ForeignKeyField(db_column='geo_high_id', rel_model=Geoschoolhigh, to_field='geo_high')
    geo_market_area = ForeignKeyField(db_column='geo_market_area_id', rel_model=Geomarketarea, to_field='geo_market_area')
    geo_mid = ForeignKeyField(db_column='geo_mid_id', rel_model=Geoschoolmid, to_field='geo_mid')
    geo_se = ForeignKeyField(db_column='geo_se_id', rel_model=Geoschoolelm, to_field='geo_se')
    gpext_geocodeprov = BigIntegerField(null=True)
    gpext_latitude = FloatField(null=True)
    property = ForeignKeyField(db_column='property_id', primary_key=True, rel_model=Property, to_field='property')
    section_num = BigIntegerField(null=True)

    class Meta:
        db_table = 'prop_geoinfo'

class PropOther(BaseModel):
    compactor = BooleanField(null=True)
    coolsystem = CharField(null=True)
    dishwasher = BooleanField(null=True)
    golfcoursename = CharField(null=True)
    hoamandatory = BooleanField(null=True)
    hoaphone = CharField(null=True)
    hoawebsite = CharField(null=True)
    homephone = CharField(null=True)
    icemaker = BooleanField(null=True)
    internetaddress = BooleanField(null=True)
    licensedsup = CharField(null=True)
    location = IntegerField(null=True)
    lotsizesrc = CharField(null=True)
    lotvalue = CharField(null=True)
    maintefeesched = CharField(null=True)
    manageco = CharField(null=True)
    mappage = CharField(null=True)
    masterplancom = CharField(null=True)
    masterplanned = BooleanField(null=True)
    microwave = BooleanField(null=True)
    modified = DateField(null=True)
    new_construction = BooleanField(null=True)
    newconstruct_desc = CharField(null=True)
    numcars = IntegerField(null=True)
    poolarea = BooleanField(null=True)
    poolpriv = BooleanField(null=True)
    poolpriv_desc = CharField(null=True)
    property = ForeignKeyField(db_column='property_id', rel_model=Property, to_field='property')
    roombed_desc = CharField(null=True)
    siding = CharField(null=True)
    tax = CharField(db_column='tax_id', null=True)
    taxamount = IntegerField(null=True)
    taxrate = FloatField(null=True)
    uid = BigIntegerField(null=True)
    uidprp = BigIntegerField(null=True)
    utildist = BooleanField(null=True)
    vacation_rent = BooleanField(null=True)
    vow = BooleanField(null=True)
    wateramenity = CharField(null=True)
    yearbuiltflay = BooleanField(null=True)
    yearbuiltsrc = CharField(null=True)

    class Meta:
        db_table = 'prop_other'

class Rangetype(BaseModel):
    rangetype_desc = CharField(null=True)
    rangetype = PrimaryKeyField(db_column='rangetype_id')

    class Meta:
        db_table = 'rangetype'

class PropRangetype(BaseModel):
    property = ForeignKeyField(db_column='property_id', rel_model=Property, to_field='property')
    rangetype = ForeignKeyField(db_column='rangetype_id', rel_model=Rangetype, to_field='rangetype')

    class Meta:
        db_table = 'prop_rangetype'
        indexes = (
            (('property', 'rangetype'), True),
        )
        primary_key = CompositeKey('property', 'rangetype')

class Restrictions(BaseModel):
    restrictions_desc = CharField(null=True)
    restrictions = PrimaryKeyField(db_column='restrictions_id')

    class Meta:
        db_table = 'restrictions'

class PropRestrictions(BaseModel):
    property = ForeignKeyField(db_column='property_id', rel_model=Property, to_field='property')
    restrictions = ForeignKeyField(db_column='restrictions_id', rel_model=Restrictions, to_field='restrictions')

    class Meta:
        db_table = 'prop_restrictions'
        indexes = (
            (('property', 'restrictions'), True),
        )
        primary_key = CompositeKey('property', 'restrictions')

class Schooldistrict(BaseModel):
    schooldistrict_desc = IntegerField(null=True)
    schooldistrict = PrimaryKeyField(db_column='schooldistrict_id')

    class Meta:
        db_table = 'schooldistrict'

class PropSchooldistrict(BaseModel):
    property = ForeignKeyField(db_column='property_id', rel_model=Property, to_field='property')
    schooldistrict = ForeignKeyField(db_column='schooldistrict_id', rel_model=Schooldistrict, to_field='schooldistrict')

    class Meta:
        db_table = 'prop_schooldistrict'
        indexes = (
            (('property', 'schooldistrict'), True),
        )
        primary_key = CompositeKey('property', 'schooldistrict')

class Streetsurface(BaseModel):
    streetsurface_desc = CharField(null=True)
    streetsurface = PrimaryKeyField(db_column='streetsurface_id')

    class Meta:
        db_table = 'streetsurface'

class PropStreetsurface(BaseModel):
    property = ForeignKeyField(db_column='property_id', rel_model=Property, to_field='property')
    streetsurface = ForeignKeyField(db_column='streetsurface_id', rel_model=Streetsurface, to_field='streetsurface')

    class Meta:
        db_table = 'prop_streetsurface'
        indexes = (
            (('property', 'streetsurface'), True),
        )
        primary_key = CompositeKey('property', 'streetsurface')

class Watersewer(BaseModel):
    watersewer_desc = CharField(null=True)
    watersewer = PrimaryKeyField(db_column='watersewer_id')

    class Meta:
        db_table = 'watersewer'

class PropWatersewer(BaseModel):
    property = ForeignKeyField(db_column='property_id', rel_model=Property, to_field='property')
    watersewer = ForeignKeyField(db_column='watersewer_id', rel_model=Watersewer, to_field='watersewer')

    class Meta:
        db_table = 'prop_watersewer'
        indexes = (
            (('property', 'watersewer'), True),
        )
        primary_key = CompositeKey('property', 'watersewer')
