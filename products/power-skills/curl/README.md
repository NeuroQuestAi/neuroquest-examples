<img src="https://raw.githubusercontent.com/NeuroQuestAi/neuroquestai.github.io/main/brand/products/power-skills/power-skills-128.png" align="right" width="80" height="80"/>

# Using Curl 🚀

[![Powered by NeuroQuestAI](https://img.shields.io/badge/powered%20by-NeuroQuestAI-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](
https://neuroquest.ai)
![curl](https://img.shields.io/static/v1.svg?label=curl&message=8.0%20&color=orange)

Documentation of the **Power Skills** API specification please access the address: [apis.neuroquest.ai/power-skills](https://apis.neuroquest.ai/power-skills/) for 
information about the *product* access the address: [docs.neuroquest.ai/power-skills](https://docs.neuroquest.ai/power-skills/)

To use **Power Skills** with `curl`:

### Environment variables

Define the environment variables with your information:

```shell
export NQ_USER="my-email"
export NQ_PASSWORD="my-password"
export NQ_TOKEN=""
export NQ_ESSAY="My text..."
```

`Note:` If you use the scripts.

### Login

```shell
curl -X POST https://api-power-skills.neuroquest.ai/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "bruce.wayne@neuroquest.ai", "password": "my-password"}' | jq .
```

Or check script: [01-auth-login](01-auth-login)

### Creating an analysis

```shell
curl -X POST https://api-power-skills.neuroquest.ai/api/v1/predict/create \
  -H "Content-Type: application/json" \
  -H "token: my-token" \
  -d '{"name": "Gabriela Ehlert", "essay": "My text to be analyzed..."}' | jq .
```

Or check script: [03-predict-create](03-predict-create)

You can also use **audio**, see: [04-predict-create](04-predict-create)

### Logout

```shell
curl -X GET https://api-power-skills.neuroquest.ai/api/v1/auth/logout?email=bruce.wayne@neuroquest.ai \
  -H "Content-Type: application/json" \
  -H "token: my-token" | jq .
```

Or check script: [01-auth-logout](01-auth-logout)

### Audio 

Instead of sending text, you can also send an audio. Wav or ogg format can be used. See more at: [04-predict-create](04-predict-create)

> Note: The audio files are examples only and were collected: [American Rhetoric](https://www.americanrhetoric.com/barackobamaspeeches.htm)

