#!/usr/bin/env python3

import os
import warnings
from pathlib import Path

import click
import gigaam
import ffmpeg
import validators
import yt_dlp

warnings.simplefilter("ignore")

DEFUALT_MODEL_NAME = 'v3_e2e_rnnt'


def validate_url(ctx, param, value):
    if not validators.url(value):
        raise click.BadParameter(f"{value}")
    return value


@click.group()
def cli():
    pass


@cli.command()
@click.argument("url", callback=validate_url, type=str)
def download(url: str) -> str:
    with yt_dlp.YoutubeDL({'outtmpl': 'downloaded_video.%(ext)s', 'quiet': True}) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info_dict)


@cli.command()
@click.argument("video_file_path", type=str)
def extract_audio(video_file_path: str) -> str:
    video_file_path = Path(video_file_path)
    if not video_file_path.exists():
        raise FileNotFoundError(f"Can't find file {video_file_path}")

    audio_file_path = video_file_path.with_suffix(".wav")

    ffmpeg\
        .input(video_file_path)\
        .output(filename=audio_file_path, format='wav', acodec='pcm_s16le', ar='44100', ac=2)\
        .global_args('-loglevel', 'quiet')\
        .run()

    if not audio_file_path.exists():
        raise FileNotFoundError(f"Can't find file {audio_file_path}")

    return str(audio_file_path)


@cli.command()
@click.argument("audio_file_path", type=str)
def ru_transcribe(audio_file_path: str):
    audio_file_path = Path(audio_file_path)
    if not audio_file_path.exists():
        raise FileNotFoundError(f"Can't find file {audio_file_path}")

    model_name = os.environ.get("SLT_STT_MODEL", None)
    if model_name is None:
        print(f'Warning: SLT_STT_MODEL value isn\'t set, {DEFUALT_MODEL_NAME} model are using by default.')
        model_name = DEFUALT_MODEL_NAME

    model = gigaam.load_model(model_name, fp16_encoder=True, use_flash=False,
                              device=None)  # TODO: switch to onnx inference
    recognition_result = model.transcribe_longform(str(audio_file_path))
    for utterance in recognition_result:
        transcription = utterance["transcription"]
        start, end = utterance["boundaries"]
        print(f"[{gigaam.format_time(start)} - {gigaam.format_time(end)}]: {transcription}")


# https://click.palletsprojects.com/en/stable/advanced/#invoking-other-commands
@cli.command()
@click.argument("url", callback=validate_url, type=str)
@click.pass_context
def ru_video_transcribe(ctx, url: str):
    ctx.invoke(ru_transcribe,
               audio_file_path=ctx.invoke(extract_audio,
                                          video_file_path=ctx.forward(download)))


if __name__ == "__main__":
    cli()
