import json
import base64

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px


def api_login(user: str, password: str) -> dict:
    resp = requests.post(
        "https://api-persona-predict.neuroquest.ai/api/v2/auth/login",
        headers={"Content-Type": "application/json"},
        json={"email": user, "password": password},
    )
    if resp.status_code == 200:
        return resp.json()
    print(f"Erro: {resp.status_code} - {resp.text}")
    return {}


def api_predict_create(token: str, data: dict, save_result: bool = False) -> dict:
    resp = requests.post(
        "https://api-persona-predict.neuroquest.ai/api/v2/predict/create",
        headers={"Content-Type": "application/json", "token": token},
        json=data,
    )
    if resp.status_code == 201:
        data = resp.json()
        if save_result:
            with open("results/persona-predict-v2.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)
        return data
    print(f"Erro: {resp.status_code} -> {resp.text}")
    return {}


def api_save_result_domain(data: dict, domain: str, level: str) -> None:
    with open(
        f"results/persona-predict-v2-{domain}-{level}.json", "w", encoding="utf-8"
    ) as f:
        json.dump(data, f, ensure_ascii=False)


def get_api_predict_result_in_file() -> dict:
    with open("results/persona-predict-v2.json", "r") as f:
        data = json.load(f)
    return data


def get_my_txt_essay(lang: str = "en") -> str:
    if lang == "en":
        return " ".join(str(open("essays/my-essay-en.txt", "r").read()).split())
    elif lang == "pt":
        return " ".join(str(open("essays/my-essay-pt.txt", "r").read()).split())
    raise ValueError("Essay not found!")


def image_to_base64(image_path: str) -> base64.b64decode:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def plot_sunburst(data: dict, image_path: str = "imgs/person1.png") -> str:
    labels, parents = [], []
    values, text = [], []

    def add_sunburst_data(label: str, parent: str, value: float) -> None:
        value = round(float(value), 2)
        labels.append(label)
        parents.append(parent)
        values.append(value)
        text.append(f"{label} ({value}%)")

    add_sunburst_data("Big Five", "", 100)

    for personality in data["data"]["person"]["analysis"]["personalities"]:
        for dimension, details in personality.items():
            add_sunburst_data(dimension.capitalize(), "Big Five", details["result"])
            for trait in details["traits"]:
                try:
                    facet_name, facet_value = trait["name"], trait["result"]
                    facet_label = f"{facet_name.replace('_', ' ').capitalize()}"
                    add_sunburst_data(facet_label, dimension.capitalize(), facet_value)
                except ValueError:
                    pass

    fig = go.Figure(
        go.Sunburst(
            labels=labels,
            parents=parents,
            values=values,
            text=text,
            textinfo="text",
            insidetextorientation="radial",
        )
    )

    fig.update_layout(
        margin=dict(t=0, l=0, r=0, b=0),
        width=1200,
        height=1200,
        uniformtext=dict(minsize=10, mode="hide"),
    )

    base64_image = image_to_base64(image_path)

    fig.update_layout(
        images=[
            dict(
                source=f"data:image/png;base64,{base64_image}",
                xref="paper",
                yref="paper",
                x=0.5,
                y=0.5,
                sizex=0.25,
                sizey=0.25,
                xanchor="center",
                yanchor="middle",
                layer="above",
            )
        ],
        margin=dict(t=0, l=0, r=0, b=0),
        uniformtext=dict(minsize=10, mode="hide"),
    )

    fig.write_image("plots/big_five_plot_sunburst.png", format="png")

    return "<center><img src='plots/big_five_plot_sunburst.png'/></center>"


def get_big5(x: dict) -> dict:
    if "openness" in x and x["openness"].get("result") is not None:
        return {"O": x["openness"]["result"]}
    elif "conscientiousness" in x and x["conscientiousness"].get("result") is not None:
        return {"C": x["conscientiousness"]["result"]}
    elif "extraversion" in x and x["extraversion"].get("result") is not None:
        return {"E": x["extraversion"]["result"]}
    elif "agreeableness" in x and x["agreeableness"].get("result") is not None:
        return {"A": x["agreeableness"]["result"]}
    elif "neuroticism" in x and x["neuroticism"].get("result") is not None:
        return {"N": x["neuroticism"]["result"]}


def plot_big5_bar(score_big_five: list) -> str:
    sns.set(style="whitegrid", rc={"grid.linewidth": 0.5})

    score_dict = {list(d.keys())[0]: list(d.values())[0] for d in score_big_five}
    df = pd.DataFrame.from_dict(
        score_dict, orient="index", columns=["Percentage"]
    ).reset_index()
    df.columns = ["Trait", "Percentage"]
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


def plot_big5_radar(score_big_five: list) -> str:
    keys = list(score_big_five[0].keys())
    percentile = list(score_big_five[0].values())

    keys.append(keys[0])
    percentile.append(percentile[0])

    _, ax = plt.subplots(figsize=(12, 6), subplot_kw={"polar": True})

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


def plot_big5_openness_facets_bar(score_openness_facets: list) -> str:
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


def plot_big5_conscientiousness_facets_bar(
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


def plot_big5_extraversion_facets_bar(
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


def plot_big5_agreeableness_facets_bar(
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


def plot_big5_neuroticism_facets_bar(
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

    plt.savefig("plots/orvis_facets_plot_bar.png", bbox_inches="tight")
    plt.close()

    return "<center><img src='plots/orvis_facets_plot_bar.png'/></center>"


def plot_eda_boxplot(
    df: pd.DataFrame, targets: list, ticktext: list, title: str, color: int
) -> None:
    fig = go.Figure()

    if color == 1:
        set_color = px.colors.sequential.Plasma
    elif color == 2:
        set_color = px.colors.sequential.Cividis
    elif color == 3:
        set_color = px.colors.sequential.Magma
    elif color == 4:
        set_color = px.colors.sequential.Inferno
    elif color == 5:
        set_color = px.colors.sequential.Turbo
    elif color == 6:
        set_color = px.colors.sequential.Jet
    elif color == 7:
        set_color = px.colors.sequential.Viridis
    elif color == 8:
        set_color = px.colors.sequential.Purp
    elif color == 9:
        set_color = px.colors.sequential.Teal

    for i, (dim, color) in enumerate(zip(targets, set_color)):
        fig.add_trace(
            go.Box(y=[df[x].tolist() for x in targets][i], name=dim, marker_color=color)
        )

    fig.update_layout(
        title=dict(text=title, x=0.5),
        yaxis=dict(title="Values"),
        xaxis=dict(
            tickvals=list(range(len(targets))),
            ticktext=ticktext,
            tickangle=45,
        ),
        height=600,
        width=1000,
        margin=dict(l=100, r=100, b=100, t=100),
    )

    fig.show()


def plot_eda_radar(df: pd.DataFrame, targets: list, title: str) -> None:
    fig = go.Figure()

    if len(targets) == 5:
        titles = targets + targets[:1]
    else:
        titles = [
            facet.split("_", 1)[1].replace("_", " ").title() for facet in targets
        ] + [targets[0].split("_", 1)[1].replace("_", " ").title()]

    for stat, line_style in [("Mean", None), ("Max", "dash"), ("Min", "dash")]:
        values = (
            df[targets].agg(stat.lower()).tolist()
            + df[targets].agg(stat.lower()).tolist()[:1]
        )
        fig.add_trace(
            go.Scatterpolar(
                r=values,
                theta=titles,
                fill="toself",
                name=stat,
                line=dict(dash=line_style),
            )
        )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100]),
            angularaxis=dict(rotation=90, direction="clockwise"),
        ),
        showlegend=True,
        title=dict(text=title, x=0.5),
        height=600,
        width=1000,
        margin=dict(l=100, r=100, b=100, t=100),
    )

    fig.show()


def remove_stop_words_from_essay(
    df: pd.DataFrame, download_data: bool = False
) -> str | None:
    import logging

    logger = logging.getLogger("nltk")
    logger.setLevel(logging.ERROR)

    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    import nltk

    if download_data:
        nltk.download("stopwords")
        nltk.download("punkt")

    essays = " ".join(df["essay"].astype(str).tolist())
    words = word_tokenize(essays)

    stopwords = set(stopwords.words("portuguese"))
    clean_stopwords = " ".join([x for x in words if x.lower() not in stopwords])

    return clean_stopwords or None
