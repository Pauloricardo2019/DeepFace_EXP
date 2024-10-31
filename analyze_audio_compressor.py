from moviepy.editor import VideoFileClip, AudioFileClip
from pydub import AudioSegment

# Caminhos dos arquivos
processed_video_path = 'processed_video.mp4'  # Caminho para o vídeo processado
audio_path = './input/teste1.mp4'  # Caminho para o arquivo de áudio original
final_output_path = './output/final_video.mp4'  # Caminho para o vídeo final

# 1. Carregar o áudio original
audio = AudioSegment.from_file(audio_path)

# 2. Exportar áudio para um novo arquivo (MP3 como exemplo)
new_audio_path = './output/new_audio.mp3'
audio.export(new_audio_path, format='mp3')

# 3. Criar objetos Video e Audio
video_clip = VideoFileClip(processed_video_path)
audio_clip = AudioFileClip(new_audio_path)  # Carregar o áudio exportado

# 4. Definir o áudio do vídeo
final_video = video_clip.set_audio(audio_clip)

# 5. Salvar o vídeo final
final_video.write_videofile(final_output_path, codec='libx264', audio_codec='aac')

# 6. Fechar os clipes
video_clip.close()
audio_clip.close()
