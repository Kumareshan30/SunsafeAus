from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base


class CancerData(Base):
    __tablename__ = 'cancer_data'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    data_type = Column(String)
    cancer_type = Column(String)
    year = Column(Integer)
    sex = Column(String)
    age_group = Column(String)
    count = Column(Integer)
    age_specific_rate = Column(Float)
    asr_2001 = Column(String)
    asr_2024 = Column(String)
    asr_who = Column(String)
    asr_segi = Column(String)
    icd10_codes = Column(String)


class CancerMortality(Base):
    __tablename__ = 'cancer_mortality'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    data_type = Column(String)
    cancer_type = Column(String)
    year = Column(Integer)
    sex = Column(String)
    age_group = Column(String)
    count = Column(Integer)
    age_specific_rate = Column(Float)
    asr_2001 = Column(String)
    asr_2024 = Column(String)
    asr_who = Column(String)
    asr_segi = Column(String)
    icd10_codes = Column(String)


class Location(Base):
    __tablename__ = 'locations'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    postcode = Column(Integer)
    locality = Column(String)
    state = Column(String)
    long = Column(Float)
    lat = Column(Float)
    dc = Column(String)
    type = Column(String)
    status = Column(String)
    sa3name = Column(String)
    sa4 = Column(Float)
    sa4name = Column(String)
    region = Column(String)
    lat_precise = Column(Float)
    long_precise = Column(Float)
    sa1_code_2021 = Column(Float)
    sa1_name_2021 = Column(String)
    sa2_code_2021 = Column(Float)
    sa2_name_2021 = Column(String)
    sa3_code_2021 = Column(Float)
    sa3_name_2021 = Column(String)
    sa4_code_2021 = Column(Float)
    sa4_name_2021 = Column(String)
    ra_2011 = Column(Float)
    ra_2016 = Column(Float)
    ra_2021 = Column(Float)
    ra_2021_name = Column(String)
    mmm_2015 = Column(Float)
    mmm_2019 = Column(Float)
    ced = Column(String)
    altitude = Column(Float)
    chargezone = Column(String)
    phn_code = Column(String)
    phn_name = Column(String)
    lgaregion = Column(String)
    lgacode = Column(Float)
    electorate = Column(String)
    electoraterating = Column(String)
    sed_code = Column(Float)
    sed_name = Column(String)


class UVIndex(Base):
    __tablename__ = 'uv_index'
    __table_args__ = {'extend_existing': True}
    date_time = Column(DateTime, primary_key=True)
    lat = Column(Float, primary_key=True)
    lon = Column(Float, primary_key=True)
    uv_index = Column(Float)
    city = Column(String)
    year = Column(Integer)
