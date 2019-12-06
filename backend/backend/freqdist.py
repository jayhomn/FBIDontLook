from backend.piazzaAPI import *  # looks for file location and imports everything with the star
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import string
from nltk.probability import FreqDist  # this is for the frequency distribution
import nltk
nltk.download('punkt')
nltk.download('stopwords')

custom_stopwords = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "!", "?", ":", "'", "%", "，", "!", "’",
                    "question", "questions", "！", "along", "using", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def raw_dict_maker(stringin):
    # define stop/filler words and punctuation
    stop = stopwords.words('english') + list(string.punctuation) + custom_stopwords
    cleaner = TweetTokenizer()

    # string stripped of punctuation and filler words
    cleanstring = [i for i in cleaner.tokenize(stringin.lower()) if i not in stop]

    # frequency distribution of cleaned string
    fdist = FreqDist(cleanstring)

    # top 50 distribution
    fdist_50 = fdist.most_common(50)

    # convert to dictionary
    freq_dictionary = {}
    for index in range(len(fdist_50)):
        freq_dictionary.update({fdist_50[index][0]: fdist_50[index][1]})

    return freq_dictionary
