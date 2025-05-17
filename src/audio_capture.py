import sounddevice as sd
import numpy as np

class SystemAudioCapture:
    def __init__(self, samplerate=16000, channels=1, blocksize=1024):
        self.samplerate = samplerate
        self.channels = channels
        self.blocksize = blocksize
        self.stream = None
        self.device = self._find_monitor_device()

    def _find_monitor_device(self):
        devices = sd.query_devices()
        for idx, dev in enumerate(devices):
            if 'monitor' in dev['name'].lower() and dev['max_input_channels'] > 0:
                return idx
        raise RuntimeError('未找到系统回放（monitor）音频设备，请确保已启用pulseaudio并有monitor设备。')

    def start_stream(self, callback):
        if self.device is None:
            raise RuntimeError('未找到系统回放设备')
        self.stream = sd.InputStream(
            device=self.device,
            channels=self.channels,
            samplerate=self.samplerate,
            blocksize=self.blocksize,
            dtype='float32',
            callback=callback
        )
        self.stream.start()

    def stop_stream(self):
        if self.stream:
            self.stream.stop()
            self.stream.close()
            self.stream = None

# 示例用法：
# def audio_callback(indata, frames, time, status):
#     # indata为numpy数组，shape=(blocksize, channels)
#     print(indata.shape)
# 
# cap = SystemAudioCapture()
# cap.start_stream(audio_callback)
# ...
# cap.stop_stream()
