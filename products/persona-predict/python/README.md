<img src="https://raw.githubusercontent.com/NeuroQuestAi/neuroquestai.github.io/main/brand/products/persona-predict/persona-predict-orange-128.png" align="right" width="65" height="65"/>

# Using Python 🚀

[![Powered by NeuroQuestAI](https://img.shields.io/badge/powered%20by-NeuroQuestAI-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](
https://neuroquest.ai)
![python](https://img.shields.io/static/v1.svg?label=python&message=3.11%20&color=orange)

Documentation of the **Persona Predict** API specification please access the address: [apis.neuroquest.ai/persona-predict](https://apis.neuroquest.ai/persona-predict/) for 
information about the *product* access the address: [docs.neuroquest.ai/persona-predict](https://docs.neuroquest.ai/persona-predict/)

To use **Persona Predict V2** with `python`:

### Environment variables

Define the environment variables with your information:

```shell
export NQ_EMAIL="my-email"
export NQ_PASSWORD="my-password"
export NQ_TOKEN=""
export NQ_ESSAY=""
```

### Build

In this directory:

```shell
poetry shell && poetry update
```

### Login

```shell
python predict.py --login 
```

### Creating an analysis

```shell
python predict.py --create
```

### Logout

```shell
python predict.py --logout
```

For more details, use `python predict.py`
