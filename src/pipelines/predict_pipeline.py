class PredictPipeline:

    def predict(self, model, data):

        prediction = model.predict(data)

        return prediction