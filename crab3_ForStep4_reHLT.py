from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName     = 'AToZH_M225_reHLT'
config.General.workArea        = 'M225_reHLT'
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName   = 'step4_reHLT_M225_cfg.py'

config.section_("Data")
config.Data.userInputFiles = [
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_1.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_2.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_3.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_4.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_5.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_6.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_7.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_8.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_9.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_10.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_11.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_12.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_13.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_14.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_15.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_16.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_17.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_18.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_19.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_20.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_21.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_22.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_23.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_24.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_25.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_26.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_27.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_28.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_29.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_30.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_31.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_32.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_33.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_34.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_35.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_36.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_37.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_38.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_39.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_40.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_41.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_42.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_43.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_44.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_45.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_46.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_47.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_48.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_49.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_RECO/161026_151925/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step3_RECO_50.root',
]
config.Data.splitting      = 'FileBased'
config.Data.unitsPerJob    = 1
config.Data.totalUnits     = -1
config.Data.publication    = False

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
