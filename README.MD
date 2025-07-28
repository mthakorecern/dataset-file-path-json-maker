# Python Script to create a json file in the format

 "<dataset-name>": {
    "short_name": "<short-name>",
    "year": "<year>",
    "process": "<physics-process>",
    "xsec": <empty-placeholder-for-xsec>,
    "files": ["<filepath-with-redictor>"]
 }


 Usage: python3 obtain_rootfiles.py <datset-names-list.txt> <process-label> <name-of-output-json-file>