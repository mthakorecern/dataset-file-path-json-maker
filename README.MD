# Python Script to create a json file in the format

##  Usage: python3 obtain_rootfiles.py <datset-names-list.txt> <process-label> <name-of-output-json-file>

 Note: In case of choosing the redirectors, the possible and recommended options are 
- "root://cmsxcache.hep.wisc.edu/"
- ""root://cms-xrd-global.cern.ch/"

## Json File format
 "dataset-name": {
    "short_name": "short-name",
    "year": "year",
    "process": "physics-process",
    "xsec": empty-placeholder-for-xsec,
    "files": ["filepath-with-redictor"]
 }


