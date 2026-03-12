import pandas as pd   # pandas -> data handling
import os             # os -> file operations


class DataIngestion:

    def __init__(self, data_path):

        self.data_path = data_path
        self.processed_path = "data/processed/processed_data.csv"


    def load_data(self):

        df = pd.read_csv(self.data_path)

        print("Dataset Loaded")

        return df


    def validate_data(self, df):

        required_columns = ["text", "human_or_ai"]

        for col in required_columns:
            if col not in df.columns:
                raise Exception(f"Missing column: {col}")

        df = df.dropna(subset=["text", "human_or_ai"])

        print("Validation Completed")

        return df


    def convert_labels(self, df):

    # normalize labels
        df["human_or_ai"] = df["human_or_ai"].str.lower().str.strip()

    # mapping
        df["label"] = df["human_or_ai"].map({
        "human": 0,
        "ai": 1
        })

    # remove rows where mapping failed
        df = df.dropna(subset=["label"])

    # convert to integer
        df["label"] = df["label"].astype(int)

        return df


    def select_features(self, df):

        df = df[["text", "label"]]

        return df


    def save_processed_data(self, df):

        os.makedirs("data/processed", exist_ok=True)

        df.to_csv(self.processed_path, index=False)

        print("Processed Data Saved")


    def run_pipeline(self):

        df = self.load_data()

        df = self.validate_data(df)

        df = self.convert_labels(df)

        df = self.select_features(df)

        self.save_processed_data(df)

        print("Dataset Shape:", df.shape)

        print("Label Counts:")
        print(df["label"].value_counts())

        return df