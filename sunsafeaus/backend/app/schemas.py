# app/schemas.py

from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class CancerData(BaseModel):
    id: int
    data_type: Optional[str] = None
    cancer_type: Optional[str] = None
    year: Optional[int] = None
    sex: Optional[str] = None
    age_group: Optional[str] = None
    count: Optional[int] = None
    age_specific_rate: Optional[float] = None
    asr_2001: Optional[str] = None
    asr_2024: Optional[str] = None
    asr_who: Optional[str] = None
    asr_segi: Optional[str] = None
    icd10_codes: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class CancerMortality(BaseModel):
    id: int
    data_type: Optional[str] = None
    cancer_type: Optional[str] = None
    year: Optional[int] = None
    sex: Optional[str] = None
    age_group: Optional[str] = None
    count: Optional[int] = None
    age_specific_rate: Optional[float] = None
    asr_2001: Optional[str] = None
    asr_2024: Optional[str] = None
    asr_who: Optional[str] = None
    asr_segi: Optional[str] = None
    icd10_codes: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class Location(BaseModel):
    id: int
    postcode: Optional[int] = None
    locality: Optional[str] = None
    state: Optional[str] = None
    long: Optional[float] = None
    lat: Optional[float] = None
    # Include other fields as necessary

    model_config = ConfigDict(from_attributes=True)


class UVIndex(BaseModel):
    date_time: Optional[datetime] = None
    lat: Optional[float] = None
    lon: Optional[float] = None
    uv_index: Optional[float] = None
    city: Optional[str] = None
    year: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)
