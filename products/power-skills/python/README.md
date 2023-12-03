<img src="https://raw.githubusercontent.com/NeuroQuestAi/neuroquestai.github.io/main/brand/products/power-skills/power-skills-128.png" align="right" width="80" height="80"/>

# Using Python 🚀

[![Powered by NeuroQuestAI](https://img.shields.io/badge/powered%20by-NeuroQuestAI-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](
https://neuroquest.ai)
![python](https://img.shields.io/static/v1.svg?label=python&message=3.11%20&color=orange)

Documentation of the **Power Skills** API specification please access the address: [apis.neuroquest.ai/power-skills](https://apis.neuroquest.ai/power-skills/) for 
information about the *product* access the address: [docs.neuroquest.ai/power-skills](https://docs.neuroquest.ai/power-skills/)

To use **Power Skills** with `python`:

### Environment variables

Define the environment variables with your information:

```shell
export NQ_USER="my-email"
export NQ_PASSWORD="my-password"
export NQ_TOKEN="test"
export NQ_ESSAY="My text..."
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
