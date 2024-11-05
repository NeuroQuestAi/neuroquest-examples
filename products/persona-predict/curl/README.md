<img src="https://raw.githubusercontent.com/NeuroQuestAi/neuroquestai.github.io/main/brand/products/persona-predict/persona-predict-orange-128.png" align="right" width="65" height="65"/>

# Using Curl 🚀

[![Powered by NeuroQuestAI](https://img.shields.io/badge/powered%20by-NeuroQuestAI-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](
https://neuroquest.ai)
![curl](https://img.shields.io/static/v2.svg?label=curl&message=8.0%20&color=orange)

Documentation of the **Persona Predict** API specification please access the address: [apis.neuroquest.ai/persona-predict](https://apis.neuroquest.ai/persona-predict/) for 
information about the *product* access the address: [docs.neuroquest.ai/persona-predict](https://docs.neuroquest.ai/persona-predict/)

To use **Persona Predict V2** with `curl`:

### Environment variables

Define the environment variables with your information:

```shell
export NQ_EMAIL="my-email"
export NQ_PASSWORD="my-password"
```

`Note:` If you use the scripts.

### Login

```shell
curl -X POST https://api-persona-predict.neuroquest.ai/api/v2/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "morpheus@neuroquest.ai", "password": "my-password"}' | jq .
```

Or check script: [01-auth-login](01-auth-login). With JSON output, set the environment variable with your **token**:

```shell
export NQ_TOKEN="eyJhbGciOiJSUzI1NiIsI"
```

### Creating an analysis

```shell
curl -X POST https://api-persona-predict.neuroquest.ai/api/v2/predict/create \
  -H "Content-Type: application/json" \
  -H "token: my-token" \
  -d '{"name": "John Green", "essay": "My text to be analyzed..."}' | jq .
```

Or check script: [03-predict-create](03-predict-create). With JSON output, define the environment variable with your **essay**, it can be in **Portuguese** or **English**:

With JSON output, set the environment variable with your **essay**:

```shell
export NQ_ESSAY="My text here that will be analyzed..."
```

To create the analysis asynchronously/tasks, use the [03-predict-create-task](03-predict-create-task) script as examples.

### Logout

```shell
curl -X GET https://api-persona-predict.neuroquest.ai/api/v2/auth/logout?email=morpheus@neuroquest.ai \
  -H "Content-Type: application/json" \
  -H "token: my-token" | jq .
```

Or check script: [01-auth-logout](products/persona-predict/curl/01-auth-logout)

