# Simple Local Transcriber (slt)

It's simple CLI tool to transcribe videos from youtube to russian language.

## Prerequisites

Tool requires `python3.11`, you can install it using [pyenv](https://github.com/pyenv/pyenv) for example.

Util requires extra models from huggingface: https://huggingface.co/pyannote/voice-activity-detection and https://huggingface.co/pyannote/segmentation . So you should get access to these models, create huggingface token and export it as environment variable:

```
export HF_TOKEN=<hf-token-here>
```

## Installation

To install tool:

1. Clone repository from github: `git clone git@github.com:qaohv/simple-local-transcriber.git`
2. Install it pip: `cd simple-local-transcriber && pip install -e .`


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
    
    Command to get trainscribtion from youtube video, it contains following steps:
    
    1. Downloading video from youtube and save to disk.
    2. Extract audio from saved video.
    3. Transcribe saved audio and print it to sandard output.

    Example:
    ```
    slt ru-video-transcribe https://www.youtube.com/watch?v=xuYMkaNo_gI
    ```

    As result transcribtion in following format will be printed in console:

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
    <summary>slt extract-audio "path-to-audio" </summary>
    
    Command to transcribe audio and print text to standart output. 

    Example:
    ```
    slt ru-transcribe downloaded_video.wav
    ```

    As result transcribtion in following format will be printed in console:

    [timestamp_start1 - timestamp_finish1]: some text 1
    [timestamp_start2 - timestamp_finish2]: some text 2
</details>