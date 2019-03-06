from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "privateMCProduction_Step4_M1000"
config.General.workArea = 'crab_privateMCProduction'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName   = 'step4_MiniAOD_cfg.py'
config.JobType.numCores   = 4

config.section_("Data")
config.Data.userInputFiles = [
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_1.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_2.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_3.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_4.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_5.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_6.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_7.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_8.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_9.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_10.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_11.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_12.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_13.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_14.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_15.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_16.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_17.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_18.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_19.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_20.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_21.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_22.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_23.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_24.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_25.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_26.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_27.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_28.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_29.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_30.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_31.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_32.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_33.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_34.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_35.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_36.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_37.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_38.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_39.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_40.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_41.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_42.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_43.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_44.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_45.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_46.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_47.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_48.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_49.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_50.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_51.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_52.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_53.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_54.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_55.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_56.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_57.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_58.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_59.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_60.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_61.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_62.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_63.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_64.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_65.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_66.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_67.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_68.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_69.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_70.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_71.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_72.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_73.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_74.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_75.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_76.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_77.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_78.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_79.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_80.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_81.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_82.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_83.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step3_M1000/170709_142147/0000/step3_84.root',
]
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob  = 1
config.Data.totalUnits   = -1
config.Data.publication  = False

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
