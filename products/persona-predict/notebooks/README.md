<img src="https://raw.githubusercontent.com/NeuroQuestAi/neuroquestai.github.io/main/brand/products/persona-predict/persona-predict-orange-128.png" align="right" width="65" height="65"/>

# Using Jupyter Notebook 🚀

[![Powered by NeuroQuestAI](https://img.shields.io/badge/powered%20by-NeuroQuestAI-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](
https://neuroquest.ai)
![jupyter](https://img.shields.io/static/v1.svg?label=jupyter&message=4.0.6%20&color=orange)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/NeuroQuestAi/neuroquest-examples/HEAD?labpath=products%2Fpersona-predict%2Fnotebooks)

Documentation of the **Persona Predict** API specification please access the address: [apis.neuroquest.ai/persona-predict](https://apis.neuroquest.ai/persona-predict/) for 
information about the *product* access the address: [docs.neuroquest.ai/persona-predict](https://docs.neuroquest.ai/persona-predict/)

To use **Persona Predict** with `jupyter-notebook`:

View with **NBViewer**:

Input of processed text in **American English** 🇺🇸:

 - [Persona-Predict-MySelf-EN-US](https://nbviewer.org/github/NeuroQuestAi/neuroquest-examples/blob/main/products/persona-predict/notebooks/Persona-Predict-MySelf-EN-US.ipynb?flush_cache=true)

Input of processed text in **Brazilian Portuguese** 🇧🇷:

  - [Persona-Predict-Eval-PT-BR](https://nbviewer.org/github/NeuroQuestAi/neuroquest-examples/blob/main/products/persona-predict/notebooks/Persona-Predict-Eval-PT-BR.ipynb?flush_cache=true)
  - [Persona-Predict-Batch-PT-BR](https://nbviewer.org/github/NeuroQuestAi/neuroquest-examples/blob/main/products/persona-predict/notebooks/Persona-Predict-Batch-PT-BR.ipynb?flush_cache=true)
  - [Persona-Predict-Population-PT-BR](https://nbviewer.org/github/NeuroQuestAi/neuroquest-examples/blob/main/products/persona-predict/notebooks/Persona-Predict-Pop-PT-BR.ipynb?flush_cache=true)
  - [Persona-Predict-Population-Confidence-PT-BR](https://nbviewer.org/github/NeuroQuestAi/neuroquest-examples/blob/main/products/persona-predict/notebooks/Persona-Predict-Pop-Conf-PT-BR.ipynb?flush_cache=true)

Or test directly in [Binder](https://mybinder.org/):

  - Run [Jupyter-Notebook in Binder](https://mybinder.org/v2/gh/NeuroQuestAi/neuroquest-examples/HEAD?labpath=products%2Fpersona-predict%2Fnotebooks)

Or use it on your machine by following the steps below.

`Note`: The raw model output can be found in the **raw_score** field. The value in the percentile field is specific to a population, representing a calibrated result. When there is no calibration for the population, the **raw_score** and **percentile** values will be identical.

### Environment variables 🛠️

Define the environment variables with your information:

```shell
export NQ_USER="my-email"
export NQ_PASSWORD="my-password"
```

Or create '**.env**' file in project root:

```file
NQ_USER=my-email
NQ_PASSWORD=my-password
```

### Build 🏗️

In this directory:

```shell
poetry shell && poetry update
```

Export requirements:

```shell
poetry update --only main && pip3 freeze > requirements.txt
```

### Start Notebook 🏁

```shell
jupyter lab
```
