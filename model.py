import pandas as pd
from pycaret import classification

def train_model() -> None:
    """Trains and compares models, save the best and creates log files"""
    df = pd.read_csv('./dataset/data.csv')
    df.drop(['PassengerId', 'Name', 'Ticket', 'Fare', 'Cabin'], axis=1, inplace=True)
    classification.setup(
        df, 
        target='Survived', 
        session_id=42, 
        silent=True, 
        html=False, 
        log_experiment=True)
    best = classification.compare_models()
    best_model = classification.finalize_model(best)
    classification.save_model(best_model, 'model')
    classification.get_logs(save=True)


def load_model(model: str='model'):
    """Loads the model using Pycare's load model function"""
    return classification.load_model(model)


if __name__ == '__main__':
    train_model()