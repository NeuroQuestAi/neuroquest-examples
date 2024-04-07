<img src="https://raw.githubusercontent.com/NeuroQuestAi/neuroquestai.github.io/main/brand/products/spectrum/spectrum-128.png" align="right" width="65" height="65"/>

# Using Curl 🚀

[![Powered by NeuroQuestAI](https://img.shields.io/badge/powered%20by-NeuroQuestAI-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](
https://neuroquest.ai)
![curl](https://img.shields.io/static/v1.svg?label=curl&message=8.0%20&color=orange)

Documentation of the **Spectrum** API specification please access the address: [apis.neuroquest.ai/spectrum](https://apis.neuroquest.ai/spectrum/) for 
information about the *product* access the address: [docs.neuroquest.ai/spectrum](https://docs.neuroquest.ai/spectrum/)

To use **Spectrum** with `curl`:

### Environment variables

Define the environment variables with your information:

```shell
export NQ_USER="my-email"
export NQ_PASSWORD="my-password"
```

`Note:` If you use the scripts.

### Login

```shell
curl -X POST https://api-spectrum.neuroquest.ai/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "joker@neuroquest.ai", "password": "my-password"}' | jq .
```

Or check script: [01-auth-login](01-auth-login)

### Audio to text

```shell
curl -X POST https://api-spectrum.neuroquest.ai/api/v1/audio/to-text \
  -H "Content-Type: multipart/form-data" \
  -F "audio_file=@audio/my-audio-file-en.way" \
  -F "audio_lang=en" \
  -H "token: my-token" | jq .
```

Or check script: [03-audio-to-text](03-audio-to-text)

### Logout

```shell
curl -X GET https://api-spectrum.neuroquest.ai/api/v1/auth/logout?email=joker@neuroquest.ai \
  -H "Content-Type: application/json" \
  -H "token: my-token" | jq .
```

Or check script: [01-auth-logout](01-auth-logout)

> Note: The audio files are examples only and were collected: [American Rhetoric](https://www.americanrhetoric.com/barackobamaspeeches.htm) and [Miller Center](https://millercenter.org/the-presidency/presidential-speeches/january-26-2018-address-world-economic-forum)
