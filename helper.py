# _*_ encoding:utf-8 _*_
__author__ = 'xiao'
__date__ = '2018/8/20 11:11'


def verify_isbn_or_word(word):
    """
    isbn isbn13 : 13个0-9的数字组成
    isbn10 10个0-9的数字组成，含有一些' - '
    现在的新书基本上都是isbn13   isbn10 是很早的书籍了
    :param word:
    :return:
    """
    isbn_or_key = "key"
    if len(word) == 13 and word.isdigit():
        isbn_or_key = "isbn"
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = "isbn"

    return isbn_or_key
