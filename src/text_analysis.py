import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation



def get_top_keywords(headlines, top_n: int = 20):
    """
    Extract top TF-IDF keywords.
    """
    vectorizer = TfidfVectorizer(stop_words="english")

    matrix = vectorizer.fit_transform(headlines)


    scores = matrix.mean(axis=0).A1

    words = vectorizer.get_feature_names_out()

    keyword_df = pd.DataFrame(
        {
            "keyword": words,
            "score": scores,
        }
    )

    keyword_df = keyword_df.sort_values(by="score", ascending=False)

    return keyword_df.head(top_n)

def get_top_publishers(df: pd.DataFrame, top_n: int = 10):
    """
    Return most active publishers.
    """
    return df["publisher"].value_counts().head(top_n)



def extract_email_domains(df: pd.DataFrame) -> pd.Series:
    """
    Extract publisher email domains.
    """
    domains = df["publisher"].str.extract(r"@(.+)")

    return domains[0].value_counts()



def perform_lda_topic_modeling(headlines, n_topics: int = 5):
    """
    Perform LDA topic modeling.
    """
    vectorizer = CountVectorizer(stop_words="english")

    matrix = vectorizer.fit_transform(headlines)

    lda = LatentDirichletAllocation(
        n_components=n_topics,
        random_state=42,
    )

    lda.fit(matrix)

    feature_names = vectorizer.get_feature_names_out()

    topics = {}

    for topic_idx, topic in enumerate(lda.components_):
        top_words = [
            feature_names[i]
            for i in topic.argsort()[-10:]
        ]

        topics[f"Topic {topic_idx + 1}"] = top_words

    return topics