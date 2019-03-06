cmsDriver.py --filein file:GluGluToAToZhToLLBB_M350_13TeV-amcatnlo_reHLT.root --fileout file:GluGluToAToZhToLLBB_M350_13TeV-amcatnlo_MLM_4f_maxj1_PUSpring16_reHLT_80X_mcRun2_asymptotic_v14_MiniAODv2.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 80X_mcRun2_asymptotic_v14 --step PAT --era Run2_2016 --customise_commands "process.patTrigger.processName = cms.string('HLT2')" --python_filename step5_MiniAODv2_M350_cfg.py --customise Configuration/DataProcessing/Utils.addMonitoring --no_exec -n 50000