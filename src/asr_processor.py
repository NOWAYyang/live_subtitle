import torch
from transformers import pipeline
import numpy as np

class WhisperASR:
    def __init__(self, model_name='openai/whisper-large-v3', device=None):
        if device is None:
            device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.device = device
        self.pipe = pipeline('automatic-speech-recognition', model=model_name, device=0 if device=='cuda' else -1)

    def transcribe(self, audio_np, sample_rate=16000):
        # audio_np: 1D numpy array, float32, -1~1, sample_rate Hz
        # transformers pipeline 支持 numpy array 输入
        result = self.pipe(audio_np, sampling_rate=sample_rate)
        return result['text']

# 示例用法：
# asr = WhisperASR()
# text = asr.transcribe(audio_np)
# print(text)
