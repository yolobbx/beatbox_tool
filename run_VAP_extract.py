import os
import subprocess


# Set the path of input and output files.
INPUT_VIDEO = r'"input/LFO - POWER _ Haten World Championship 2024 Loopstation Category Wildcard _ #HWC2024.mp4"'
OUTPUT_FILE = "output/LFO - POWER.mp3"


# Set the command for processing the input video/audio.
cmd = "ffmpeg -i " + INPUT_VIDEO + " -ab 320k -ac 2 -ar 48000 -vn " + OUTPUT_FILE

# -ac 2 将音频转为 立体声 -ac 1 将音频转为 单声道
# 44100 Hz ( 44.1 kHz ) , 这是 CD 音质的标准采样率 ;
# 48000 Hz ( 48 kHz ) , 这是 专业音频和视频制作 采样率 ;
#    -ab bitrate 设置音频码率
#    -ar freq 设置音频采样率
#    -ac channels 设置通道 缺省为1，即单通道

# Execute the (Terminal) command within Python.
subprocess.call(cmd, shell=True)


import os
import subprocess

# Set the path of input and output folders.
INPUT_FOLDER = r'input'
OUTPUT_FOLDER = 'output'

# Ensure the output folder exists.
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Get a list of all files in the input folder.
for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith('.mp4'):  # Change this to match your file type.
        input_file_path = os.path.join(INPUT_FOLDER, filename)
        output_file_path = os.path.join(OUTPUT_FOLDER, os.path.splitext(filename)[0] + '.mp3')

        # Set the command for processing the input video/audio.
        cmd = f'ffmpeg -i "{input_file_path}" -ab 320k -ac 2 -ar 48000 -vn "{output_file_path}"'

        # Execute the (Terminal) command within Python.
        subprocess.call(cmd, shell=True)