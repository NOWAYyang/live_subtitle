#!/usr/bin/env python3
import os
import subprocess
import sys

REQUIREMENTS = 'requirements.txt'

# 检查并安装pip
try:
    import pip
except ImportError:
    print('pip 未安装，正在尝试安装...')
    subprocess.run(['sudo', 'apt', 'update'])
    subprocess.run(['sudo', 'apt', 'install', '-y', 'python3-pip'])

# 检查并安装pulseaudio和pavucontrol
print('检查并安装 pulseaudio 和 pavucontrol...')
subprocess.run(['sudo', 'apt', 'update'])
subprocess.run(['sudo', 'apt', 'install', '-y', 'pulseaudio', 'pavucontrol'])

# 检查requirements.txt
if not os.path.exists(REQUIREMENTS):
    print(f'未找到 {REQUIREMENTS}，请确认路径。')
    sys.exit(1)

# 安装Python依赖
print('正在安装Python依赖...')
subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', REQUIREMENTS])

print('\n依赖安装完成！')
print('如需NVIDIA加速，请确保已正确安装CUDA驱动。')
print('如需配置monitor设备，可用pavucontrol手动启用。')
print('\n现在可以运行: python3 -m src.main')
