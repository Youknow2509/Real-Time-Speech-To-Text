# Contact:
- **Mail**: *lytranvinh.work@gmail.com*
- **Github**: *https://github.com/Youknow2509*

# Doc
- Project is Real Time Speed to text use **whisper**.
- Use: 
    - [Whisper](https://github.com/openai/whisper)
    - [Speech Recognition](https://github.com/Uberi/speech_recognition)
  
# How to use it:
- Download environment:
  
    ``` shell
      pip install -r requirements.txt
    ```

- Display devices information use input speech:

    ``` shell
        python utils/displayDevices.py
    ```

- Speech to text computer's audio:
  **[Note]**: Use `DEVICE_INDEX` input speech device index

    ``` shell
        python main.py
    ```

# How to run in MacOS:
- Use [`Black Hole`](https://github.com/ExistentialAudio/BlackHole) create driver:
    - How to install: 
        ``` shell
            # install home brew
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            # install black hole plugin
            brew install blackhole-2ch
        ```

- Read [*doc*](https://github.com/ExistentialAudio/BlackHole) it and create mutil output device.

- Find **index** of plugin and change to file main and run it.
  
