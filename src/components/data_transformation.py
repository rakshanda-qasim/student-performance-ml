import pandas as pd
from sklearn.model_selection import train_test_split


class DataTransformation:

    def preprocess(self, df: pd.DataFrame, target_column):

        # strip spaces in column names (VERY IMPORTANT)
        df.columns = df.columns.str.strip()

        # check target column exists
        if target_column not in df.columns:
            raise Exception(f"Target column '{target_column}' not found. Available columns: {df.columns}")

        X = df.drop(columns=[target_column])
        y = df[target_column]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=0.2,
            random_state=42
        )

        return X_train, X_test, y_train, y_test