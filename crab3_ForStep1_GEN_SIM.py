from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName     = 'AToZH_M225_GEN_SIM'
config.General.workArea        = 'M225_GEN_SIM'       
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName   = 'step1_GEN_SIM_M225_cfg.py'

config.section_("Data")
config.Data.userInputFiles = [
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_1.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_2.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_3.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_4.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_5.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_6.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_7.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_8.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_9.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_10.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_11.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_12.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_13.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_14.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_15.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_16.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_17.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_18.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_19.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_20.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_21.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_22.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_23.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_24.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_25.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_26.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_27.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_28.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_29.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_30.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_31.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_32.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_33.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_34.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_35.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_36.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_37.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_38.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_39.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_40.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_41.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_42.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_43.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_44.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_45.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_46.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_47.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_48.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_49.root',
'/store/user/aioannou/CRAB_PrivateMC/crab_AToZh_M225_LHE/161018_203838/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_LHE_50.root'
]
config.Data.splitting      = 'FileBased'
#config.Data.inputDBS       = 'phys03'
config.Data.unitsPerJob    = 1
config.Data.totalUnits     = -1
config.Data.publication    = False

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'

