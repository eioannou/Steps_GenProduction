from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "privateMCProduction_Step3_M1000"
config.General.workArea = 'crab_privateMCProduction'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName   = 'step3_RECO_cfg.py'
config.JobType.numCores   = 4

config.section_("Data")
config.Data.userInputFiles = [
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_1.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_2.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_3.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_4.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_5.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_6.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_7.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_8.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_9.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_10.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_11.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_12.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_13.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_14.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_15.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_16.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_17.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_18.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_19.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_20.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_21.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_22.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_23.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_24.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_25.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_26.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_27.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_28.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_29.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_30.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_31.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_32.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_33.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_34.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_35.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_36.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_37.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_38.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_39.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_40.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_41.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_42.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_43.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_44.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_45.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_46.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_47.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_48.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_49.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_50.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_51.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_52.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_53.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_54.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_55.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_56.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_57.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_58.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_59.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_60.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_61.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_62.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_63.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_64.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_65.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_66.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_67.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_68.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_69.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_70.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_71.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_72.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_73.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_74.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_75.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_76.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_77.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_78.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_79.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_80.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_81.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_82.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_83.root',
'/store/user/aioannou/CRAB_UserFiles/crab_privateMCProduction_Step2_M1000/170707_072355/0000/step2_84.root',
]
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob  = 1
config.Data.totalUnits   = -1
config.Data.publication  = False

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
