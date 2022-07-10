from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:Delfin173@falabella:3306/falabelladb")
meta = MetaData()
conn = engine.connect()