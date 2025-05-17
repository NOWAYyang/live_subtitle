# Live Subtitle 使用说明

## 环境准备
1. 建议使用 Python 3.8 及以上版本。
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 确保 Ubuntu 系统已启用 pulseaudio，并存在“monitor”设备（可用 pavucontrol 工具查看）。
4. 推荐 NVIDIA 显卡和 CUDA 驱动（可选，但大幅提升识别速度）。

## 启动程序
在 live_subtitle 目录下运行：
```bash
python3 -m src.main
```

## 功能说明
- 程序自动采集系统回放（你听到的所有声音），无需手动选择设备。
- 实时识别系统声音为字幕，并自动翻译（默认英译中）。
- 字幕以大字显示在窗口中央。

## 常见问题
- 启动报“未找到系统回放（monitor）音频设备”：请检查 pulseaudio 是否启用，或用 pavucontrol 启用“monitor”设备。
- 识别慢：建议使用 NVIDIA 显卡并正确安装 CUDA 驱动。
- 翻译不准确：可在 src/translator.py 中更换 transformers 支持的其他翻译模型。

## 进阶用法
- 可根据需求修改 src/main.py，调整识别/翻译语言、字幕刷新频率等。
- 支持多语言识别与翻译，详见 transformers 文档。

## 退出方法
- 关闭字幕窗口即可退出程序。

## 联系与反馈
如有问题或建议，欢迎提交 issue。
