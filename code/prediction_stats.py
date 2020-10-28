    
import pandas as pd
import numpy as np

from sklearn.metrics import accuracy_score, precision_score, recall_score
from scipy.stats import pearsonr

orig_file = ../


def compare_income_preds(original_filepath, predicted_filepath):
    """
    Compare actual and predicted income levels
    :param original_filepath: Path of the file containing actual income level values
    :param predicted_filepath:  Path of the file containing predicted income level values
    :return: 
    """
    original_subdistrict_dict = {}
    corr_pred = []
    incorr_pred = []
    data_original = pd.read_csv(original_filepath)
    data_predicted = pd.read_csv(predicted_filepath)
    header_list = list(data_predicted)[1:]
    for ii, row in data_original.iterrows():
        original_subdistrict_dict[row['subdistrict_code']] = [row[header] for header in header_list]
    for ii, row in data_predicted.iterrows():
        predicted_values.append([row[header] for header in header_list])
        original_values.append(original_subdistrict_dict[row['subdistrict_code']])
    original_values = np.array(original_values)
    predicted_values = np.array(predicted_values)
