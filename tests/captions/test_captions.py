import unittest
from pathlib import Path
from typing import Callable

from encremagique.captions import SRTGenerator, ChineseProcessor, EnglishProcessor


class TestLanguageProcessors(unittest.TestCase):
    def test_chinese_processor(self):
        processor = ChineseProcessor()
        sentences = processor.split_sentences("这是一个句子。这是另一个句子！还有这个。")
        self.assertEqual(sentences, ["这是一个句子", "这是另一个句子", "还有这个"])
        tokens = processor.tokenize("这是一个测试句子")
        self.assertListEqual(tokens, ["这是", "一个", "测试", "句子"])

    def test_english_processor(self):
        processor = EnglishProcessor()
        sentences = processor.split_sentences("This is a sentence. This is another one! And what about this one.")
        self.assertEqual(sentences, ["This is a sentence", "This is another one", "And what about this one"])
        tokens = processor.tokenize("This is a test sentence")
        self.assertListEqual(tokens, ["This", "is", "a", "test", "sentence"])


class TestSRTGenerator(unittest.TestCase):
    def setUp(self):
        self.temp_dir = Path(__file__).parent / "temp"
        self.temp_dir.mkdir(exist_ok=True)
        self.output_file = self.temp_dir / "output.srt"

    def tearDown(self):
        self.output_file.unlink(missing_ok=True)

    def test_get_default_processor(self):
        generator = SRTGenerator(lang='zh')
        self.assertIsInstance(generator.processor, ChineseProcessor)

        generator = SRTGenerator(lang='en')
        self.assertIsInstance(generator.processor, EnglishProcessor)

        with self.assertRaises(ValueError):
            SRTGenerator(lang='unsupported')

    def test_convert_to_srt_chinese(self):
        generator = SRTGenerator(lang='zh', text="这是一个长句子，需要被分割成多个小句子。这是第二个长句子。")
        generator.convert_to_srt()
        expected_srt = """\  
1  
00:00:00,000 --> 00:00:03,000  
这是一个长句子，  

2  
00:00:03,000 --> 00:00:06,000  
需要被分割成多个小句子。  

3  
00:00:06,000 --> 00:00:09,000  
这是第二个长句子。  
"""
        self.assertEqual(generator.srt, expected_srt)

    def test_convert_to_srt_english(self):
        generator = SRTGenerator(lang='en',
                                 text="This is a long sentence that needs to be split into multiple ones. This is the second long sentence.")
        generator.convert_to_srt()
        expected_srt = """\  
1  
00:00:00,000 --> 00:00:03,000  
This is a long  

2  
00:00:03,000 --> 00:00:06,000  
sentence that needs  

3  
00:00:06,000 --> 00:00:09,000  
to be split into  

4  
00:00:09,000 --> 00:00:12,000  
multiple ones.  

5  
00:00:12,000 --> 00:00:15,000  
This is the second  

6  
00:00:15,000 --> 00:00:18,000  
long sentence.  
"""
        self.assertEqual(generator.srt, expected_srt)

    def test_create_srt_file_chinese(self):
        generator = SRTGenerator(lang='zh', text="这是一个需要转换成SRT的长句子。")
        generator.create_srt_file(self.output_file)
        with open(self.output_file, 'r', encoding="utf-8") as f:
            content = f.read()
        expected_srt = """\  
1  
00:00:00,000 --> 00:00:03,000  
这是一个需要转换成SRT的  

2  
00:00:03,000 --> 00:00:06,000  
长句子。  
"""
        self.assertEqual(content, expected_srt)

    def test_create_srt_file_english(self):
        generator = SRTGenerator(lang='en', text="This is a long sentence that needs to be converted to SRT.")
        generator.create_srt_file(self.output_file)
        with open(self.output_file, 'r', encoding="utf-8") as f:
            content = f.read()
        expected_srt = """\  
1  
00:00:00,000 --> 00:00:03,000  
This is a long  

2  
00:00:03,000 --> 00:00:06,000  
sentence that needs  

3  
00:00:06,000 --> 00:00:09,000  
to be converted to  

4  
00:00:09,000 --> 00:00:12,000  
SRT.  
"""
        self.assertEqual(content, expected_srt)

    def test_create_srt_file_with_post_process(self):
        def post_process(word: str) -> str:
            return word.upper()

        generator = SRTGenerator(lang='en', text="This is a test.")
        generator.create_srt_file(self.output_file, post_process)
        with open(self.output_file, 'r', encoding="utf-8") as f:
            content = f.read()
        expected_srt = """\  
1  
00:00:00,000 --> 00:00:03,000  
THIS IS A  

2  
00:00:03,000 --> 00:00:06,000  
TEST.  
"""
        self.assertEqual(content, expected_srt)


if __name__ == '__main__':
    unittest.main()