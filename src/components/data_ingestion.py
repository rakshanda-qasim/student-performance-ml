import pandas as pd


class DataIngestion:

    def load_data(self, file_path):

        df = pd.read_csv(file_path)

        return df