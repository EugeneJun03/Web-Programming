from fastapi import APIRouter, Form
from ..db.m_db import m_db_connection
from typing import List

router = APIRouter(
    prefix="/api/admission",
)

@router.get("/test_api")
def test_api():
    return {"Hello":"world!"}

@router.get("/application")
def inquiry_application():
    result=m_db_connection.mdb_read()
    return {'result_list':result}

@router.post("/application")
def write_application(
    cli_title=Form(...),
    cli_subjects=Form(...), # array를 전달하지만 결국은 ,로 구분된 문자열을 받게 됨
    cli_written_time=Form(...)):

    content_guide=m_db_connection.get_content_guide_obj()
    content_guide.title=cli_title
    content_guide.subjects=cli_subjects
    content_guide.time=cli_written_time
    m_db_connection.mdb_write(content_guide)

    return {'status':'success'}

@router.get("/application/{app_num}")
def inquiry_application_detail(app_num):
    result=m_db_connection.mdb_read(int(app_num))
    return {'result':result}

@router.put("/application/{app_num}")
def modify_application(
    app_num,
    cli_title=Form(...),
    cli_subjects=Form(...), # array를 전달하지만 결국은 ,로 구분된 문자열을 받게 됨
    cli_written_time=Form(...)):

    content_guide=m_db_connection.get_content_guide_obj()
    content_guide.title=cli_title
    content_guide.subjects=cli_subjects
    content_guide.time=cli_written_time
    m_db_connection.mdb_modify(int(app_num), content_guide)

    return {'status':'success'}

@router.delete("/application/{app_num}")
def delete_applications(app_num):
    result=m_db_connection.mdb_delete(int(app_num))
    return {'result':result}
