<img src="https://raw.githubusercontent.com/NeuroQuestAi/neuroquestai.github.io/main/brand/products/power-skills/power-skills-128.png" align="right" width="65" height="65"/>

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
export NQ_TOKEN="..."
```

To create an audio analysis, you must first transcribe the audio using [Spectrum API](https://github.com/NeuroQuestAi/neuroquest-examples/tree/main/products/spectrum) and 
obtain the audio analysis document ID.

```shell
export NQ_AUDIO_DOC_ID="q01vDxALebMNfDBKo33o"
```

`Note:` If you use the scripts.

### Login

```shell
curl -X POST https://api-power-skills.neuroquest.ai/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "bruce.wayne@neuroquest.ai", "password": "my-password"}' | jq .
```

Or check script: [01-auth-login](01-auth-login)

### Creating a text analysis

```shell
curl -X POST https://api-power-skills.neuroquest.ai/api/v1/predict/create/by-text \
  -H "Content-Type: application/json" \
  -H "token: my-token" \
  -d '{"name": "Gabriela Ehlert", "essay": "My text to be analyzed..."}' | jq .
```

Or check script: [03-predict-create-by-text](03-predict-create-by-text)

### Creating an audio analysis

To create an audio analysis, you must first transcribe the audio using the [Spectrum API](https://github.com/NeuroQuestAi/neuroquest-examples/tree/main/products/spectrum).

```shell
curl -X POST https://api-power-skills.neuroquest.ai/api/v1/predict/create/by-audio \
  -H "Content-Type: application/json" \
  -H "token: my-token" \
  -d '{"name": "Gabriela Ehlert", "document_id": "my-audio-id"}' | jq .
```

Or check script: [03-predict-create-by-audio](03-predict-create-by-audio)

### Logout

```shell
curl -X GET https://api-power-skills.neuroquest.ai/api/v1/auth/logout?email=bruce.wayne@neuroquest.ai \
  -H "Content-Type: application/json" \
  -H "token: my-token" | jq .
```

Or check script: [01-auth-logout](01-auth-logout)
