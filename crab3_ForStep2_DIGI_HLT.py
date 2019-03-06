from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName     = 'AToZH_M225_DIGI_HLT'
config.General.workArea        = 'M225_DIGI_HLT'
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'step2_DIGI_HLT_M225_cfg.py'

config.section_("Data")
config.Data.userInputFiles = [
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_1.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_2.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_3.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_4.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_5.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_6.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_7.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_8.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_9.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_10.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_11.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_12.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_13.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_14.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_15.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_16.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_17.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_18.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_19.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_20.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_21.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_22.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_23.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_24.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_25.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_26.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_27.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_28.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_29.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_30.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_31.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_32.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_33.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_34.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_35.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_36.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_37.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_38.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_39.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_40.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_41.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_42.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_43.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_44.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_45.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_46.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_47.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_48.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_49.root',
'/store/user/aioannou/CRAB_UserFiles/crab_AToZH_M225_GEN_SIM/161019_103928/0000/GluGluToAToZhToLLBB_M225_13TeV-amcatnlo_GEN-SIM_50.root',
]
config.Data.splitting      = 'FileBased'
config.Data.unitsPerJob    = 1
config.Data.totalUnits     = -1
config.Data.publication    = False

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
