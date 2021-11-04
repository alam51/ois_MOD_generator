from calendar import monthrange
import mysql.connector
import pandas as pd

sql_connector = mysql.connector.connect(
    host='127.0.0.1',
    user="root",
    password="por1BABU",
    database="ois"
)

query_ss_equipments = f"""
SELECT ss.name as ss_name, ss.id AS ss_id, se.name as eq_name, se.id AS eq_id
FROM substation_equipment AS se
JOIN substation AS ss ON se.substation_id = ss.id
ORDER BY ss_id
"""

df = pd.read_sql_query(query_ss_equipments, sql_connector)
# ss_equipments_df1 = ss_equipments_df.set_index(['eq_id'])
df1 = df[df.duplicated(keep=False, subset=['ss_id', 'eq_name']) == True]
df2 = df1.sort_values(by=['ss_id', 'eq_name'], )
df2.to_excel('duplicate_equipments.xlsx', index=None)
a = 5
