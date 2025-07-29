import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(person[person.duplicated('email')]['email'].unique(), columns=['email'])