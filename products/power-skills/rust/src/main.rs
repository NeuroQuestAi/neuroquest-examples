use reqwest;
use serde::{Deserialize, Serialize};
use std::env;

#[derive(Debug, Serialize, Deserialize)]
struct Login {
    email: String,
    password: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct EssayAudio {
    name: String,
    document_id: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct EssayText {
    name: String,
    essay: String,
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    if let (Ok(user), Ok(password), Ok(token), Ok(text), Ok(audio_document_id)) = (
        env::var("NQ_USER"),
        env::var("NQ_PASSWORD"),
        env::var("NQ_TOKEN"),
        env::var("NQ_ESSAY"),
        env::var("NQ_AUDIO_DOC_ID"),
    ) {
        let args: Vec<String> = env::args().collect();

        if args.len() < 2 {
            println!(
                "Usage: {} --login or --logout or --create-by-text or --create-by-audio",
                args[0]
            );
            return Ok(());
        }

        if args[1] == "--login" {
            api_predict_login(&user, &password).await?;
        } else if args[1] == "--logout" {
            api_predict_logout(&user, &token).await?;
        } else if args[1] == "--create-by-text" {
            api_predict_create_by_text(&text, &token).await?;
        } else if args[1] == "--create-by-audio" {
            api_predict_create_by_audio(&audio_document_id, &token).await?;
        } else {
            println!("Invalid option: {}", args[1]);
        }
    } else {
        println!(
            ">Environment variables not defined: NQ_USER or NQ_PASSWORD or NQ_TOKEN or NQ_ESSAY or NQ_AUDIO_DOC_ID"
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
        .post("https://api-power-skills.neuroquest.ai/api/v1/auth/login")
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
        "https://api-power-skills.neuroquest.ai/api/v1/auth/logout?email={}",
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

async fn api_predict_create_by_text(
    text: &str,
    token: &str,
) -> Result<(), Box<dyn std::error::Error>> {
    let data = EssayText {
        name: "Gabriela Ehlert".to_string(),
        essay: text.to_string(),
    };

    let res = reqwest::Client::new()
        .post("https://api-power-skills.neuroquest.ai/api/v1/predict/create/by-text")
        .header(reqwest::header::CONTENT_TYPE, "application/json")
        .header(reqwest::header::ACCEPT, "application/json")
        .header("token", token)
        .json(&data)
        .send()
        .await?;

    println!("{}", res.text().await?);
    Ok(())
}

async fn api_predict_create_by_audio(
    audio_document_id: &str,
    token: &str,
) -> Result<(), Box<dyn std::error::Error>> {
    let data = EssayAudio {
        name: "Gabriela Ehlert".to_string(),
        document_id: audio_document_id.to_string(),
    };

    let res = reqwest::Client::new()
        .post("https://api-power-skills.neuroquest.ai/api/v1/predict/create/by-audio")
        .header(reqwest::header::CONTENT_TYPE, "application/json")
        .header(reqwest::header::ACCEPT, "application/json")
        .header("token", token)
        .json(&data)
        .send()
        .await?;

    println!("{}", res.text().await?);
    Ok(())
}
