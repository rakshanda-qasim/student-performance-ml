from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error


class ModelEvaluation:

    def evaluate(self, model, X_test, y_test):

        predictions = model.predict(X_test)

        r2 = r2_score(y_test, predictions)

        rmse = mean_squared_error(
            y_test,
            predictions,
            squared=False
        )

        return {
            "R2 Score": r2,
            "RMSE": rmse
        }