# Simple Local Transcriber

Simple local transcribe (slt) is a CLI tool to transcribe videos from youtube to Russian language.

## Prerequisites

Tool requires `python3.11`, you can install it using [pyenv](https://github.com/pyenv/pyenv) for example.

The tool requires additional models from huggingface: [https://huggingface.co/pyannote/segmentation-3.0](https://huggingface.co/pyannote/segmentation-3.0) . So you should get access to these models, create huggingface token and export it as environment variable:

```
export HF_TOKEN=<hf-token-here>
```
## Background

Download [pyannote/segmentation-3.0 model](https://huggingface.co/pyannote/segmentation-3.0/resolve/main/pytorch_model.bin) by hands and put it to `$HOME/.cache/huggingface/hub/models--pyannote--segmentation-3.0/snapshots/e66f3d3b9eb0873085418a7b813d3b369bf160bb/`

## Installation

To install tool:

1. Clone repository from github: `git clone git@github.com:qaohv/simple-local-transcriber.git`
2. Install it with pip: `cd simple-local-transcriber && pip install -e .`


## Usage

slt provides four commands:

```
Usage: slt [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  download
  extract-audio
  ru-transcribe
  ru-video-transcribe
```

Details about each of them you can find below.

<details>
    <summary>slt ru-video-transcribe "url-to-video" </summary>
    
    Command to transcribe youtube video, it contains following steps:
    
    1. Downloading video from youtube and save to disk.
    2. Extract audio from saved video.
    3. Transcribe saved audio and print it to standard output.

    Example:
    ```
    slt ru-video-transcribe https://www.youtube.com/watch?v=xuYMkaNo_gI
    ```

    As result, transcription in following format will be printed in console:

    [timestamp_start1 - timestamp_finish1]: some text 1
    [timestamp_start2 - timestamp_finish2]: some text 2
</details>

<details>
    <summary>slt download "url-to-video" </summary>
    
    Command to download video from youtube and save it on a disk. 

    Example:
    ```
    slt download https://www.youtube.com/watch?v=xuYMkaNo_gI
    ```

    As result video with name `downloaded_video.webm` will be saved on a disk.
</details>

<details>
    <summary>slt extract-audio "path-to-video" </summary>
    
    Command to extract audio from youtube video and save it on a disk. 

    Example:
    ```
    slt extract-audio downloaded_video.webm
    ```

    As result audio with name `downloaded_video.wav` will be saved on a disk.
</details>

<details>
    <summary>slt ru-transcribe "path-to-audio" </summary>
    
    Command to transcribe audio and print text to standard output. 

    Example:
    ```
    slt ru-transcribe downloaded_video.wav
    ```

    As result, transcription in following format will be printed in console:

    [timestamp_start1 - timestamp_finish1]: some text 1
    [timestamp_start2 - timestamp_finish2]: some text 2
</details>

As you may have noticed the first command is a sequential call to the next three.
The tool provides audio extraction and transcribing functionality in case the user already has a video/audio file on the system.

**Usefull tip:**
 
 You can save transcribtion of audio to text file with printint to stdout using `tee` command, for example:

 ```
 slt <audio-file> | tee <text-file>
 ```

## Technical details

For speech-to-text [GigaAM-E2E-RNNT](https://github.com/salute-developers/GigaAM) model are used.
You can change model via env variable SLT_STT_MODEL, possible options: `v3_e2e_rnnt`, `v3_e2e_ctc`, `v3_rnnt`, `v3_ctc`.
Also, as mentioned above, [https://huggingface.co/pyannote/segmentation-3.0](https://huggingface.co/pyannote/segmentation-3.0) model is used for long audio recognition.

All models are running locally, so, if you trust hf/salute-developers models you may transcribe sensitive information.