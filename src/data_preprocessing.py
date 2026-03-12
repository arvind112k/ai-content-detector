import re   # regex operations
import nltk

from nltk.corpus import stopwords   # stopword list
from nltk.stem import WordNetLemmatizer   # lemmatization


class TextPreprocessor:

    def __init__(self):

        # English stopwords
        self.stop_words = set(stopwords.words("english"))

        # lemmatizer
        self.lemmatizer = WordNetLemmatizer()


    def clean_text(self, text):

        # convert to lowercase
        text = text.lower()

        # remove URLs
        text = re.sub(r"http\S+", "", text)

        # remove punctuation
        text = re.sub(r"[^a-zA-Z\s]", "", text)

        # remove extra spaces
        text = re.sub(r"\s+", " ", text).strip()

        return text


    def remove_stopwords(self, text):

        words = text.split()

        filtered_words = [
            word for word in words if word not in self.stop_words
        ]

        return " ".join(filtered_words)


    def lemmatize_text(self, text):

        words = text.split()

        lemmatized_words = [
            self.lemmatizer.lemmatize(word)
            for word in words
        ]

        return " ".join(lemmatized_words)


    def preprocess(self, text):

        text = self.clean_text(text)

        text = self.remove_stopwords(text)

        text = self.lemmatize_text(text)

        return text