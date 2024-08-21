from db_init import Session, User, Role

def insert_records(s):
    role1 = Role(name='admin')
    role2 = Role(name='operate')
    user1 = User(name='jack', password='111',)
    user3 = User(name='rose', password='222',)
    user2 = User(name='jesse', password='333',)
    
    user1.roles.append(role1)
    user1.roles.append(role2)
    user2.roles.append(role1)
    user3.roles.append(role2)

    s.add_all([ user1, user2, user3])
    s.commit()
    
    
def select_user(s):
    u = s.query(User).filter(User.id == 1).first()
    print(u)
    print(u.roles)
# def select_role(s):
#     u = s.query(Role).filter(Role.id == 1).first()
#     print(u)
#     print(u.users)
session = Session()
insert_records(session)
# select_user(session)