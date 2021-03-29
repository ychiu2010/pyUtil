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
    __section_char = ['', '萬', '億', '兆']

    @classmethod
    def number_2_chinese_chars(cls, in_value):
        out_text = ''
        if isinstance(in_value, int):
            in_value = str(in_value)

        for index in range(0, len(in_value)):
            out_text += cls.__char_mapping[in_value[index]]

        return out_text

    @classmethod
    def number_2_chinese_words(cls, in_value):
        out_text = ''
        in_string = in_value
        if isinstance(in_value, int):
            in_string = str(in_value)

        if '0' == in_string:
            return cls.__char_mapping[in_string]
        if '10' == in_string:
            return '十'

        in_len = len(in_string)
        pad_zeros = False
        section_zeros = 0

        for digit in range(in_len - 1, -1, -1):
            index = in_len - 1 - digit
            if in_string[index] == '0':
                if not pad_zeros:
                    pad_zeros = True
                section_zeros += 1
            else:
                if pad_zeros:
                    out_text += cls.__char_mapping['0']
                    section_zeros = 0

                out_text += cls.__char_mapping[in_string[index]]
                out_text += cls.__digit_pos_char[digit % 4]
                pad_zeros = False

            if (0 < digit // 4) and (0 == digit % 4):
                if 4 != section_zeros:
                    out_text += cls.__section_char[digit // 4]
                    pad_zeros = False
                    section_zeros = 0
        return out_text


if __name__ == '__main__':
    converter = Converters()
    text = converter.number_2_chinese_words(0)
    print(text)
