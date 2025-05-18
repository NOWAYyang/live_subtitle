import sys
import threading
import numpy as np
from src.audio_capture import SystemAudioCapture
from src.asr_processor import WhisperASR
from src.translator import SubtitleTranslator
from src.gui import SubtitleGUI
from PyQt5 import QtWidgets
from PyQt5 import QtCore

class LiveSubtitleApp:
    def __init__(self):
        self.gui = SubtitleGUI()
        self.asr = WhisperASR()
        self.translator = SubtitleTranslator()
        self.audio_buffer = []
        self.buffer_lock = threading.Lock()
        self.samplerate = 16000
        self.blocksize = 1024
        self.capture = SystemAudioCapture(samplerate=self.samplerate, blocksize=self.blocksize)
        self.running = True

    def audio_callback(self, indata, frames, time, status):
        # indata: (blocksize, channels)
        mono = indata.mean(axis=1) if indata.shape[1] > 1 else indata[:,0]
        with self.buffer_lock:
            self.audio_buffer.append(mono.copy())

    def process_audio(self):
        # 每2秒处理一次音频
        chunk_samples = self.samplerate * 2
        while self.running:
            QtCore.QThread.msleep(500)
            with self.buffer_lock:
                if len(self.audio_buffer) * self.blocksize >= chunk_samples:
                    audio_np = np.concatenate(self.audio_buffer)[:chunk_samples]
                    self.audio_buffer = []
                else:
                    continue
            try:
                text = self.asr.transcribe(audio_np, sample_rate=self.samplerate)
                zh_text = self.translator.translate(text)
                self.gui.update_subtitle(f"{text}\n{zh_text}")
            except Exception as e:
                self.gui.update_subtitle(f"[错误] {e}")

    def run(self):
        self.capture.start_stream(self.audio_callback)
        threading.Thread(target=self.process_audio, daemon=True).start()
        self.gui.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    live_app = LiveSubtitleApp()
    live_app.run()
    sys.exit(app.exec_())
