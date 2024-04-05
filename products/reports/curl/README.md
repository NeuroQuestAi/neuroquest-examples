<img src="https://raw.githubusercontent.com/NeuroQuestAi/neuroquestai.github.io/main/brand/products/reports/reports-128.png" align="right" width="65" height="65"/>

# Using Curl 🚀

[![Powered by NeuroQuestAI](https://img.shields.io/badge/powered%20by-NeuroQuestAI-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](
https://neuroquest.ai)
![curl](https://img.shields.io/static/v1.svg?label=curl&message=8.0%20&color=orange)

Documentation of the **Reports** API specification please access the address: [apis.neuroquest.ai/reports](https://apis.neuroquest.ai/reports/) for 
information about the *product* access the address: [docs.neuroquest.ai/reports](https://docs.neuroquest.ai/reports/)

To use **Reports** with `curl`:

### Environment variables

Define the environment variables with your information:

```shell
export NQ_USER="my-email"
export NQ_PASSWORD="my-password"
export NQ_TOKEN=""
export NQ_POWER_SKILLS_ANALYSIS_DOC_ID="..."
export NQ_REPORT_TEMPLATE="TNQ1"
export NQ_PROFILE_PICTURE="https://media.neuroquest.ai/reports/img/profile-1.png"
```

`Note:` If you use the scripts.

### Login

```shell
curl -X POST https://api-reports.neuroquest.ai/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "joker@neuroquest.ai", "password": "my-password"}' | jq .
```

Or check script: [01-auth-login](01-auth-login)

### Check service health

```shell
curl -X GET https://api-reports.neuroquest.ai/api/v1/health/check \
  -H "Content-Type: application/json" \
  -H "token: my-token" | jq .
```

Or check script: [02-health-check](02-health-check)

### Creating the report

```shell
curl -X POST https://api-reports.neuroquest.ai/api/v1/report/create \
  -H "Content-Type: application/json" \
  -H "token: my-token" \
  -d '{"document_id": "5aXKOmoTcFWccalUBmj6", \
       "profile_picture": "https://test.com/profile.png", \
       "report_template": "TNQ1"}' | jq .
```

Or check script: [03-report-create](03-report-create)

### Logout

```shell
curl -X GET https://api-reports.neuroquest.ai/api/v1/auth/logout?email=joker@neuroquest.ai \
  -H "Content-Type: application/json" \
  -H "token: my-token" | jq .
```

Or check script: [01-auth-logout](01-auth-logout)

