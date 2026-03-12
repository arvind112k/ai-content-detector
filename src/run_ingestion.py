from data_ingestion import DataIngestion   # import ingestion class


if __name__ == "__main__":

    ingestion = DataIngestion(
        data_path="data/raw/ai_human_dataset.csv"
    )

    df = ingestion.run_pipeline()

    print(df.head())