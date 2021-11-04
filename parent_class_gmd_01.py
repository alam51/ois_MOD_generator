from calendar import monthrange
import mysql.connector
import pandas as pd


# , equipment_id, time_query, equipment_type_query, power_voltage_energy_query
# def query(ss_id, equipment_type, mw_mvar_kwh_kvarh_kv_table_name, time_start, time_end):
#     query_str = f"""
# SELECT *
# FROM substation_equipment AS se
# JOIN {mw_mvar_kwh_kvarh_kv_table_name} AS x ON x.sub_equip_id = se.id
# -- JOIN mega_watt AS mw ON mw.sub_equip_id = se.id
# -- JOIN mega_var AS mvar ON mvar.sub_equip_id = se.id
# WHERE
# se.substation_id = {ss_id} AND
# se.is_{equipment_type} = 1 AND
# x.date_time BETWEEN '{time_start}' AND '{time_end}'
# """
#     # return


class Query:
    def __init__(self, ss_id, mw_mvar_kwh_kvarh_kv_table_name, time_start, time_end, equipment_type=None):
        self.sql_db = mysql.connector.connect(
            host='127.0.0.1',
            user="root",
            password="por1BABU",
            database="ois"
        )
        query_str = f"""
        SELECT *
        FROM substation_equipment AS se
        JOIN {mw_mvar_kwh_kvarh_kv_table_name} AS xy ON xy.sub_equip_id = se.id
        -- JOIN mega_watt AS mw ON mw.sub_equip_id = se.id
        -- JOIN mega_var AS mvar ON mvar.sub_equip_id = se.id
        WHERE 
        se.substation_id = {ss_id} AND
        -- se.is_{equipment_type} = 1 AND
        xy.date_time BETWEEN '{time_start}' AND '{time_end}'       
        """
        b = 5
        self.df = pd.read_sql_query(query_str, self.sql_db)


class Equipment:
    def __init__(self, ss_id, time_start, time_end):
        self.voltage_db = Query(ss_id=ss_id, mw_mvar_kwh_kvarh_kv_table_name='voltage',
                                time_start=time_start, time_end=time_end).df

        self.mw_db = Query(ss_id=ss_id, mw_mvar_kwh_kvarh_kv_table_name='mega_watt',
                           time_start=time_start, time_end=time_end).df

        self.mvar_db = Query(ss_id=ss_id, mw_mvar_kwh_kvarh_kv_table_name='mega_var',
                           time_start=time_start, time_end=time_end).df

        self.kwh_db = Query(ss_id=ss_id, mw_mvar_kwh_kvarh_kv_table_name='energy',
                           time_start=time_start, time_end=time_end).df


df = Equipment(21, '2021-8-11', '2021-8-12')
b = 4
