
import re


full_name_pattern = r'^(.+)\(\d+\)$'

def filter_name(name: str):
    matcher = re.match(full_name_pattern, name)
    if (matcher):
        return matcher.group(1).strip()
    
    return name