# Verification Blueprint

## Understanding the vulnerability
`GHSA-87vv-r9j6-g5qv` describes a vulnerability in the package `moment` version prior to 2.11.2. The vulnerability is triggered when arbitrary user input is passed into `moment.duration()`, results in denial of service.

## Quick check if OWASP Juice use "moment"
With command `npm ls moment`, we can check if the application is using `moment` package or if its dependencies are using `moment` package.
```
$ npm ls moment
juice-shop@18.0.0
├─┬ express-jwt@0.1.3
│ └─┬ jsonwebtoken@0.1.0
│   └── moment@2.0.0
├─┬ filesniffer@1.0.3
│ └─┬ filehound@1.17.6
│   ├── moment@2.30.1 deduped
│   └─┬ unit-compare@1.0.1
│     └── moment@2.30.1 deduped
├─┬ finale-rest@1.2.2
│ └── moment@2.30.1
└─┬ sequelize@6.37.7
  ├─┬ moment-timezone@0.5.48
  │ └── moment@2.30.1 deduped
  └── moment@2.30.1 deduped
```
We can see that many dependencies use `moment`. However, only `jsonwebtoken` uses the vulnerable version 2.0.0 (<2.11.2)

## Deep code analysis
Even though a vulnerable version of `moment` is used, it is not exploitable if it does not satisfy the condition : passing arbitrary user input into `moment.duration()`.

To be sure if the application is affected by `GHSA-87vv-r9j6-g5qv` or not, we need to analyze the code that uses `moment` which is `jsonwebtoken`

Checking `node_modules/express-jwt/node_modules/jsonwebtoken/index.js`, we see no usage of `moment.duration()`.

## Conclusion
OWASP Juice Shop is not affected by `GHSA-87vv-r9j6-g5qv`