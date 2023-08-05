# text_analysis.py

import nltk
from nltk.corpus import opinion_lexicon
from nltk.corpus import stopwords
import re
from textblob import TextBlob

def compute_text_analysis(article_text):
    # Download NLTK resources if not already downloaded
    nltk.download("punkt")
    nltk.download("opinion_lexicon")
    nltk.download("stopwords")

    # Cleaning the text using stop words
    stop_words = set(stopwords.words("english"))
    words = nltk.word_tokenize(article_text)
    words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

    # Creating dictionary of positive and negative words
    positive_words = set(opinion_lexicon.positive())
    negative_words = set(opinion_lexicon.negative())

    # Extracting derived variables
    positive_score = sum(word in positive_words for word in words)
    negative_score = sum(word in negative_words for word in words)
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (len(words) + 0.000001)

    # TextBlob for additional sentiment analysis
    blob = TextBlob(article_text)
    sentiment = blob.sentiment
    additional_positive_score = sentiment.polarity
    additional_subjectivity_score = sentiment.subjectivity

    # Analysis of Readability
    sentences = nltk.sent_tokenize(article_text)
    total_words = len(words)
    total_sentences = len(sentences)
    avg_sentence_length = total_words / total_sentences

    complex_words = [word for word in words if len(word) > 2]
    percentage_of_complex_words = len(complex_words) / total_words
    fog_index = 0.4 * (avg_sentence_length + percentage_of_complex_words)

    # Average Number of Words Per Sentence
    avg_words_per_sentence = total_words / total_sentences

    # Complex Word Count
    complex_word_count = len(complex_words)

    # Syllable Count Per Word
    def count_syllables(word):
        word = word.lower()
        if len(word) <= 3:
            return 1
        count = 0
        vowels = "aeiouy"
        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith("e"):
            count -= 1
        if word.endswith("le") and len(word) > 2 and word[-3] not in vowels:
            count += 1
        if count == 0:
            count = 1
        return count

    syllable_per_word = sum(count_syllables(word) for word in words) / len(words)

    # Personal Pronouns
    personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', article_text, re.IGNORECASE))

    # Average Word Length
    avg_word_length = sum(len(word) for word in words) / len(words)

    # Create a dictionary with all the required keys and their respective values
    analysis_result = {
        "positive_score": positive_score,
        "negative_score": negative_score,
        "polarity_score": polarity_score,
        "subjectivity_score": subjectivity_score,
        "avg_sentence_length": avg_sentence_length,
        "percentage_of_complex_words": percentage_of_complex_words,
        "fog_index": fog_index,
        "avg_words_per_sentence": avg_words_per_sentence,
        "complex_word_count": complex_word_count,
        "word_count": total_words,
        "syllable_per_word": syllable_per_word,
        "personal_pronouns": personal_pronouns,
        "avg_word_length": avg_word_length,
        "additional_positive_score": additional_positive_score,
        "additional_subjectivity_score": additional_subjectivity_score
    }

    return analysis_result
