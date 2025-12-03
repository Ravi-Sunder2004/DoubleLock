import re
import datetime
from pathlib import Path
import ujson
import logging


auth_log = Path('../logs/sample.log')



with open(auth_log,'r') as f:
    auth_log_lines = f.readlines()
    parsed_events = []
    
    for line in auth_log_lines:
        
        parsed_events.append(line.strip())
     


def export_to_json(parsed_events,output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path,'w') as f:

        ujson.dump(parsed_events,f,indent=4)
        

export_to_json(parsed_events,'./exported/auth_log.json')

