from transformers import pipeline

class SubtitleTranslator:
    def __init__(self, model_name='Helsinki-NLP/opus-mt-en-zh'):
        self.pipe = pipeline('translation', model=model_name)

    def translate(self, text, src_lang='en', tgt_lang='zh'):
        # transformers pipeline自动检测语言，模型需支持目标语言
        result = self.pipe(text)
        return result[0]['translation_text']

# 示例用法：
# translator = SubtitleTranslator()
# zh_text = translator.translate('Hello world!')
# print(zh_text)
