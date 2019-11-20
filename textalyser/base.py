import requests
from requests.exceptions import RequestException

from bs4 import BeautifulSoup
import re

class Textalyser:
    def __init__(self, sentence, min_char=3, words_toanalyze=10,
                 count_numbers=1, is_log=1, stoplist_lang=1):
        URL = "http://textalyser.net/index.php?lang=en#analysis"
        data = {
            'text_main': sentence,
            'min_char': min_char,
            'words_toanalyze': words_toanalyze,
            'count_numbers': count_numbers,
            'is_log': is_log,
            'stoplist_lang': stoplist_lang
        }
        try:
            r = requests.post(url=URL, data=data)
        except RequestException:
            raise ValueError("Input too long to analyze")

        if r.status_code != 200:
            raise ValueError("Input too long to analyze")

        self.soup = BeautifulSoup(r.text, 'html.parser')
        if int(self.soup.find(text="Total word count : ").parent.find_next('td').text) == 0:
            raise ValueError("Input too long to analyze")

    @property
    def word_count(self):
        return int(self.soup.find(text="Total word count : ").parent.find_next('td').text)

    @property
    def distinct_word_count(self):
        return int(self.soup.find(text="Number of different words : ").parent.find_next('td').text)

    @property
    def lexical_density(self):
        return float(self.soup.find(text="Complexity factor (Lexical Density) : ").parent.find_next('td').text[:-1]) / 100

    @property
    def gunning_fog(self):
        return float(self.soup.find(text="Readability  (Gunning-Fog Index) : ").parent.find_next('td').text)

    @property
    def char_count(self):
        return int(self.soup.find(text="Total number of characters : ").parent.find_next('td').text)

    @property
    def char_count_no_spaces(self):
        return int(self.soup.find(text="Number of characters without spaces : ").parent.find_next('td').text)

    @property
    def avg_syllables(self):
        return float(self.soup.find(text="Average Syllables per Word : ").parent.find_next('td').text)

    @property
    def sentence_count(self):
        return int(self.soup.find(text="Sentence count : ").parent.find_next('td').text)

    @property
    def avg_sentence_length(self):
        return float(self.soup.find(text="Average sentence length (words) : ").parent.find_next('td').text)

    @property
    def max_sentence_length(self):
        return int(self.soup.find(text="Max sentence length  (words) : ").parent.find_next('td').text)

    @property
    def longest_sentence(self):
        return self.soup.find(text="Max sentence length  (words) : ").parent.parent.find_next('tr').text[1:-1]

    @property
    def min_sentence_length(self):
        return int(self.soup.find(text="Min sentence length  (words) : ").parent.find_next('td').text)

    @property
    def alt_readability(self):
        return float(self.soup.find(text="Readability  (Alternative) beta : ").parent.find_next('td').text)
