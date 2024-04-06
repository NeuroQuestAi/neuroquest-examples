<img src="https://raw.githubusercontent.com/NeuroQuestAi/neuroquestai.github.io/main/brand/products/reports/reports-128.png" align="right" width="65" height="65"/>

# Using Rust 🚀

[![Powered by NeuroQuestAI](https://img.shields.io/badge/powered%20by-NeuroQuestAI-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](
https://neuroquest.ai)
![rustc](https://img.shields.io/static/v1.svg?label=rustc&message=1.70%20&color=orange)

Documentation of the **Reports** API specification please access the address: [apis.neuroquest.ai/reports](https://apis.neuroquest.ai/reports/) for 
information about the *product* access the address: [docs.neuroquest.ai/reports](https://docs.neuroquest.ai/reports/)

To use **Reports** with `rust`:

### Environment variables

Define the environment variables with your information:

```shell
export NQ_USER="my-email"
export NQ_PASSWORD="my-password"
export NQ_TOKEN="..."
export NQ_POWER_SKILLS_ANALYSIS_DOC_ID="..."
export NQ_REPORT_TEMPLATE="TNQ1"
export NQ_PROFILE_PICTURE="https://media.neuroquest.ai/reports/img/profile-1.png"
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

### Creating the reports

```shell
cargo run -- --create
```

### Logout

```shell
cargo run -- --logout
```

For more details, use `cargo run -- --help`
