import os
import subprocess
from typing import List

import ffmpeg


def create_zoom_out_video(input_image: str = 'input.jpg', output_video: str = 'output.mp4',
                          duration: int = 5, frame_rate: int = 30) -> str:
    """
    通过图片创建缩小效果的视频。

    Args:
        input_image: 输入图片文件的路径。默认为'input.jpg'。
        output_video: 输出视频文件的路径。默认为'output.mp4'。
        duration: 视频的时长，单位为秒。默认为5。
        frame_rate: 视频的帧率。默认为30。

    Returns:
        str: 生成的视频文件路径。

    Raises:
        ValueError: 如果输入文件不存在或输出文件路径无效。
        subprocess.CalledProcessError: 如果ffmpeg命令执行失败。
    """
    if not os.path.isfile(input_image):
        raise ValueError("输入图片文件不存在.")

    if not os.path.isabs(output_video):
        raise ValueError("输出视频文件路径无效.")

    # 设置ffmpeg的输入和输出
    input_stream = ffmpeg.input(input_image, loop=1)
    output_stream = ffmpeg.output(input_stream, output_video,
                                  vf=f'zoompan=z=\'if(lte(zoom,1.0),2.0,max(1.001,zoom-0.008))\':d={duration * 1000}:s=1920x1080,fps={frame_rate},setpts=N/(FRAME_RATE*TB)',
                                  vcodec='libx264', t=duration)

    # 运行ffmpeg命令
    ffmpeg.run(output_stream, overwrite_output=True)
    return output_video


def image_to_video(image_file: str, output_file: str, fps: int = 30, width: int = 1920, height: int = 1080) -> str:
    """
    将单张图片转换为视频，主要用于封面帧的制作。

    Args:
        image_file: 输入图片文件的路径。
        output_file: 输出视频文件的路径。
        fps: 视频的帧率。默认为30。
        width: 视频的宽度。默认为1920。
        height: 视频的高度。默认为1080。

    Returns:
        str: 生成的视频文件路径。

    Raises:
        ValueError: 如果输入文件不存在或输出文件路径无效。
        subprocess.CalledProcessError: 如果ffmpeg命令执行失败。
    """
    if not os.path.isfile(image_file):
        raise ValueError("输入图片文件不存在.")

    if not os.path.isabs(output_file):
        raise ValueError("输出视频文件路径无效.")

    # 设置ffmpeg的输入和输出
    input_stream = ffmpeg.input(image_file, loop=1)
    output_stream = ffmpeg.output(input_stream, output_file,
                                  vcodec='libx264', r=fps, t=1, s=f'{width}x{height}', pix_fmt='yuv420p')

    # 运行ffmpeg命令
    ffmpeg.run(output_stream, overwrite_output=True)
    return output_file


def add_subtitles(video_file: str, subtitles_file: str, output_file: str) -> str:
    """
    将字幕添加到视频中。

    Args:
        video_file: 输入视频文件的路径。
        subtitles_file: 字幕文件的路径。
        output_file: 输出视频文件的路径。

    Returns:
        str: 生成的视频文件路径。

    Raises:
        ValueError: 如果输入文件不存在或输出文件路径无效。
        subprocess.CalledProcessError: 如果ffmpeg命令执行失败。
    """
    if not os.path.isfile(video_file):
        raise ValueError("输入视频文件不存在.")

    if not os.path.isfile(subtitles_file):
        raise ValueError("字幕文件不存在.")

    if not os.path.isabs(output_file):
        raise ValueError("输出视频文件路径无效.")

    # 设置ffmpeg的输入和输出
    input_stream = ffmpeg.input(video_file)
    subtitles_stream = ffmpeg.input(subtitles_file)
    output_stream = ffmpeg.output(input_stream['v'], subtitles_stream['s'], output_file,
                                  vf='subtitles', acodec='copy', scodec='mov_text')

    # 运行ffmpeg命令
    ffmpeg.run(output_stream, overwrite_output=True)
    return output_file


def merge_videos(video_files: List[str], output_file: str, video_codec: str = 'copy', audio_codec: str = 'copy') -> str:
    """
    合并多个视频文件。

    Args:
        video_files: 包含视频文件路径的列表。
        output_file: 输出合并后的视频文件路径。
        video_codec: 视频编码器。默认为'copy'，即不进行视频重编码。
        audio_codec: 音频编码器。默认为'copy'，即不进行音频重编码。

    Returns:
        str: 生成的合并后的视频文件路径。

    Raises:
        ValueError: 如果视频文件列表为空或输出文件路径无效。
        subprocess.CalledProcessError: 如果ffmpeg命令执行失败。
    """
    if not video_files:
        raise ValueError("视频文件列表为空.")

    if not os.path.isabs(output_file):
        raise ValueError("输出视频文件路径无效.")

    # 设置ffmpeg的输入和输出
    inputs = [ffmpeg.input(file) for file in video_files]
    output_stream = ffmpeg.output(*inputs, output_file, vcodec=video_codec, acodec=audio_codec)

    # 运行ffmpeg命令
    ffmpeg.run(output_stream, overwrite_output=True)
    return output_file


def merge_video_audio(video_path: str, audio_path: str, output_path: str, loop_video: bool = False,
                      video_codec: str = 'copy', audio_codec: str = 'aac') -> str:
    """
    将视频和音频合并。

    Args:
        video_path: 视频文件的路径。
        audio_path: 音频文件的路径。
        output_path: 合并后输出文件的路径。
        loop_video: 是否循环视频。默认为False。
        video_codec: 视频编码格式。默认为'copy'。
        audio_codec: 音频编码格式。默认为'aac'。

    Returns:
        str: 合并后的视频文件路径。

    Raises:
        ValueError: 如果输入文件路径无效或输出文件路径无效。
        subprocess.CalledProcessError: 如果ffmpeg命令执行失败。
    """
    if not os.path.isfile(video_path):
        raise ValueError("视频文件路径无效.")

    if not os.path.isfile(audio_path):
        raise ValueError("音频文件路径无效.")

    if not os.path.isabs(output_path):
        raise ValueError("输出文件路径无效.")

    # 设置ffmpeg的输入和输出
    input_video = ffmpeg.input(video_path, stream_loop=-1 if loop_video else None)
    input_audio = ffmpeg.input(audio_path)
    output_stream = ffmpeg.output(input_video['v'], input_audio['a'], output_path,
                                  vcodec=video_codec, acodec=audio_codec, shortest=None)

    # 运行ffmpeg命令
    ffmpeg.run(output_stream, overwrite_output=True)
    return output_path


def sort_files_by_size(folder_path: str, extensions=None) -> List[str]:
    """
    根据文件大小对文件夹中的文件进行排序。

    Args:
        folder_path: 包含文件的文件夹路径。
        extensions: 要忽略的文件扩展名列表。默认为 [".mp4", ".gif", ".png"]。

    Returns:
        List[str]: 排序后的文件名列表。

    Raises:
        ValueError: 如果输入文件夹路径无效。
        FileNotFoundError: 如果无法访问输入文件夹或文件。
    """
    if extensions is None:
        extensions = [".mp4", ".gif", ".png"]
    if not os.path.isdir(folder_path):
        raise ValueError("输入文件夹路径无效.")

    files = os.listdir(folder_path)
    files_with_size = []

    for file in files:
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path) and os.path.splitext(file)[1].lower() not in extensions:
            file_size = os.path.getsize(file_path)
            files_with_size.append((file, file_size))

    sorted_files = sorted(files_with_size, key=lambda x: x[1], reverse=True)
    sorted_file_names = [file[0] for file in sorted_files]

    return sorted_file_names


def generator_videos(folder_path: str, all_time: int) -> str:
    """
    根据文件夹中的图片生成视频序列。

    Args:
        folder_path: 包含图片文件的文件夹路径。
        all_time: 总视频时长，单位为秒。

    Returns:
        str: 封面图像文件路径。

    Raises:
        ValueError: 如果输入文件夹路径无效。
        FileNotFoundError: 如果无法访问输入文件夹或文件。
    """
    sorted_files = sort_files_by_size(folder_path)
    cover_img = None

    for f in sorted_files:
        duration = min(5, all_time)
        all_time -= duration

        input_image = os.path.join(folder_path, f)

        if not cover_img:
            cover_img = os.path.join(folder_path, "cover.jpg")
            image_to_video(input_image, cover_img + ".mp4")
            try:
                os.rename(cover_img + ".mp4", cover_img)
            except Exception as e:
                os.remove(cover_img)
                os.rename(cover_img + ".mp4", cover_img)

        output_video = os.path.join(folder_path, f.split(".")[0] + ".mp4")
        create_zoom_out_video(input_image, output_video, duration)

        if all_time == 0:
            return cover_img

    return cover_img
