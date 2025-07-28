# Python Script to create a json file in the format

##  Usage: 
`
python3 obtain_rootfiles.py <datset-names-list.txt> <process-label> <name-of-output-json-file>`

Note: In case of choosing the redirectors, the possible and recommended options are 

- `"root://cmsxcache.hep.wisc.edu/"`
- `"root://cms-xrd-global.cern.ch/"`

## Json File format
Example:
<pre><code>```{
   "/WtoENu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM": {
       "short_name": "WtoENu_4Jets_TuneCP5_13p6TeV_madgraphMLM_v2-v2", 
       "year": "2024", 
       "process": "WJets", 
       "xsec": null, 
       "files": [ "root://cmsxcache.hep.wisc.edu//store/mc/RunIII2024Summer24NanoAODv15/WtoENu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/NANOAODSIM/150X_mcRun3_2024_realistic_v2-v2/2810000/2fff3c7f-1b85-4265-b549-eb655ddf2f27.root" ]
      }
   } ```</code></pre>
