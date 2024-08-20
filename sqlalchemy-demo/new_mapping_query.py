from new_mapping import Session, Department, Employee


def insert_records(session):
    d1 = Department(name = 'hrsss')
    session.add(d1)
    e1 = Employee(dep_id=d1.id, name='jackss', birthday='2020-02-0112')

    session.add(e1)
    session.commit()
    
    
session = Session()

# p = Women(name = 'amy', birthday='2012-12-01', adress='unknown')

# session.add(p)

insert_records(session)