from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import os

# Get the folder path and file names
folder_path = "C:\\Users\\yashk\\OneDrive\\Pictures\\Movies&TV\\Movies\\Your Name"
video_file = "Your.name.mp4"
subtitle_file = "Your.name.srt"

# Load the video and subtitle files
video_path = os.path.join(folder_path, video_file)
subtitle_path = os.path.join(folder_path, subtitle_file)
video = VideoFileClip(video_path)
generator = lambda txt: TextClip(txt, font='Arial', fontsize=48, color='white')
subtitles = SubtitlesClip(subtitle_path, generator)


# Add the subtitles to the video
result = CompositeVideoClip([video, subtitles.set_pos(('center','bottom'))])

# Write the result to a new video file
result_path = os.path.join(folder_path, "Your.name_with_subtitles.mp4")
result.write_videofile(result_path, fps=video.fps)
