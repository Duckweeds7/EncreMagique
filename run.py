from encremagique.media import generator_videos
from encremagique.subtitle import create_srt_file

if __name__ == '__main__':
    t = open('static/test_text', 'r', encoding='utf-8').read()
    all_time = create_srt_file(t, "subtitles.srt")
    folder_path = "static/images"
    cover_image = generator_videos(folder_path, all_time)
    files = os.listdir(folder_path)  # 获取文件夹中的文件列表
    video_files = []

    for file in files:
        file_path = os.path.join(folder_path, file)
        if ".mp4" in file and os.path.getsize(file_path) > 0:
            video_files.append(file_path)
    merge_file = 'temp.mp4'
    merge_videos(video_files, merge_file)
    video_with_subtitles_video = "video_with_subtitles_video.mp4"
    add_subtitles(merge_file, subtitles_file, video_with_subtitles_video)
    os.rename(cover_image, cover_image + ".mp4")
    merge_videos([cover_image + ".mp4", "open.mp4", video_with_subtitles_video, "end.mp4"], "temp_temp.mp4")
    final_path = os.path.join(fr"F:\PycharmProjects\zimeiti_editor\article\pub_path",
                              f"{p.t_title}.mp4").replace('"', '').replace("'", '')
    merge_video_audio("temp_temp.mp4", "audio2.mp3", final_path)
