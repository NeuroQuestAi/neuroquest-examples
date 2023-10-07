<img src="https://raw.githubusercontent.com/NeuroQuestAi/neuroquestai.github.io/main/brand/logo/neuroquest-orange-logo.png" align="right" width="80" height="80"/>

# Using Curl 📃

[![Powered by NeuroQuestAI](https://img.shields.io/badge/powered%20by-NeuroQuestAI-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](
https://neuroquest.ai)
![curl](https://img.shields.io/static/v1.svg?label=curl&message=8.0%20&color=orange)

Documentation of the **Persona Predict** API specification please access the address: [apis.neuroquest.ai/persona-predict](https://apis.neuroquest.ai/persona-predict/) for 
information about the *product* access the address: [docs.neuroquest.ai/persona-predict](https://docs.neuroquest.ai/persona-predict/)

To use **Persona Predict** with `curl`:

### Login

```shell
curl -X POST https://api-persona-predict.neuroquest.ai/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "morpheus@neuroquest.ai", "password": "my-password"}' | jq .
```

Or check script: [01-auth-login](products/persona-predict/curl/01-auth-login)

### Creating an analysis

```shell
curl -X POST https://api-persona-predict.neuroquest.ai/api/v1/predict/create \
  -H "Content-Type: application/json" \
  -H "token: my-token" \
  -d '{"name": "John Green", "essay": "My text to be analyzed..."}' | jq .
```

### Logout

```shell
curl -X GET https://api-persona-predict.neuroquest.ai/api/v1/auth/logout?email=morpheus@neuroquest.ai \
  -H "Content-Type: application/json" \
  -H "token: my-token" | jq .
```

Or check script: [01-auth-logout](products/persona-predict/curl/01-auth-logout)


