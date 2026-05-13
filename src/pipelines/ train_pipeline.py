from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation


class TrainPipeline:

    def run_pipeline(self, file_path, target_column):

        # data ingestion
        ingestion = DataIngestion()

        df = ingestion.load_data(file_path)

        # preprocessing
        transformation = DataTransformation()

        X_train, X_test, y_train, y_test = transformation.preprocess(
            df,
            target_column
        )

        # model training
        trainer = ModelTrainer()

        model = trainer.train(
            X_train,
            y_train
        )

        # model evaluation
        evaluator = ModelEvaluation()

        metrics = evaluator.evaluate(
            model,
            X_test,
            y_test
        )

        return model, metrics