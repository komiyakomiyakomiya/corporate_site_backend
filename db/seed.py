
from database import SessionLocal
import models.employee as employee_model
import models.department as department_model
import models.work as work_model
import models.tag as tag_model
import models.work_tag as work_tag_model
from utils import utils


if __name__ == '__main__':
    department_objs = [
        department_model.Department(
            department_name = 'Stylist'
        ),
        department_model.Department(
            department_name = 'Assistant'
        ),
        department_model.Department(
            department_name = 'Reception'
        )
    ]

    employee_objs = [
        employee_model.Employee(
            employee_name = '向井',
            image_path = 's3;//images/employees/1.png',
            department_id = 1,
        )
    ]

    tag_objs = [
        tag_model.Tag(
            tag_name = 'Mens',
        ),
        tag_model.Tag(
            tag_name = 'Womens',
        ),
        tag_model.Tag(
            tag_name = 'Short',
        ),
        tag_model.Tag(
            tag_name = 'Bob',
        ),
        tag_model.Tag(
            tag_name = 'Long',
        ),
    ]

    work_objs = [
        work_model.Work(
            image_path = 's3;//images/works/1.png',
            employee_id = 1,
        )
    ]

    work_tag_objs = [
        work_tag_model.WorkTag(
            work_id = 1,
            tag_id = 1
        ),
        work_tag_model.WorkTag(
            work_id = 1,
            tag_id = 2
        ),
                work_tag_model.WorkTag(
            work_id = 2,
            tag_id = 3
        ),
        work_tag_model.WorkTag(
            work_id = 3,
            tag_id = 1
        ),
    ]


    db = SessionLocal()
    utils.create_objs(department_objs, db)
    utils.create_objs(employee_objs, db)
    utils.create_objs(work_objs, db)
    utils.create_objs(tag_objs, db)
    utils.create_objs(work_tag_objs, db)
    # delete_employee_by_ids(employee_ids)
