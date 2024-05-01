import json

import requests


def login(user: str, password: str) -> dict:
    resp = requests.post(
        "https://api-spectrum.neuroquest.ai/api/v1/auth/login",
        headers={"Content-Type": "application/json"},
        json={"email": user, "password": password},
    )
    if resp.status_code == 200:
        return resp.json()
    print(f"Erro: {resp.status_code} - {resp.text}")
    return {}


def audio_to_text(
    token: str, audio_file: str, audio_lang: str, save_result: bool = False
) -> dict:
    resp = requests.post(
        "https://api-spectrum.neuroquest.ai/api/v1/audio/to-text",
        headers={"token": token},
        files={"audio_file": open(audio_file, "rb")},
        data={"audio_lang": audio_lang},
    )

    if resp.status_code == 201:
        data = resp.json() or {}
        if save_result:
            with open("audio-transcription-result.json", "w") as f:
                json.dump(data, f)
        return data
    print(f"Erro: {resp.status_code} -> {resp.text}")
    return {}


def get_audio_to_text_in_file() -> dict:
    with open("audio-transcription-result.json", "r") as f:
        data = json.load(f) or {}
    return data


def audio_ser(token: str, audio_document_id: str, save_result: bool = False) -> dict:
    resp = requests.put(
        f"https://api-spectrum.neuroquest.ai/api/v1/audio/speech-emotion-recognition/by-transcript?document_id={audio_document_id}",
        headers={"Content-Type": "application/json", "token": token},
    )

    if resp.status_code == 201:
        data = resp.json() or {}
        if save_result:
            with open("audio-ser-result.json", "w") as f:
                json.dump(data, f)
        return data
    print(f"Erro: {resp.status_code} -> {resp.text}")
    return {}


def get_audio_ser_in_file() -> dict:
    with open("audio-ser-result.json", "r") as f:
        data = json.load(f) or {}
    return data
