from sklearn.linear_model import LinearRegression


class ModelTrainer:

    def train(self, X_train, y_train):

        model = LinearRegression()

        model.fit(X_train, y_train)

        return model