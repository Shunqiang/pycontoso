from declarative_sessionmaker import Session, Women


session = Session()

# result = session.query(Women).all()
# result = session.query(Women).filter(Women.adress == 'unknown').first()

# 使用first, 结果又都多条
# 使用one， 结果有且只有一条
# 使用scalar， 结果最多一条， 也可以没有

result = session.query(Women).filter(Women.name == 'jesse').update({
    Women.adress: 'beijing'
})

session.commit()
# for row in result:
# print(result.name, result.birthday, result.adress)