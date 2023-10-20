import sys
from fastapi import APIRouter
from db.db_connect import engine
from models.course_models import School
from schemas.schools_schema import SchoolBase
from sqlalchemy import select
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


@router.put('/{id}/update')
def search_school_id(id: str, request: SchoolBase):
    pass

# @router.post('/{id}/update')
# def update_user(id: int, request: SchoolBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
#     return db_user.update_user(db, id, request)
