import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import seaborn as sns
from IPython.display import HTML, Markdown, display


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


def get_my_txt_essay() -> str:
    return " ".join(str(open("my-essay.txt", "r").read()).split())


def get_big_five(x: dict) -> dict:
    return {
        "O": x.get("openness").get("O"),
        "C": x.get("conscientiousness").get("C"),
        "E": x.get("extraversion").get("E"),
        "A": x.get("agreeableness").get("A"),
        "N": x.get("neuroticism").get("N"),
    }


def get_openness_facets(x: dict) -> dict:
    if "imagination" in x:
        return {"Imagination": x.get("imagination")}
    elif "artistic_interests" in x:
        return {"Artistic Interests": x.get("artistic_interests")}
    elif "emotionality" in x:
        return {"Emotionality": x.get("emotionality")}
    elif "adventurousness" in x:
        return {"Adventurousness": x.get("adventurousness")}
    elif "intellect" in x:
        return {"Intellect": x.get("intellect")}
    elif "liberalism" in x:
        return {"Liberalism": x.get("liberalism")}
    return {}


def get_conscientiousness_facets(x: dict) -> dict:
    if "self_efficacy" in x:
        return {"Self-Efficacy": x.get("self_efficacy")}
    elif "orderliness" in x:
        return {"Orderliness": x.get("orderliness")}
    elif "dutifulness" in x:
        return {"Dutifulness": x.get("dutifulness")}
    elif "achievement_striving" in x:
        return {"Achievement-Striving": x.get("achievement_striving")}
    elif "self_discipline" in x:
        return {"Self-Discipline": x.get("self_discipline")}
    elif "cautiousness" in x:
        return {"Cautiousness": x.get("cautiousness")}
    return {}


def get_conscientiousness_facets(x: dict) -> dict:
    if "self_efficacy" in x:
        return {"Self-Efficacy": x.get("self_efficacy")}
    elif "orderliness" in x:
        return {"Orderliness": x.get("orderliness")}
    elif "dutifulness" in x:
        return {"Dutifulness": x.get("dutifulness")}
    elif "achievement_striving" in x:
        return {"Achievement Striving": x.get("achievement_striving")}
    elif "self_discipline" in x:
        return {"Self-Discipline": x.get("self_discipline")}
    elif "cautiousness" in x:
        return {"Cautiousness": x.get("cautiousness")}
    return {}


def get_extraversion_facets(x: dict) -> dict:
    if "friendliness" in x:
        return {"Friendliness": x.get("friendliness")}
    elif "gregariousness" in x:
        return {"Gregariousness": x.get("gregariousness")}
    elif "assertiveness" in x:
        return {"Assertiveness": x.get("assertiveness")}
    elif "activity_level" in x:
        return {"Activity Level": x.get("activity_level")}
    elif "excitement_seeking" in x:
        return {"Excitement-Seeking": x.get("excitement_seeking")}
    elif "cheerfulness" in x:
        return {"Cheerfulness": x.get("cheerfulness")}
    return {}


def get_agreeableness_facets(x: dict) -> dict:
    if "trust" in x:
        return {"Trust": x.get("trust")}
    elif "morality" in x:
        return {"Morality": x.get("morality")}
    elif "altruism" in x:
        return {"Altruism": x.get("altruism")}
    elif "cooperation" in x:
        return {"Cooperation": x.get("cooperation")}
    elif "modesty" in x:
        return {"Modesty": x.get("modesty")}
    elif "sympathy" in x:
        return {"Sympathy": x.get("sympathy")}
    return {}


def get_neuroticism_facets(x: dict) -> dict:
    if "anxiety" in x:
        return {"Anxiety": x.get("anxiety")}
    elif "anger" in x:
        return {"Anger": x.get("anger")}
    elif "depression" in x:
        return {"Depression": x.get("depression")}
    elif "self_consciousness" in x:
        return {"Self-Consciousness": x.get("self_consciousness")}
    elif "immoderation" in x:
        return {"Immoderation": x.get("immoderation")}
    elif "vulnerability" in x:
        return {"Vulnerability": x.get("vulnerability")}
    return {}


def plot_big_five_bar(score_big_five: list) -> None:
    sns.set(style="whitegrid", rc={"grid.linewidth": 0.5})

    df = pd.DataFrame.from_dict(
        score_big_five[0], orient="index", columns=["Percentage"]
    ).reset_index()
    df = df.rename(columns={"index": "Trait"})

    plt.figure(figsize=(12, 6))
    sns.barplot(
        data=df, x="Trait", y="Percentage", palette="viridis", hue="Trait", legend=False
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

    display(Markdown("<center><img src='plots/big_five_plot_bar.png'/></center>"))


def plot_big_five_radar(score_big_five: list) -> None:
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

    display(HTML("<center><img src='plots/big_five_plot_radar.png' /></center>"))


def plot_big_five_openness_facets_bar(score_openness_facets: list) -> None:
    sns.set(style="whitegrid", rc={"grid.linewidth": 0.5})
    traits = [list(item.keys())[0] for item in score_openness_facets]
    scores = [list(item.values())[0] for item in score_openness_facets]

    df = pd.DataFrame({"Trait": traits, "Percentage": scores})

    plt.figure(figsize=(12, 6))
    colors = sns.color_palette("RdPu", len(traits))

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
    plt.show()


def plot_big_five_conscientiousness_facets_bar(
    score_conscientiousness_facets: list,
) -> None:
    sns.set(style="whitegrid", rc={"grid.linewidth": 0.5})
    traits = [list(item.keys())[0] for item in score_conscientiousness_facets]
    scores = [list(item.values())[0] for item in score_conscientiousness_facets]

    df = pd.DataFrame({"Trait": traits, "Percentage": scores})

    plt.figure(figsize=(12, 6))
    colors = sns.color_palette("YlOrBr", len(traits))

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
    plt.show()


def plot_big_five_extraversion_facets_bar(
    score_extraversion_facets: list,
) -> None:
    sns.set(style="whitegrid", rc={"grid.linewidth": 0.5})
    traits = [list(item.keys())[0] for item in score_extraversion_facets]
    scores = [list(item.values())[0] for item in score_extraversion_facets]

    df = pd.DataFrame({"Trait": traits, "Percentage": scores})

    plt.figure(figsize=(12, 6))
    colors = sns.color_palette("Greens", len(traits))

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
    plt.show()


def plot_big_five_agreeableness_facets_bar(
    score_agreeableness_facets: list,
) -> None:
    sns.set(style="whitegrid", rc={"grid.linewidth": 0.5})
    traits = [list(item.keys())[0] for item in score_agreeableness_facets]
    scores = [list(item.values())[0] for item in score_agreeableness_facets]

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
    plt.title("Agreeableness Facets")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_big_five_neuroticism_facets_bar(
    score_neuroticism_facets: list,
) -> None:
    sns.set(style="whitegrid", rc={"grid.linewidth": 0.5})
    traits = [list(item.keys())[0] for item in score_neuroticism_facets]
    scores = [list(item.values())[0] for item in score_neuroticism_facets]

    df = pd.DataFrame({"Trait": traits, "Percentage": scores})

    plt.figure(figsize=(12, 6))
    colors = sns.color_palette("Reds", len(traits))

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
    plt.show()
