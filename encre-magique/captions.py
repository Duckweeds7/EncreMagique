import jieba


def split_sentences(text):
    sentences = text.split('。')  # 假设句子以句号作为分隔符
    sentences_with_comma = []
    for sentence in sentences:
        sub_sentences = sentence.split('，')  # 以逗号作为分隔符再次切割句子
        sub_sub_sentences = []
        sub_tmp = ""
        for ss in sub_sentences:
            if len(ss) + len(sub_tmp) >= 10 and len(sub_tmp) != 0:
                sub_sub_sentences.append(sub_tmp)
                sub_tmp = ss
            elif len(sub_tmp) == 0:
                sub_tmp = ss
            elif len(sub_tmp) != 0:
                sub_tmp = sub_tmp + "," + ss
        sub_sub_sentences.append(sub_tmp)
        sub_sub_sentences = [sub_sub_sentence.strip() for sub_sub_sentence in sub_sub_sentences if
                             sub_sub_sentence.strip()]  # 去除空句子

        sentences_with_comma.extend(sub_sub_sentences)
    sentences = [sentence.strip() for sentence in sentences_with_comma if sentence.strip()]  # 去除空句子
    return sentences


def convert_to_srt(sentences, max_length=20):
    srt = ''
    start_time = 0
    for i, sentence in enumerate(sentences):
        words = jieba.lcut(sentence)  # 使用jieba分词将句子分割为单词
        segments = []
        current_segment = ''
        for word in words:
            if len(current_segment) + len(word) <= max_length:
                current_segment += word
            else:
                segments.append(current_segment)
                current_segment = word

        segments.append(current_segment)
        segments.reverse()
        duration = max(3, len(segments) // 3)  # 根据分段数量计算每句字幕的持续时间（最小为3秒）
        end_time = start_time + duration  # 每句字幕的结束时间

        for j, segment in enumerate(segments):
            srt += f'{i * len(segments) + j + 1}\n00:00:{start_time:02d},000 --> 00:00:{end_time:02d},000\n{segment}\n\n'

        start_time = end_time

    return srt, end_time


def create_srt_file(text, output_file):
    sentences = split_sentences(text)
    srt_content, end_time = convert_to_srt(sentences)
    with open(output_file, 'w', encoding="utf-8") as f:
        f.write(srt_content)
    return end_time