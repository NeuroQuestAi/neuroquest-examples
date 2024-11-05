use reqwest;
use serde::{Deserialize, Serialize};
use std::env;

#[derive(Debug, Serialize, Deserialize)]
struct Login {
    email: String,
    password: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct Essay {
    name: String,
    essay: String,
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    if let (Ok(user), Ok(password), Ok(token), Ok(text)) = (
        env::var("NQ_EMAIL"),
        env::var("NQ_PASSWORD"),
        env::var("NQ_TOKEN"),
        env::var("NQ_ESSAY"),
    ) {
        let args: Vec<String> = env::args().collect();

        if args.len() < 2 {
            println!("Usage: {} --login or --logout or --create", args[0]);
            return Ok(());
        }

        if args[1] == "--login" {
            api_predict_login(&user, &password).await?;
        } else if args[1] == "--logout" {
            api_predict_logout(&user, &token).await?;
        } else if args[1] == "--create" {
            api_predict_create(&text, &token).await?;
        } else {
            println!("Invalid option: {}", args[1]);
        }
    } else {
        println!(
            ">Environment variables not defined: NQ_EMAIL or NQ_PASSWORD or NQ_TOKEN or NQ_ESSAY"
        );
    }

    Ok(())
}

async fn api_predict_login(user: &str, password: &str) -> Result<(), Box<dyn std::error::Error>> {
    let data = Login {
        email: user.to_string(),
        password: password.to_string(),
    };

    let res = reqwest::Client::new()
        .post("https://api-persona-predict.neuroquest.ai/api/v2/auth/login")
        .header(reqwest::header::CONTENT_TYPE, "application/json")
        .header(reqwest::header::ACCEPT, "application/json")
        .json(&data)
        .send()
        .await?;

    println!("{}", res.text().await?);
    Ok(())
}

async fn api_predict_logout(user: &str, token: &str) -> Result<(), Box<dyn std::error::Error>> {
    let url = format!(
        "https://api-persona-predict.neuroquest.ai/api/v2/auth/logout?email={}",
        user
    );

    let res = reqwest::Client::new()
        .get(url)
        .header(reqwest::header::CONTENT_TYPE, "application/json")
        .header(reqwest::header::ACCEPT, "application/json")
        .header("token", token)
        .send()
        .await?;

    println!("{}", res.text().await?);
    Ok(())
}

async fn api_predict_create(text: &str, token: &str) -> Result<(), Box<dyn std::error::Error>> {
    let data = Essay {
        name: "John Green".to_string(),
        essay: text.to_string(),
    };

    let res = reqwest::Client::new()
        .post("https://api-persona-predict.neuroquest.ai/api/v2/predict/create")
        .header(reqwest::header::CONTENT_TYPE, "application/json")
        .header(reqwest::header::ACCEPT, "application/json")
        .header("token", token)
        .json(&data)
        .send()
        .await?;

    println!("{}", res.text().await?);
    Ok(())
}
