<img src="https://raw.githubusercontent.com/NeuroQuestAi/neuroquestai.github.io/main/brand/products/power-skills/power-skills-128.png" align="right" width="80" height="80"/>

# Using Rust 🚀

[![Powered by NeuroQuestAI](https://img.shields.io/badge/powered%20by-NeuroQuestAI-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](
https://neuroquest.ai)
![rustc](https://img.shields.io/static/v1.svg?label=rustc&message=1.70%20&color=orange)

Documentation of the **Power Skills** API specification please access the address: [apis.neuroquest.ai/power-skills](https://apis.neuroquest.ai/power-skills/) for 
information about the *product* access the address: [docs.neuroquest.ai/persona-predict](https://docs.neuroquest.ai/power-skills/)

To use **Power Skills** with `rust`:

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
cargo build
```

### Login

```shell
cargo run -- --login
```

### Creating an analysis

```shell
cargo run -- --create
```

### Logout

```shell
cargo run -- --logout
```

For more details, use `cargo run -- --help`
