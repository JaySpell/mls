---
---Information about property - all information about the property will
---bind to the property_id
---

CREATE TABLE property (
  property_id           bigserial PRIMARY KEY,
  acres                 decimal,
  acresdesc             varchar(50),
  bathsfull             smallint,
  bathshalf             smallint,
  beds                  smallint,
  bedsmax               smallint,
  beddim                varchar[],
  buildersname          varchar(50),
  countertops           varchar(50),
  garagecap             smallint,
  legal_addr            varchar(500),
  sqftbuilding          smallint,
  lotdim                varchar(50),
  stories               real,
  breakfastdim          varchar(25),
  diningdim             varchar(25),
  dendim                varchar(25),
  kitchendim            varchar(25),
  livingdim             varchar(25),
  mediadim              varchar(25),
  familydim             varchar(25)
);


---Dump all other values for property here---

CREATE TABLE prop_other (
  property_id           bigserial REFERENCES property (property_id),
  golfcoursename        varchar(50),
  hoamandatory          boolean,
  hoaphone              varchar(15),
  hoawebsite            varchar(50),
  icemaker              boolean,
  dishwasher            boolean,
  compactor             boolean,
  coolsystem            varchar(25),
  homephone             varchar(15),
  internetaddress       boolean,
  licensedsup           varchar(50),
  location              smallint,
  manageco              varchar(50),
  mappage               varchar(50),
  lotsizesrc            varchar(50),
  lotvalue              varchar(50),
  maintefeesched        varchar(50),
  masterplanned         boolean,
  masterplancom         varchar(50),
  microwave             boolean,
  modified              date,
  new_construction      boolean,
  numcars               smallint,
  newconstruct_desc     varchar(50),
  poolarea              boolean,
  poolpriv              boolean,
  poolpriv_desc         varchar(200),
  roombed_desc          varchar(200),
  siding                varchar(50),
  taxamount             smallint,
  tax_id                varchar(25),
  taxrate               real,
  uid                   bigint,
  uidprp                bigint,
  utildist              boolean,
  vacation_rent         boolean,
  yearbuiltsrc          varchar(25),
  yearbuiltflag         boolean,
  wateramenity          varchar(25),
  vow                   boolean
);

---                           ---
---   Linking tables below    ---
---                           ---
CREATE TABLE restrictions (
  restrictions_id       serial PRIMARY KEY,
  restrictions_desc     varchar(50)
);

CREATE TABLE prop_restrictions (
  property_id           bigserial REFERENCES property (property_id),
  restrictions_id       serial REFERENCES restrictions (restrictions_id),
  PRIMARY KEY (property_id, restrictions_id)
);

CREATE TABLE schooldistrict (
  schooldistrict_id     serial PRIMARY KEY,
  schooldistrict_desc   smallint
);

CREATE TABLE prop_schooldistrict (
  property_id           bigserial REFERENCES property (property_id),
  schooldistrict_id     serial REFERENCES schooldistrict(schooldistrict_id),
  PRIMARY KEY (property_id, schooldistrict_id)
);

CREATE TABLE watersewer (
  watersewer_id         serial PRIMARY KEY,
  watersewer_desc       varchar(50)
);

CREATE TABLE prop_watersewer (
  property_id           bigserial REFERENCES property (property_id),
  watersewer_id         serial REFERENCES watersewer (watersewer_id),
  PRIMARY KEY (property_id, watersewer_id)
);

CREATE TABLE streetsurface (
  streetsurface_id      serial PRIMARY KEY,
  streetsurface_desc    varchar(50)
);

CREATE TABLE prop_streetsurface (
  property_id           bigserial REFERENCES property (property_id),
  streetsurface_id      serial REFERENCES streetsurface (streetsurface_id),
  PRIMARY KEY (property_id, streetsurface_id)
);

CREATE TABLE exemptions (
  exemptions_id         serial PRIMARY KEY,
  exemptions_desc       varchar(25)
);

CREATE TABLE prop_exemptions (
  property_id           serial REFERENCES property (property_id),
  exemptions_id         serial REFERENCES exemptions (exemptions_id),
  PRIMARY KEY (property_id, exemptions_id)
);

CREATE TABLE rangetype (
  rangetype_id          serial PRIMARY KEY,
  rangetype_desc        varchar(50)
);

CREATE TABLE prop_rangetype (
  property_id           serial REFERENCES property (property_id),
  rangetype_id          serial REFERENCES rangetype (rangetype_id),
  PRIMARY KEY (property_id, rangetype_id)
);

CREATE TABLE subdivision (
  subdivision_id        serial PRIMARY KEY,
  subdivision_desc      varchar(50)
);

CREATE TABLE garage (
  garage_id             serial PRIMARY KEY,
  garage_desc           varchar(50)
);

CREATE TABLE prop_garage (
  property_id           serial REFERENCES property (property_id),
  garage_id             serial REFERENCES garage (garage_id),
  PRIMARY KEY (property_id, garage_id)
);

CREATE TABLE garagecarport (
  garagecarport_id      serial PRIMARY KEY,
  garagecarport_desc    varchar(50)
);

CREATE TABLE prop_garagecarport (
  property_id          serial REFERENCES property (property_id),
  garage_desc_id       serial REFERENCES garagecarport (garagecarport_id),
  PRIMARY KEY (property_id, garage_desc_id)
);

CREATE TABLE bath (
  bath_id               serial PRIMARY KEY,
  bath_desc             varchar(50)
);

CREATE TABLE prop_bath (
  property_id           serial REFERENCES property (property_id),
  bath_id               serial REFERENCES bath (bath_id),
  PRIMARY KEY (property_id, bath_id)
);

CREATE TABLE floors (
  floors_id             serial PRIMARY KEY,
  floors_desc           varchar(50)
);

CREATE TABLE prop_floors (
  property_id           bigserial REFERENCES property (property_id),
  floors_id             serial REFERENCES floors (floors_id),
  PRIMARY KEY (property_id, floors_id)
);

CREATE TABLE foundation (
  foundation_id         serial PRIMARY KEY,
  foundation_desc       varchar(50)
);

CREATE TABLE prop_foundation (
  property_id           serial REFERENCES property (property_id),
  foundation_id         serial REFERENCES foundation (foundation_id),
  PRIMARY KEY (property_id, foundation_id)
);

CREATE TABLE geomarketarea (
  geomarketarea_id    serial PRIMARY KEY,
  geomarketarea_desc  varchar(50)
);

CREATE TABLE geoschoolelm (
  geoschoolelm_id       serial PRIMARY KEY,
  geoschoolelm_desc     bigserial
);

CREATE TABLE geoschoolmid (
  geoschoolmid_id       serial PRIMARY KEY,
  geoschoolmid_desc     bigserial
);

CREATE TABLE geoschoolhigh (
  geoschoolhigh_id      serial PRIMARY KEY,
  geoschoolhigh_desc    bigserial
);

CREATE TABLE disclosures (
  disclosures_id         serial PRIMARY KEY,
  disclosures_desc       varchar(50)
);

CREATE TABLE financeavail (
  financeavail_id       bigserial PRIMARY KEY,
  financeavail_desc     varchar(75)
);

CREATE TABLE physicaladdr (
  property_id           bigserial REFERENCES property (property_id),
  physicaladdr_id       bigserial,
  state                 smallint,
  streetdir             char(1),
  streetname            varchar(50),
  streetnum             bigint,
  streetnumdis          smallint,
  subdivision_id        serial REFERENCES subdivision (subdivision_id),
  zipcode               bigint,
  zip4                  smallint,
  PRIMARY KEY (property_id, physicaladdr_id)
);

CREATE TABLE prop_geoinfo (
  property_id           bigserial REFERENCES property (property_id),
  gpext_geocodeprov     bigint,
  gpext_latitude        real,
  section_num           bigint,
  geomarketarea_id      serial REFERENCES geomarketarea (geomarketarea_id),
  geoschoolelm_id       serial REFERENCES geoschoolelm (geoschoolelm_id),
  geoschoolmid_id       serial REFERENCES geoschoolmid (geoschoolmid_id),
  geoschoolhigh_id      serial REFERENCES geoschoolhigh (geoschoolhigh_id),
  PRIMARY KEY (property_id)
);

---                               ---
--- Listing tables - specific     ---
--- to the listing not property   ---
---                               ---

CREATE TABLE listing (
  list_id               bigserial PRIMARY KEY,
  property_id           bigserial REFERENCES property (property_id),
  mlsnum                smallint,
  list_date             date,
  list_price            real,
  list_price_orig       real,
  phoneapptdesc         varchar(50),
  phone_alt             varchar(20),
  phone_night           varchar(20),
  photo_count           smallint,
  points_discount       smallint,
  pendingdate           date,
  realremark            varchar(500),
  remarks               varchar(500),
  removaloptdate        date,
  repairseller          smallint,
  showinstruct          varchar(200),
  title_paid_by         varchar(50),
  webaddr               varchar(200),
  withdrawndate         date,
  variable_dual_rate    boolean,
  offmarketdate         date,
  onlinebid             boolean,
  onlinebiddate         date,
  agentlist             varchar(25),
  agentsell             varchar(25),
  agentweb              varchar(25)
);

CREATE TABLE listtype (
  ltype_id              serial PRIMARY KEY,
  ltype_info            varchar(50)
);

CREATE TABLE listing_listtype (
  listing_id            serial REFERENCES listing (list_id),
  ltype_id              serial REFERENCES listtype (ltype_id),
  PRIMARY KEY (listing_id, ltype_id)
);

CREATE TABLE price (
  price_id              bigserial PRIMARY KEY,
  list_id               bigserial REFERENCES listing (list_id),
  pricesqftlist         real,
  pricesqftsold         real,
  sale_price            bigint,
  seller_closing_cost   bigint
);

CREATE TABLE listing_financeavail (
  list_id               bigserial REFERENCES listing (list_id),
  financeavail_id       bigserial REFERENCES financeavail (financeavail_id),
  PRIMARY KEY (list_id, financeavail_id)
);

CREATE TABLE listing_disclosures (
  list_id               bigserial REFERENCES listing (list_id),
  disclosures_id        serial REFERENCES disclosures (disclosures_id),
  PRIMARY KEY (list_id, disclosures_id)
);
