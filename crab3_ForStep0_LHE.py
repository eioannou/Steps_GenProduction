from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName     = 'AToZh_M225_LHE'
config.General.workArea        = 'M225_LHE'
config.General.transferOutputs = True
#config.General.transferLogs    = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName   = 'step0_LHE_M225_cfg.py'
config.JobType.generator  = 'lhe'
#config.JobType.inputFiles  = ['GluGluToAToZhToLLBB_M250_13TeV-amcatnlo_LHE.lhe']

config.section_("Data")
#config.Data.userInputFiles   = ['/store/user/aioannou/LHE_Files/GluGluToAToZhToLLBB_M250_13TeV-amcatnlo_LHE.lhe']
config.Data.inputDBS         = 'phys03'
config.Data.splitting        = 'EventBased'
config.Data.unitsPerJob      = 1000
config.Data.totalUnits       = 50000
#config.Data.outLFNDirBase    = '/store/user/aioannou/'
config.Data.publication      = False
#config.Data.publishDbsUrl    = 'phys03'
#config.Data.outputDatasetTag = 'GluGluAToZhLLBB_LHE_STEP-0'

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
