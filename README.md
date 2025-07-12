# js-vuln-analysis

## Instalation Requirements

`pip install -r requirements.txt`

## Filtering and Extracting information from OSV
NOTE: This setup is entirely for the purpose of analysing JS-related vulnerabilities disclosed in the last 12 months so the configuration of the script is hard-coded. Feel free to change them :)

`npm_all.zip` contains all JavaScript-related vulnerabilities descriptions in OSV schemas (in json). You can download it from [OSV](https://storage.googleapis.com/osv-vulnerabilities/index.html?prefix=npm/) (scroll to the bottom). Extract it into `./Vulnerabilities`

`main.py` will iterate all the json files to filter and extract information. `main.py` will create 2 files `list_vuln.txt` and `details.json`.

`list_vuln.txt` contains name of files after filtering.

`details.json` contains reduced OSV schema information that useful for vulnerability detection:
- `id` : vulnerability ID
- `name` : name of package affected
- `ranges` : the range of version affected
- `versions` : list of version affected
- `severity` : severity in CVSS score
- `details` : short description of the vulnerability

Friendly Reminder : Check before cloning ([CVE-2025-48384](https://securitylabs.datadoghq.com/articles/git-arbitrary-file-write/))