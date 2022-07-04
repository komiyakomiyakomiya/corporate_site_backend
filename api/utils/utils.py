import models.employee as employee_model
import models.department as department_model
import models.work as work_model
import models.tag as tag_model
import models.work_tag as work_tag_model


def create_objs(objs, db):
    db.add_all(objs)
    db.commit()


# def create_employee_by_employeename(employeenames, db):
#     employees = [employee_model.Employee(employeename=employeename) for employeename in employeenames]
#     db.add(employees)
#     db.commit()


# def update_employees_delflg_by_ids(ids, del_flg, db):
#     employees = db.query(employee_model.Employee).filter(employee_model.Employee.id.in_(ids)).all()
#     for employee in employees:
#         employee.del_flg = del_flg
#         db.add(employee)
#     db.commit()


# def delete_employees_by_employeenames(employeenames, db):
#     db.query(employee_model.Employee).filter(
#         employee_model.Employee.employeename.in_(employeenames)).delete()
#     db.commit()


# def update_books_employee_id_by_ids(ids, employee_id, db):
#     books = db.query(book_model.Book).filter(book_model.Book.id.in_(ids)).all()
#     for book in books:
#         book.employee_id = employee_id
#         db.add(book)
#     db.commit()
