import subprocess

INPUT_MEDIA = r'../data/audio/LFO - POWER.mp3'
OUTPUT_PATH = r'../data/trimmed_audio/LFO - POWER.mp3'

START = '00:00:25' + '.000'
END = '00:03:12' + '.000'

# 当末尾时间默认时，可不带 END 参数，默认裁剪至末尾

# cmd = f'ffmpeg -i "{INPUT_MEDIA}" -ab 320k -ac 2 -ar 48000 -ss  "{START}" -to "{END}"  "{OUTPUT_PATH}"'
cmd = f'ffmpeg -i "{INPUT_MEDIA}" -ab 320k -ac 2 -ar 48000 -ss "{START}"  "{OUTPUT_PATH}"'

subprocess.call(cmd, shell=True)

# $ ffmpeg -i in.mpn -ss [start] -to [end] out.mpn
# Note:
#    '[start]' - The start point of original media 'in.mpn'.
#    '[start]' - The format is 'hh:mm:ss.xxx' or 'nnn', '00:01:15.000' or '75'.
#    '[end]'   - The end point of original media 'in.mpn'.
#    '[end]'   - The format is 'hh:mm:ss.xxx' or 'nnn', '00:01:25.000' or '85'.
# Note:
#     Setting '-i in.mpn' before '-ss [start]' avoids inaccurate clips.
#     Removing 'copy' re-encodes clips and avoids black screen/frames.
#     Removing 'copy' leads to high CPU load and long operating time.