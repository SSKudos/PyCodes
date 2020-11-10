#converts video to audio
import moviepy.editor

video = moviepy.editor.VideoFileClip(r'C:\Users\CHIJINDU\Desktop\Awilo.mp4')

audio = video.audio
audio.write_audiofile(r'C:\Users\CHIJINDU\Desktop\Awilo2.mp3')
