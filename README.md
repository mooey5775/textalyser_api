Python Textalyser
=================

Analyzes features in text using a call to [Textalyzer](http://textalyser.net/). Uses `requests` and `BeautifulSoup4`. Requires Python >3.6.

This package is not official and uses some specific wording to extract information from the response from textalyser.net, so some functionality may break in the future if textalyser.net is updated.

Usage
-----

Currently, this package supports extracting some basic information about text. More detailed analytics coming soon.

A new Textalyser object can be created through:

`talyze = Textalyser("This is some text")`

Afterwards, some parameters can be accessed:

 - `word_count`: Total word count
 - `distinct_word_count`: Number of distinct words
 - `lexical_density`: Lexical density (between 0-1)
 - `gunning_fog`: Gunning-Fog Readability
 - `char_count`: Number of characters
 - `char_count_no_spaces`: Number of characters excluding spaces
 - `avg_syllables`: Average number of syllables per word
 - `sentence_count`: Number of sentences
 - `avg_sentence_length`: Average length of sentences
 - `max_sentence_length`: Max length of sentence
 - `longest_sentence`: Longest sentence (string)
 - `min_sentence_length`: Min length of sentence
 - `alt_readability`: Alternate readability metric
