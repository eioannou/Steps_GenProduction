from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName     = 'AToZH_M225_miniaod'
config.General.workArea        = 'M225_miniaod'
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName   = 'step5_MiniAODv2_M225_cfg.py'

config.section_("Data")
config.Data.userInputFiles = [
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_1.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_2.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_3.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_4.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_5.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_6.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_7.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_8.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_9.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_10.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_11.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_12.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_13.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_14.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_15.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_16.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_17.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_18.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_19.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_20.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_21.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_22.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_23.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_24.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_25.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_26.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_27.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_28.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_29.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_30.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_31.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_32.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_33.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_34.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_35.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_36.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_37.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_38.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_39.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_40.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_41.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_42.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_43.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_44.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_45.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_46.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_47.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_48.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_49.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_reHLT/161028_152623/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_reHLT_50.root'
]
config.Data.splitting      = 'FileBased'
config.Data.unitsPerJob    = 1
config.Data.totalUnits     = -1
config.Data.publication    = False

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
