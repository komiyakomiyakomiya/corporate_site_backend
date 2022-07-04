from database import SessionLocal
from utils import utils
import models.employee as employee_model
import models.department as department_model
import models.work as work_model
import models.tag as tag_model
import models.work_tag as work_tag_model

db = SessionLocal()
# items = db.query(employee_model.Employee) \
#     .filter(employee_model.Employee.del_flg != 1) \
#     .all()

# for item in items:
#     print(item.works[0].image_path)


item = db.query(work_model.Work).get(1)
print(item.employee)
