#from google.cloud import bigquery
# import ibm_db_dbi
# import pandas as pd
# import datetime
# import pytz

class CDM_Compare:
  def __init__(self, V_Config_Project, V_Config_Dataset, V_Config_Table, V_Source_Count, V_Config_New_Table):
    self.V_Config_Project=V_Config_Project
    self.V_Config_Dataset = V_Config_Dataset
    self.V_Config_Table = V_Config_Table
    self.V_Source_Count = V_Source_Count
    self.V_Config_New_Table = V_Config_New_Table

    # Getting Last run date of the Table and Project
  def get_source_details(self,V_Source_Table):
    #bq_client = bigquery.Client(project=V_Config_Project)
    get_db2_query= "select DB2_SOURCE_LOAD_TIMESTAMP Last_DB2_Date, db2_record_count from `"+self.V_Config_Project+"."+self.V_Config_Dataset+"."+self.V_Config_New_Table+\
                   "` where db2_source_table = upper('"+V_Source_Table+"');"
    print(get_db2_query)
    return get_db2_query






