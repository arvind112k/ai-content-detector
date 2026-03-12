import pandas as pd

from data_preprocessing import TextPreprocessor


def run_preprocessing():

    # load processed dataset
    df = pd.read_csv("data/processed/processed_data.csv")

    preprocessor = TextPreprocessor()

    print("Starting Text Preprocessing...")

    df["clean_text"] = df["text"].apply(
        preprocessor.preprocess
    )

    print("Preprocessing Completed")

    # save dataset
    df.to_csv(
        "data/processed/cleaned_data.csv",
        index=False
    )

    print("Cleaned dataset saved")

    return df


if __name__ == "__main__":

    df = run_preprocessing()

    print(df.head())