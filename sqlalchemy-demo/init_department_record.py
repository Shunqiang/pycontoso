from init_department import department, engine, employee
import sqlalchemy
with engine.connect() as conn:
    # conn.execute(department.insert(), [
    #     {"name": 'haha1'},
    #     {"name": 'ccc1'},
    # ])
    
    # conn.execute(employee.insert(), [
    #     {"name": 'jack1', "department_id": 1},
    #     {"name": 'jack3', "department_id": 1},
      
    # ])
    
    # 一对多查询部门下所有员工
    join = employee.join(department, department.c.id == employee.c.department_id)
    # 带部门信息
    query = sqlalchemy.select(join).where(department.c.name == 'haha') 
    # 不带部门信息
    # query = sqlalchemy.select(employee).select_from(join).where(department.c.name == 'haha') 
    # 员工下的部门信息
    # query = sqlalchemy.select(department).select_from(join).where(employee.c.name == 'jack3') 
    
    print(conn.execute(query).fetchall())