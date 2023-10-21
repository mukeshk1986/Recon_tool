import DB2_BQ_Reconn_Library as TCS

if __name__ == '__main__':
  V_Config_Project='edp-prod-hcbstorage'
  V_Config_Dataset='edp_hcb_core_src'
  V_Config_Table='T_DB2_BQ_RECON_CONFIG'
  V_Source_Count='T_DB2_STRATEGIC_COUNT'
  V_Config_New_Table='T_DB2_BQ_STRATEGIC_COUNT'
  cdmc = TCS.CDM_Compare(V_Config_Project, V_Config_Dataset, V_Config_Table, V_Source_Count, V_Config_New_Table)
  print(cdmc.V_Config_Dataset)
  print(cdmc.get_source_details('Source Table'))

