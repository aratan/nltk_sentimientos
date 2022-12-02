from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

x = "It is charming and beautiful product"
y = "It was a horrible experience"
z = "I have no idea what"

r = SentimentIntensityAnalyzer()
resultados = r.polarity_scores(x)

print(resultados)