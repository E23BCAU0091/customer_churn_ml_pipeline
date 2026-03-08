from sklearn.metrics import accuracy_score

class ModelEvaluation:

    def evaluate(self, model, X_test, y_test):

        pred = model.predict(X_test)

        accuracy = accuracy_score(y_test, pred)

        return accuracy
