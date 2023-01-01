import  moviepy.editor

video = moviepy.editor.VideoFileClip('16394856544720.mp4')
audio = video.audio
audio.write_audiofile('16394856544720.mp3')