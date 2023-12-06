import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import seaborn as sns


def login(user: str, password: str) -> dict:
    resp = requests.post(
        "https://api-persona-predict.neuroquest.ai/api/v1/auth/login",
        headers={"Content-Type": "application/json"},
        json={"email": user, "password": password},
    )
    if resp.status_code == 200:
        return resp.json()
    print(f"Erro: {resp.status_code} - {resp.text}")
    return {}


def predict_create(token: str, data: dict, save_result: bool = False) -> dict:
    resp = requests.post(
        "https://api-persona-predict.neuroquest.ai/api/v1/predict/create",
        headers={"Content-Type": "application/json", "token": token},
        json=data,
    )
    if resp.status_code == 201:
        data = resp.json()
        if save_result:
            with open("predict-result.json", "w") as f:
                json.dump(data, f)
        return data
    print(f"Erro: {resp.status_code} -> {resp.text}")
    return {}


def get_predict_result_in_file() -> dict:
    with open("predict-result.json", "r") as f:
        data = json.load(f)
    return data


def get_my_txt_essay(lang: str = "en") -> str:
    if lang == "en":
        return " ".join(str(open("my-essay-en.txt", "r").read()).split())
    elif lang == "pt":
        return " ".join(str(open("my-essay-pt.txt", "r").read()).split())
    raise ValueError("Essay not found!")


def get_big_five(x: dict) -> dict:
    return {
        "O": x.get("openness").get("result"),
        "C": x.get("conscientiousness").get("result"),
        "E": x.get("extraversion").get("result"),
        "A": x.get("agreeableness").get("result"),
        "N": x.get("neuroticism").get("result"),
    }


def plot_big_five_bar(score_big_five: list) -> str:
    sns.set(style="whitegrid", rc={"grid.linewidth": 0.5})

    df = pd.DataFrame.from_dict(
        score_big_five[0], orient="index", columns=["Percentage"]
    ).reset_index()
    df = df.rename(columns={"index": "Trait"})
    custom_colors = ["#577EF3", "#3996DF", "#43C386", "#FDCB1E", "#F57C1A"]

    plt.figure(figsize=(12, 6))
    sns.barplot(
        data=df,
        x="Trait",
        y="Percentage",
        palette=custom_colors,
        hue="Trait",
        legend=False,
    )

    for x, y in zip(df["Percentage"], plt.gca().patches):
        plt.gca().annotate(
            f"{x:.2f}%",
            (y.get_x() + y.get_width() / 2, y.get_height()),
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
        )

    plt.xlabel("Traits")
    plt.ylabel("Percentage")
    plt.title("Big-Five Personality")

    plt.xticks(rotation=0)
    plt.tight_layout()

    plt.savefig("plots/big_five_plot_bar.png", bbox_inches="tight")
    plt.close()

    return "<center><img src='plots/big_five_plot_bar.png'/></center>"


def plot_big_five_radar(score_big_five: list) -> str:
    keys = list(score_big_five[0].keys())
    percentile = list(score_big_five[0].values())

    keys.append(keys[0])
    percentile.append(percentile[0])

    fig, ax = plt.subplots(figsize=(12, 6), subplot_kw={"polar": True})

    angles = np.linspace(0, 2 * np.pi, len(keys), endpoint=True)

    ax.plot(
        angles,
        percentile,
        "b",
        linestyle="solid",
        linewidth=1,
        marker="o",
        markersize=7,
        label="Score",
    )
    ax.fill(angles, percentile, "b", alpha=0.1)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(keys[:-1])

    plt.title("Big-Five Personality")
    plt.legend(loc="upper right")

    plt.savefig("plots/big_five_plot_radar.png", bbox_inches="tight")
    plt.close()

    return "<center><img src='plots/big_five_plot_radar.png'/></center>"


def plot_big_five_openness_facets_bar(score_openness_facets: list) -> str:
    sns.set(style="whitegrid", rc={"grid.linewidth": 0.5})
    traits = [list(item.values())[1] for item in score_openness_facets]
    scores = [list(item.values())[2] for item in score_openness_facets]

    df = pd.DataFrame({"Trait": traits, "Percentage": scores})

    plt.figure(figsize=(12, 6))
    colors = sns.color_palette("light:b", len(traits))

    sns.barplot(
        data=df, x="Trait", y="Percentage", palette=colors, hue="Trait", legend=False
    )

    for x, bar in zip(scores, plt.gca().patches):
        plt.gca().annotate(
            f"{x:.2f}%",
            (bar.get_x() + bar.get_width() / 2, bar.get_height()),
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
        )

    plt.xlabel("Traits")
    plt.ylabel("Percentage")
    plt.title("Openness Facets")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("plots/big_five_openness_facets_plot_bar.png", bbox_inches="tight")
    plt.close()

    return "<center><img src='plots/big_five_openness_facets_plot_bar.png'/></center>"


def plot_big_five_conscientiousness_facets_bar(
    score_conscientiousness_facets: list,
) -> str:
    sns.set(style="whitegrid", rc={"grid.linewidth": 0.5})
    traits = [list(item.values())[1] for item in score_conscientiousness_facets]
    scores = [list(item.values())[2] for item in score_conscientiousness_facets]

    df = pd.DataFrame({"Trait": traits, "Percentage": scores})

    plt.figure(figsize=(12, 6))
    colors = sns.color_palette("Blues", len(traits))

    sns.barplot(
        data=df, x="Trait", y="Percentage", palette=colors, hue="Trait", legend=False
    )

    for x, bar in zip(scores, plt.gca().patches):
        plt.gca().annotate(
            f"{x:.2f}%",
            (bar.get_x() + bar.get_width() / 2, bar.get_height()),
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
        )

    plt.xlabel("Traits")
    plt.ylabel("Percentage")
    plt.title("Conscientiousness Facets")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        "plots/big_five_conscientiousness_facets_plot_bar.png", bbox_inches="tight"
    )
    plt.close()

    return "<center><img src='plots/big_five_conscientiousness_facets_plot_bar.png'/></center>"


def plot_big_five_extraversion_facets_bar(
    score_extraversion_facets: list,
) -> str:
    sns.set(style="whitegrid", rc={"grid.linewidth": 0.5})
    traits = [list(item.values())[1] for item in score_extraversion_facets]
    scores = [list(item.values())[2] for item in score_extraversion_facets]

    df = pd.DataFrame({"Trait": traits, "Percentage": scores})

    plt.figure(figsize=(12, 6))
    colors = sns.light_palette("seagreen", len(traits))

    sns.barplot(
        data=df, x="Trait", y="Percentage", palette=colors, hue="Trait", legend=False
    )

    for x, bar in zip(scores, plt.gca().patches):
        plt.gca().annotate(
            f"{x:.2f}%",
            (bar.get_x() + bar.get_width() / 2, bar.get_height()),
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
        )

    plt.xlabel("Traits")
    plt.ylabel("Percentage")
    plt.title("Extraversion Facets")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("plots/big_five_extraversion_facets_plot_bar.png", bbox_inches="tight")
    plt.close()

    return (
        "<center><img src='plots/big_five_extraversion_facets_plot_bar.png'/></center>"
    )


def plot_big_five_agreeableness_facets_bar(
    score_agreeableness_facets: list,
) -> str:
    sns.set(style="whitegrid", rc={"grid.linewidth": 0.5})
    traits = [list(item.values())[1] for item in score_agreeableness_facets]
    scores = [list(item.values())[2] for item in score_agreeableness_facets]

    df = pd.DataFrame({"Trait": traits, "Percentage": scores})

    plt.figure(figsize=(12, 6))
    colors = sns.color_palette("light:y", len(traits))

    sns.barplot(
        data=df, x="Trait", y="Percentage", palette=colors, hue="Trait", legend=False
    )

    for x, bar in zip(scores, plt.gca().patches):
        plt.gca().annotate(
            f"{x:.2f}%",
            (bar.get_x() + bar.get_width() / 2, bar.get_height()),
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
        )

    plt.xlabel("Traits")
    plt.ylabel("Percentage")
    plt.title("Agreeableness Facets")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("plots/big_five_agreeableness_facets_plot_bar.png", bbox_inches="tight")
    plt.close()

    return (
        "<center><img src='plots/big_five_agreeableness_facets_plot_bar.png'/></center>"
    )


def plot_big_five_neuroticism_facets_bar(
    score_neuroticism_facets: list,
) -> str:
    sns.set(style="whitegrid", rc={"grid.linewidth": 0.5})
    traits = [list(item.values())[1] for item in score_neuroticism_facets]
    scores = [list(item.values())[2] for item in score_neuroticism_facets]

    df = pd.DataFrame({"Trait": traits, "Percentage": scores})

    plt.figure(figsize=(12, 6))
    colors = sns.color_palette("Oranges", len(traits))

    sns.barplot(
        data=df, x="Trait", y="Percentage", palette=colors, hue="Trait", legend=False
    )

    for x, bar in zip(scores, plt.gca().patches):
        plt.gca().annotate(
            f"{x:.2f}%",
            (bar.get_x() + bar.get_width() / 2, bar.get_height()),
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
        )

    plt.xlabel("Traits")
    plt.ylabel("Percentage")
    plt.title("Neuroticism Facets")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("plots/big_five_neuroticism_facets_plot_bar.png", bbox_inches="tight")
    plt.close()

    return (
        "<center><img src='plots/big_five_neuroticism_facets_plot_bar.png'/></center>"
    )


def plot_orvis_facets_bar(
    score_orvis_facets: list,
) -> str:
    sns.set(style="whitegrid", rc={"grid.linewidth": 0.5})
    traits = [list(item.values())[1] for item in score_orvis_facets]
    scores = [list(item.values())[2] for item in score_orvis_facets]

    df = pd.DataFrame({"Trait": traits, "Percentage": scores})

    plt.figure(figsize=(12, 6))
    colors = sns.color_palette("Set2", len(traits))

    sns.barplot(
        data=df, x="Trait", y="Percentage", palette=colors, hue="Trait", legend=False
    )

    for x, bar in zip(scores, plt.gca().patches):
        plt.gca().annotate(
            f"{x:.2f}%",
            (bar.get_x() + bar.get_width() / 2, bar.get_height()),
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
        )

    plt.xlabel("Traits")
    plt.ylabel("Percentage")
    plt.title("ORVIS")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("plots/big_five_orvis_facets_plot_bar.png", bbox_inches="tight")
    plt.close()

    return "<center><img src='plots/big_five_orvis_facets_plot_bar.png'/></center>"
