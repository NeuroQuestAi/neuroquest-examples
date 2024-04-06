use reqwest;
use serde::{Deserialize, Serialize};
use std::env;

#[derive(Debug, Serialize, Deserialize)]
struct Login {
    email: String,
    password: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct Report {
    document_id: String,
    report_template: String,
    profile_picture: String,
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    if let (Ok(user), Ok(password), Ok(token), Ok(document_id), Ok(report_template), Ok(profile_picture)) = (
        env::var("NQ_USER"),
        env::var("NQ_PASSWORD"),
        env::var("NQ_TOKEN"),
        env::var("NQ_POWER_SKILLS_ANALYSIS_DOC_ID"),
        env::var("NQ_REPORT_TEMPLATE"),
        env::var("NQ_PROFILE_PICTURE"),
    ) {
        let args: Vec<String> = env::args().collect();

        if args.len() < 2 {
            println!("Usage: {} --login or --logout or --create", args[0]);
            return Ok(());
        }

        if args[1] == "--login" {
            api_report_login(&user, &password).await?;
        } else if args[1] == "--logout" {
            api_report_logout(&user, &token).await?;
        } else if args[1] == "--create" {
            api_report_create(&document_id, &report_template, &profile_picture, &token).await?;
        } else {
            println!("Invalid option: {}", args[1]);
        }
    } else {
        println!(
            ">Environment variables not defined: NQ_USER | NQ_PASSWORD | NQ_TOKEN | NQ_POWER_SKILLS_ANALYSIS_DOC_ID | NQ_REPORT_TEMPLATE | NQ_PROFILE_PICTURE"
        );
    }

    Ok(())
}

async fn api_report_login(user: &str, password: &str) -> Result<(), Box<dyn std::error::Error>> {
    let data = Login {
        email: user.to_string(),
        password: password.to_string(),
    };

    let res = reqwest::Client::new()
        .post("https://api-reports.neuroquest.ai/api/v1/auth/login")
        .header(reqwest::header::CONTENT_TYPE, "application/json")
        .header(reqwest::header::ACCEPT, "application/json")
        .json(&data)
        .send()
        .await?;

    println!("{}", res.text().await?);
    Ok(())
}

async fn api_report_logout(user: &str, token: &str) -> Result<(), Box<dyn std::error::Error>> {
    let url = format!(
        "https://api-reports.neuroquest.ai/api/v1/auth/logout?email={}",
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

async fn api_report_create(document_id: &str, report_template: &str, profile_picture: &str, token: &str) -> Result<(), Box<dyn std::error::Error>> {
    let data = Report {
        document_id: document_id.to_string(),
        report_template: report_template.to_string(),
        profile_picture: profile_picture.to_string(),
    };

    let res = reqwest::Client::new()
        .post("https://api-reports.neuroquest.ai/api/v1/report/create")
        .header(reqwest::header::CONTENT_TYPE, "application/json")
        .header(reqwest::header::ACCEPT, "application/json")
        .header("token", token)
        .json(&data)
        .send()
        .await?;

    println!("{}", res.text().await?);
    Ok(())
}
