from sqlalchemy import AliasedReturnsRows, select, insert, update, bindparam, delete
from sqlalchemy.orm import  outerjoin, aliased
from init import Session, Department, Employee

def select_department():
    query = select(Department).order_by('name')
    
    result = session.execute(query)
    
    for row in result:
        print(row)
        
        
# 查询多个类
def select_multiple():
    query = select(Employee, Department ).join(Employee.department)
    
    result = session.execute(query)
    
    for row in result:
        print(row)
def select_with_alias():
    
    emp_cls = aliased(Employee, name='emp')  
    dep_cls = aliased(Department, name='dep')  
    query = select(emp_cls, dep_cls ).join(emp_cls.department.of_type(dep_cls), isouter=True)
    result = session.execute(query)
    for row in result:
        print(row)

def select_fileds():
    query = select(Employee.name, Department.name).join_from(Employee, Department)
    
    result = session.execute(query)
    
    for row in result:
        print(row)
        
        
def batch_insert():
    session.execute(
        insert(Department).values(
            [
                {"name": "技术"},
                {"name": "客服"},
            ]
        )
        
    )
    session.commit()
def batch_insert_emp():
    session.execute(
        insert(Employee).values(
            [
                {
                    "name": "jack125",
                    "birthday": "2020-02-01",
                    "dep_id": select(Department.id).where(Department.name=='hr')
                },
            ]
        )
    )
    session.commit()
    
def batch_update_emp():
    session.execute(
        update(Employee),
        [
            {"id": 3, "name": 'Employee'}
        ]
    )
    session.commit()
session = Session()

# select_department()
# select_multiple()
# select_with_alias()
# select_fileds()
# batch_insert()
# batch_insert_emp()
# batch_update_emp()