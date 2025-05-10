import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values(by='score', ascending=False)
    scores.drop(columns=['id'], inplace=True)
    scores['rank'] = scores['score'].rank(ascending=False, method='dense')

    return scores