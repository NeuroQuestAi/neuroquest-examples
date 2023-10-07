<img src="https://raw.githubusercontent.com/NeuroQuestAi/neuroquestai.github.io/main/brand/logo/neuroquest-orange-logo.png" align="right" width="80" height="80"/>

# Using Rust 🚀

[![Powered by NeuroQuestAI](https://img.shields.io/badge/powered%20by-NeuroQuestAI-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](
https://neuroquest.ai)
![rustc](https://img.shields.io/static/v1.svg?label=rustc&message=1.70%20&color=orange)

Documentation of the **Persona Predict** API specification please access the address: [apis.neuroquest.ai/persona-predict](https://apis.neuroquest.ai/persona-predict/) for 
information about the *product* access the address: [docs.neuroquest.ai/persona-predict](https://docs.neuroquest.ai/persona-predict/)

To use **Persona Predict** with `rust`:

### Environment variables

Define the environment variables with your information:

```shell
export NQ_USER="my-email"
export NQ_PASSWORD="my-password"
export NQ_TOKEN=""
```

### Build

In this directory:

```shell
cargo build
```

### Login

```shell
cargo run -- --login
```

### Logout

```shell
cargo run -- --logout
```

For more details, use `cargo run -- --help`
