import sys
import os

sys.path.append(os.path.abspath("."))

from src.pipelines.train_pipeline import TrainPipeline


def main():

    file_path = "data/StudentsPerformance.csv"

    target_column = "math score"

    pipeline = TrainPipeline()

    model, metrics = pipeline.run_pipeline(
        file_path,
        target_column
    )

    print(metrics)


if __name__ == "__main__":

    main()