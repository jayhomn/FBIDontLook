############# splits apostrophes

# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
#
# from nltk import word_tokenize
# from nltk.corpus import stopwords
# import string
#
# sent = "this is a foo bar, bar black sheep. hello i'm kevin. a b c "
# stop = stopwords.words('english') + list(string.punctuation)
# clean = [i for i in word_tokenize(sent.lower()) if i not in stop]
# print(clean)

############ tweek tokenizer / this will take words with apostrophes as one thing

from backend.piazzaAPI import * ## looks for file location and imports everything with the star

import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import string

from nltk.probability import FreqDist ## this is for the frequency distribution


# from pycontractions import Contractions ################trying to unexpand contractions
#
# cont = Contractions(api_key="glove-twitter-100")
custom_stopwords = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",",".","!","?",":","'","%","，","!","’","question", "questions","！", "along", "using","a","b","c","d","e", "f","g","h", "i", "j", "k", "l","m","n", "o","p", "q", "r","s", "t","u", "v","w","x", "y","z"]
def raw_dict_maker(stringin):

    stop = stopwords.words('english') + list(string.punctuation) + custom_stopwords

    cleaner = TweetTokenizer()

    clean = [i for i in cleaner.tokenize(stringin.lower()) if i not in stop]



    fdist = FreqDist(clean)


    fdist1 = fdist.most_common(40)

    freq_dic = {}
    for index in range(len(fdist1)):
        freq_dic.update({fdist1[index][0]: fdist1[index][1]})

    return freq_dic
