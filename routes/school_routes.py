import sys
from fastapi import APIRouter
from db.db_connect import engine
from models.course_models import School
from schemas.schools_schema import SchoolBase
from sqlalchemy import select, update
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix='/schools',
    tags=['schools']
)


@router.get('/')
def get_schools():
    school_list = []
    try:
        with Session(engine) as session:
            schools = select(School)
            for sch in session.scalars(schools):
                school_list.append(sch.__dict__)
    except SQLAlchemyError as err:
        print(f'Error working with db. Error: {err}', file=sys.stderr)

    return {'schools': jsonable_encoder(school_list)}


@router.get('/search/{name}')
def search_school_name(name: str):
    partial_name = f'%{name}%'
    school_list = []
    try:
        with Session(engine) as session:
            schools = select(School).where(School.fullname.like(partial_name))
            for sch in session.scalars(schools):
                print(sch.fullname)
                school_list.append(sch.__dict__)
    except SQLAlchemyError as err:
        print(f'Error working with db. Error: {err}', file=sys.stderr)

    return {'schools': jsonable_encoder(school_list)}


@router.post('/{sch_id}/update')
def search_school_id(sch_id: str, request: SchoolBase):
    result = []
    try:
        with Session(engine) as session:
            session.begin()
            stmt = (
                update(School)
                .where(School.school_id == sch_id)
                .values(
                    city=request.city,
                    state=request.state,
                    country=request.country
                )
            )
            session.execute(stmt)
            session.commit()

            # Confirm record was updated
            updated_result = select(School).where(School.school_id == sch_id)

            for r in session.scalars(updated_result):
                result.append(r.__dict__)

        return {'updated_values': result}
    except SQLAlchemyError as err:
        session.rollback()
        print(f'Error working with db. Error: {err}', file=sys.stderr)
