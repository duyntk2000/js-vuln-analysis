import os
import json
import pytz

from datetime import datetime, timedelta
from dateutil import parser

def get_analysis(data):
    extracted_list = []
    affected_list = data.get("affected")
    for affected in affected_list:
        package = affected.get("package")
        if package.get("ecosystem") != "npm":
            continue

        ident = data.get("id")
        ranges = affected.get("ranges")
        versions = affected.get("versions")
        severity = data.get("severity")
        details = data.get("details")
        extracted = {
            "id" : ident,
            "name" : package.get("name"),
            "ranges" : ranges,
            "versions" : versions,
            "severity" : severity,
            "details" : details
        }
        extracted_list.append(extracted)
    return extracted_list

if __name__ == "__main__":
    now = datetime.now(pytz.utc)
    one_year_ago = now - timedelta(days=365)
    recent_vuln = []
    details = []

    #Path to folder containning vulnerability details
    folder = "./Vulnerabilities"
    for filename in os.listdir(folder):
        if filename.endswith('.json'):
            full_path = os.path.join(folder, filename)
            with open(full_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            published_str = data.get("published")
            if published_str:
                published_date = parser.parse(published_str)
                if one_year_ago <= published_date <= now:
                    recent_vuln.append(filename)
                    details += get_analysis(data)

    with open("details.json", "w") as v:
        json.dump(details, v, indent=2)

    with open("./list_vuln.txt", "w") as f:
        for vuln in recent_vuln:
            f.write(f"{vuln}\n")
