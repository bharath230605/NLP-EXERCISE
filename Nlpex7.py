from sklearn.feature_extraction.text import
TfidVectorizer
from sklearn.metrices.pairwise
import cosine_similarity
p1="the language platform helps users improve vocabulary."
p2="this system suggests synonyms to expand vocabulary."
vec=TfidVectorizer().fit_transform([p1,p2])
score=cosine_simalarity
