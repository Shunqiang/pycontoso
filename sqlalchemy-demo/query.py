from declarative_sessionmaker import Session, Women

session = Session()

# p = Women(name = 'amy', birthday='2012-12-01', adress='unknown')

# session.add(p)

p_list = [
    Women(name = 'tina', birthday='2012-12-01', adress='unknown'),
    Women(name = 'tom', birthday='2011-12-01', adress='unknown'),
    Women(name = 'jesse', birthday='2010-12-01', adress='unknown')
]
session.add_all(p_list)
session.commit()