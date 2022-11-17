import numpy as np
import pandas as pd

from src.utils.algorithm_utils import Algorithm

class Random_guessing(Algorithm):
    def __init__(self, name='random_guess', seed: int=None, save_dir=None, multi_outputs=True):
        """Isolation Forest algorithm for anomaly detection.

        Args:
            name (str, optional)            : Algorithm's name. Defaults to 'IForest'.
            seed (int, optional)            : Random seed. Defaults to None.
            save_dir ([type], optional)     : Folder to save the outputs. Defaults to None.

        """
        Algorithm.__init__(self, __name__, name, seed=seed)
        self.model = None
        self.seed = seed
        self.save_dir = save_dir
        self.additional_params = {}
        self.multi_outputs = multi_outputs
        self.init_params = {
            'save_dir' : save_dir,
            'seed' : seed,
            'multi_outputs': multi_outputs
        }
        
        

        
    def fit(self, train_data : np.array, categorical_columns=None):
        """Fit the model.

        Args:
            train_data (pd.DataFrame): Training dataframe.
            categorical_columns (list, optional): Column to be one-hot encoded.
                                                Defaults to None.
        """
        

    def predict(self, test_data : pd.DataFrame):
        """Predict on the test dataframe

        Args:
            test_data (pd.DataFrame): Test dataframe.
            if_shap (bool, optional): If Shap values is computed during prediction. Defaults to True.

        Returns:
            np.array: Test predictions.
        """
        np.random.seed(self.seed)
        preds = []
        pred_size = test_data.shape[1]
        for i in range(test_data.shape[0]):
            preds.append(np.random.randint(low=0, high=2, size=(pred_size,)))
        anomalies = np.concatenate(preds)
        predictions_dict = {'anomalies': anomalies,
                                'anomalies_score' : anomalies
                               }
        return predictions_dict