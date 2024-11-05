<img src="https://raw.githubusercontent.com/NeuroQuestAi/neuroquestai.github.io/main/brand/products/persona-predict/persona-predict-orange-128.png" align="right" width="65" height="65"/>

# Using Rust 🚀

[![Powered by NeuroQuestAI](https://img.shields.io/badge/powered%20by-NeuroQuestAI-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](
https://neuroquest.ai)
![rustc](https://img.shields.io/static/v1.svg?label=rustc&message=1.70%20&color=orange)

Documentation of the **Persona Predict** API specification please access the address: [apis.neuroquest.ai/persona-predict](https://apis.neuroquest.ai/persona-predict/) for 
information about the *product* access the address: [docs.neuroquest.ai/persona-predict](https://docs.neuroquest.ai/persona-predict/)

To use **Persona Predict V2** with `rust`:

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
cargo update && cargo build
```

### Login

```shell
cargo run -- --login
```

With JSON output, set the environment variable with your **token**:

```shell
export NQ_TOKEN="acKhbQcipiaSUzI1NiIDF"
```

### Creating an analysis

First define a text in the **NQ_ESSAY** variable:

```shell
export NQ_ESSAY="My text here that will be analyzed..."
```

Now create the analysis:

```shell
cargo run -- --create
```

### Logout

```shell
cargo run -- --logout
```

For more details, use `cargo run -- --help`
