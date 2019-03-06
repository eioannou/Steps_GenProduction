from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "privateMCProduction_Step2_M1000"
config.General.workArea = 'crab_privateMCProduction'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName   = 'step2_cfg.py'
config.JobType.numCores   = 4

config.section_("Data")
config.Data.userInputFiles = [
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_1.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_2.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_3.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_4.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_5.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_6.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_7.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_8.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_9.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_10.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_11.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_12.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_13.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_14.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_15.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_16.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_17.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_18.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_19.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_20.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_21.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_22.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_23.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_24.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_25.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_26.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_27.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_28.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_29.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_30.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_31.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_32.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_33.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_34.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_35.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_36.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_37.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_38.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_39.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_40.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_41.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_42.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_43.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_44.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_45.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_46.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_47.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_48.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_49.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_50.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_51.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_52.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_53.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_54.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_55.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_56.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_57.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_58.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_59.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_60.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_61.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_62.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_63.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_64.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_65.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_66.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_67.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_68.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_69.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_70.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_71.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_72.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_73.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_74.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_75.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_76.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_77.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_78.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_79.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_80.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_81.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_82.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_83.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_privateMCProduction_Step1_M1000/170706_192401/0000/step1_84.root',
]
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob  = 1
config.Data.totalUnits   = -1
config.Data.publication  = False

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
