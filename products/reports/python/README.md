<img src="https://raw.githubusercontent.com/NeuroQuestAi/neuroquestai.github.io/main/brand/products/reports/reports-128.png" align="right" width="65" height="65"/>

# Using Python 🚀

[![Powered by NeuroQuestAI](https://img.shields.io/badge/powered%20by-NeuroQuestAI-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](
https://neuroquest.ai)
![python](https://img.shields.io/static/v1.svg?label=python&message=3.11%20&color=orange)

Documentation of the **Reports** API specification please access the address: [apis.neuroquest.ai/reports](https://apis.neuroquest.ai/reports/) for 
information about the *product* access the address: [docs.neuroquest.ai/reports](https://docs.neuroquest.ai/reports/)

To use **Power Skills** with `python`:

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

`Note:` All variables must be defined. The audio file must be a minimum of 10 seconds and a maximum of 60 seconds.

### Build

In this directory:

```shell
poetry shell && poetry update
```

### Login

```shell
python report.py --login 
```

`Note:` After getting the token triggering the login endpoint. Redefine the environment variable: NQ_TOKEN

### Creating the report 

```shell
python report.py --create
```

### Logout

```shell
python report.py --logout
```

For more details, use `python report.py`
