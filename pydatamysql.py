import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
import xlrd

# mydb=mysql.connector.connect(host="localhost",user='root',passwd='root', database='sample')
# myc= mydb.cursor()
# myc.execute("select * from samtab")
# for i in myc:
#     print(i)
# myc.fetchall()
# myc.fetchone()



# mydb=mysql.connector.connect(host="localhost",user='root',passwd='root', database='pypandasql')
# cur=mydb.cursor()


# df=pd.read_csv("pokemon_data.csv")
# engine=create_engine('mysql://root:root@localhost/pypandasql')
 df.to_sql('new_pokemon',con=engine,if_exists='append',index=False,)

