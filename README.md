# live_subtitle 技术文档

## 1. 项目简介

live_subtitle 是一个基于 PyQt5 的实时语音识别与翻译字幕显示工具。它能够捕获系统音频，实时进行语音识别（ASR），将识别结果翻译为中文，并以字幕形式在桌面窗口中显示。适用于会议、直播、视频观看等场景。

---

## 2. 项目结构

```
live_subtitle/
├── README.md
├── requirements.txt
├── setup_and_install.py
├── USAGE.md
├── resources/
└── src/
    ├── asr_processor.py      # 语音识别模块
    ├── audio_capture.py      # 音频采集模块
    ├── gui.py                # GUI 显示模块
    ├── main.py               # 主控逻辑
    └── translator.py         # 翻译模块
```

---

## 3. 主要模块说明

### 3.1 main.py（主控逻辑）

- **LiveSubtitleApp 类**：应用主类，负责各模块初始化、音频缓冲、线程管理和主流程控制。
- **audio_callback**：音频流回调，将采集到的音频数据转为单通道并缓存在 `audio_buffer`。
- **process_audio**：后台线程，每 2 秒处理一次音频缓冲，调用 ASR 和翻译模块，更新字幕。
- **run**：启动音频采集、后台处理线程，并显示 GUI。

#### 主流程

1. 初始化 GUI、ASR、翻译、音频采集等模块。
2. 启动音频采集，注册回调函数。
3. 启动后台线程定时处理音频缓冲。
4. 每次处理时，将音频缓冲拼接为固定长度，送入 ASR 识别。
5. 识别结果送入翻译模块，得到目标语言文本。
6. GUI 实时更新字幕内容。

### 3.2 audio_capture.py（音频采集）

- **SystemAudioCapture 类**：负责系统音频的采集，支持采样率、块大小等参数设置。
- **start_stream(callback)**：启动音频流采集，并将数据通过回调传递给主控逻辑。

### 3.3 asr_processor.py（语音识别）

- **WhisperASR 类**：封装语音识别模型（如 OpenAI Whisper），提供 `transcribe(audio, sample_rate)` 方法，将音频数据转为文本。

### 3.4 translator.py（翻译）

- **SubtitleTranslator 类**：封装翻译 API 或本地模型，提供 `translate(text)` 方法，将识别文本翻译为目标语言。

### 3.5 gui.py（字幕显示）

- **SubtitleGUI 类**：基于 PyQt5 实现的字幕显示窗口，提供 `update_subtitle(text)` 方法实时更新字幕内容。
- 支持窗口置顶、透明背景、字体样式自定义等功能。

---

## 4. 关键技术点

- **多线程**：音频采集与处理、GUI 显示分离，保证界面流畅与实时性。
- **线程安全**：音频缓冲区通过 `threading.Lock` 保护，避免多线程读写冲突。
- **音频处理**：支持多通道音频自动转为单通道，保证兼容性。
- **异常处理**：ASR/翻译过程异常会被捕获并显示在字幕窗口，提升用户体验。
- **GUI 响应**：所有字幕更新通过 GUI 主线程安全调用，避免界面卡死。

---

## 5. 依赖说明

- **Python 3.7+**
- **PyQt5**：桌面 GUI 框架
- **numpy**：音频数据处理
- **sounddevice / pyaudio**：音频采集（具体依赖见 audio_capture.py）
- **ASR/翻译相关依赖**：如 openai-whisper、transformers、requests 等（具体见 requirements.txt）

---

## 6. 运行方式

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 启动程序：
   ```bash
   python src/main.py
   ```

---

## 7. 常见问题与排查

- **无字幕显示**：检查音频采集设备、依赖安装、ASR/翻译 API 配置。
- **界面卡死**：确认未在主线程执行耗时操作。
- **识别/翻译慢**：可更换更快的模型或优化 chunk 处理逻辑。

---

如需详细 API 或模块内部实现说明，可进一步查阅各模块源码或补充文档。
