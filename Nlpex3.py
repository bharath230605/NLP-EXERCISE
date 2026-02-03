import re
from collections import counter
import nltk
from nltk.corpus import stopwords
posts=["I love this new phone battery life is amazing","This updates is very bad and disappointing","Amazing camera and great perfomance","The app is slow and the interface is bad","I love the camera quality and battery performance"]
nltk.download('stopwords')
stwords=set(stopwords.words('english'))
ug,bg,tg=[],[].[]
for post in posts:
    post=post.lower()
    post=re.sub(r'[^a-z\s]',",post)
                words=[w for w in post.split() if w not in stwords]
                ug.extend(words)
                bg.extends(zip(words,words[1:]))
                tg.extends(zip(words,words[1:],words[2:]))
                ugc=Counter(ug)
                bgc=Counter(bg)
                tgc=Counter(tg)
                print("Top Unigrams:",ugc.most_common(3))
                print("\nTop Bigrams:",bgc.most_common(3))
                print("\nTop Trigrams:",tgc.most_common(3))
                from textblop import TextBlob
                print("\n Sentiment Ananlysis:")
                for post in posts:
                blob=TextBlob(post)
                polarity=blob.sentiment.polarity
                if polarity > 0:
                   print ("positive")
                elif polarity < 0:
                    print ("negative")
                else:
                    print("neutral")
                    print(f"Post:{post}'Polarity:polarity}")
                
