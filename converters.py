class Converters:
    __char_mapping = {'0': '零',
                      '1': '一',
                      '2': '二',
                      '3': '三',
                      '4': '四',
                      '5': '五',
                      '6': '六',
                      '7': '七',
                      '8': '八',
                      '9': '九'}
    __digit_pos_char = ['', '十', '百', '千']
    __section_char = ['兆', '億', '萬']

    @classmethod
    def number_2_chinese_characters(cls, in_value):
        out_text = ''
        if isinstance(in_value, int):
            in_value = str(in_value)

        for index in range(0, len(in_value)):
            out_text += cls.__char_mapping[in_value[index]]

        return out_text

    @classmethod
    def convert_nnnn(cls, in_string):
        out_text = ''
        in_len = len(in_string)
        pad_zeros = False

        for digit in range(0, in_len):
            if in_string[digit] == '零':
                if not pad_zeros:
                    pad_zeros = True
            else:
                if pad_zeros:
                    out_text += '零'
                out_text += in_string[digit]
                out_text += cls.__digit_pos_char[in_len-1-digit]
                pad_zeros = False

        return out_text

    @classmethod
    def number_2_chinese_words(cls, in_value):
        return


if __name__ == '__main__':
    converter = Converters()
    text = converter.convert_nnnn('二零一一')
    print(text)
