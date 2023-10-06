use std::env;
use serde::{Deserialize, Serialize};
use reqwest;

#[derive(Debug, Serialize, Deserialize)]
struct Login {
    email: String,
    password: String,
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        println!("Usage: {} --login", args[0]);
        return Ok(());
    }

    if args[1] == "--login" {
        api_predict_login().await?;
    } else {
        println!("Invalid option: {}", args[1]);
    }

    Ok(())
}

async fn api_predict_login() -> Result<(), Box<dyn std::error::Error>> {
    let data = Login {
        email: "ederbsd@gmail.com".into(),
        password: "oraculo045".into(),
    };

    let res = reqwest::Client::new()
        .post("https://api-persona-predict.neuroquest.ai/api/v1/auth/login")
        .json(&data)
        .send()
        .await?;

    println!("{}", res.text().await?);
    Ok(())
}

