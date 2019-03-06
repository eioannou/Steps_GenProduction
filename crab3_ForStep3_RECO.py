from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName     = 'AToZH_M225_RECO'
config.General.workArea        = 'M225_RECO'
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName   = 'step3_RECO_M225_cfg.py'

config.section_("Data")
config.Data.userInputFiles = [
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_1.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_2.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_3.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_4.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_5.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_6.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_7.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_8.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_9.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_10.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_11.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_12.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_13.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_14.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_15.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_16.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_17.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_18.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_19.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_20.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_21.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_22.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_23.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_24.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_25.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_26.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_27.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_28.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_29.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_30.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_31.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_32.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_33.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_34.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_35.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_36.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_37.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_38.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_39.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_40.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_41.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_42.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_43.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_44.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_45.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_46.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_47.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_48.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_49.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_DIGI_HLT/161024_200407/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_step2_DIGI-HLT_50.root',
]
config.Data.splitting   = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits  = -1
config.Data.publication = False

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
