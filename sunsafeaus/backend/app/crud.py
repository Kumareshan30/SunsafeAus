# app/crud.py
from typing import Optional, List

from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from . import model


def get_locations(db: Session, search_param: Optional[str] = None, limit: int = 100) -> List[model.Location]:
    query = db.query(model.Location)
    if search_param:
        search_pattern = f"%{search_param.lower()}%"
        query = select(
            model.Location.id,
            model.Location.postcode,
            model.Location.locality,
            model.Location.state,
            model.Location.long,
            model.Location.lat
        )
        query = query.filter(
            or_(
                model.Location.locality.ilike(search_pattern),
                model.Location.postcode.ilike(search_pattern),
                model.Location.state.ilike(search_pattern)
            )
        )
    return query.limit(limit)
