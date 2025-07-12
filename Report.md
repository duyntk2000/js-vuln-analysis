# JavaScript-Ecosystem Snapshot
## Pulling Vulnerabilities from OSV
The interest is to find all vulnerabilities that relate to JavaScript and were disclosed within the last 12 months. The OSV API doesn't allow filter vulnerabilities by time range. Luckily, the completed database is [published](https://storage.googleapis.com/osv-vulnerabilities/index.html).

## Vulnerabilities Analysis
The quickest way to detect these vulnerabilities is through checking the package versions. The vulnerable versions can be deducted through the fields:
- "ranges" - the vulnerable version will be between : 
    - "ranges" -> "event" -> "introduced" - the first vulnerable version
    - "ranges" -> "event" -> "fixed" - the fixed version

- "versions" - list of vulnerable versions

The more precise way is analyzing the "details" field to get which functions actually matter

## Vulnerability Severity
It is recommended to tackle the vulnerabilities with prefix "MAL" in the name first because these are packages that contain malicious code meaning applications using them have high chance to be compromised.

For the rest of vulnerabilites, we can order them base on :
- The "severity" fields (The CVSS score)
- The popularity of the package
- The EPSS score (exploit prediction)