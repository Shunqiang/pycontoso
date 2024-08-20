from one_to_many_orm import Session, Department, Employee

def insert_records(session):
    d1 = Department(name = 'hr1')
    e1 = Employee(department=d1, name='jack1', birthday='2020-02-01')
    session.add(e1)
    session.commit()


def select_records(session):
    department = session.query(Department).filter(Department.name == 'hr').one()
   
    print(department)
    print(department.employees)
    
def select_records_em(session):
    em = session.query(Employee).filter(Employee.name == 'jacks').one()

    print(em)
    print(em.department)
session = Session()
# select_records(session)
select_records_em(session)
