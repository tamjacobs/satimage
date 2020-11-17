    
import pandas as pd
import numpy as np

from sklearn.metrics import accuracy_score, precision_score, recall_score, mean_squared_error, r2_score
from scipy.stats import pearsonr
from scipy.special import logit


# Determines the number of subdistricts the model correctly predicts the majority class - 
# e.g. max percentage in which income class/category
def check_income_category(original_filepath, predicted_filepath,correct,incorrect,num_subdist):

    maj_class_orig = []
    maj_class_pred = []
    comp_df = []

    # Load in csv files
    data_original = pd.read_csv(original_filepath, index_col=False)
    data_predicted = pd.read_csv(predicted_filepath, index_col=False)
    header_list = list(data_predicted)[1:]
    del data_original['subdistrict_name']

    # Correct default index included
    data_original.set_index('subdistrict_code',inplace=True)
    data_predicted.set_index('subdistrict_code',inplace=True)

    # Find header of the max number e.g. largest income group
    maj_class_orig = data_original.idxmax(1)
    maj_class_pred = data_predicted.idxmax(1)
    # Compare the headers
    comp_df = maj_class_orig.compare(maj_class_pred)
    corr = len(maj_class_orig)-len(comp_df)
    incorr = len(comp_df)
    num_subdist+=len(maj_class_orig)
    if comp_df.empty:
        correct+=len(maj_class_orig)
    else:
        incorrect+=len(comp_df)
        correct+=len(maj_class_orig)-len(comp_df)
    return corr, incorr, num_subdist

    # Count the number of 0_0, 0_1, 0_2 majority classes
def count_income_category(original_filepath, num_0,num_1,num_2):

    maj_class_orig = []
    # Load in csv files
    data_original = pd.read_csv(original_filepath, index_col=False)
    #del data_original['subdistrict_name']

    data_original.set_index('subdistrict_code',inplace=True)

    # Correct default index included
    #data_original.set_index('subdistrict_code',inplace=True)
    # Find header of the max number e.g. largest income group
    maj_class_orig = data_original.idxmax(1)
    print(maj_class_orig)
    # for i in range(maj_class_orig.size):
    #     if maj_class_orig[i] == '0_0':
    #         num_0+=1
    #     elif maj_class_orig[i] == '0_1':
    #         num_1+=1
    #     elif maj_class_orig[i] == '0_2':
    #         num_2+=1
    
    return num_0, num_1, num_2

def mean_sqr_err_in(original_filepath,predicted_filepath):
    data_original = pd.read_csv(original_filepath, index_col=False)
    data_predicted = pd.read_csv(predicted_filepath, index_col=False)

    data_original.set_index('subdistrict_code',inplace=True)
    data_predicted.set_index('subdistrict_code',inplace=True)

    mse_0 = mean_squared_error((data_original['0_0']),(data_predicted['0_0']))
    mse_1 = mean_squared_error((data_original['0_1']),(data_predicted['0_1']))
    mse_2 = mean_squared_error((data_original['0_2']),(data_predicted['0_2']))

    return mse_0,mse_1,mse_2

def mean_sqr_err_dev(original_filepath,predicted_filepath):
    data_original = pd.read_csv(original_filepath, index_col=False)
    data_predicted = pd.read_csv(predicted_filepath, index_col=False)
    mse0 = []
    mse1 = []
    mse2 = []
    r2_0 = []
    r2_1 = []
    r2_2 = []

    # First indicator
    for i in range(0,9):
        indx = '0_'+str(i)
        mse0.append(mean_squared_error(data_original[indx],data_predicted[indx]))
        r2_0.append(r2_score(data_original[indx],data_predicted[indx]))

    # Second indicator
    for i in range(0,6):
        indx = '1_'+str(i)
        mse1.append(mean_squared_error(data_original[indx],data_predicted[indx]))
        r2_1.append(r2_score(data_original[indx],data_predicted[indx]))
    
    for i in range(0,10):
        indx = '2_'+str(i)
        mse2.append(mean_squared_error(data_original[indx],data_predicted[indx]))
        r2_2.append(r2_score(data_original[indx],data_predicted[indx]))
        

    mse_r2_df = [mse0,mse1,mse2,r2_0,r2_1,r2_2]

    #mse_data = [mse_00,mse_01,mse_02,mse_10,mse_11,mse_12,mse_20,mse_21,mse_22]
    #r2_data = [r2_00,r2_01,r2_02,r2_10,r2_11,r2_12,r2_20,r2_21,r2_22]

    #return mse_00,mse_01,mse_02,mse_10,mse_11,mse_12,mse_20,mse_21,mse_22,r2_00,r2_01
    return mse_r2_df

def r2(original_filepath,predicted_filepath):
    data_original = pd.read_csv(original_filepath, index_col=False)
    data_predicted = pd.read_csv(predicted_filepath, index_col=False)

    data_original.set_index('subdistrict_code',inplace=True)
    data_predicted.set_index('subdistrict_code',inplace=True)

    r2_0 = r2_score(data_original['0_0'],data_predicted['0_0'])
    r2_1 = r2_score(data_original['0_1'],data_predicted['0_1'])
    r2_2 = r2_score(data_original['0_2'],data_predicted['0_2'])
    return r2_0,r2_1,r2_2

def check_development_category(original_filepath, predicted_filepath,c0,c1,c2,w1,w2,w3,num_subdist):

    # Load in csv files
    data_original = pd.read_csv(original_filepath, index_col=False)
    data_predicted = pd.read_csv(predicted_filepath, index_col=False)
    header_list = list(data_predicted)[1:]

    # Correct default index included
    data_original.set_index('village_code',inplace=True)
    data_predicted.set_index('village_code',inplace=True)
    # Now want to go through and compare how often the prediction and original match  


def compare_income_predictions(original_filepath, predicted_filepath):
    """
    Compare actual and predicted income levels
    :param original_filepath: Path of the file containing actual income level values
    :param predicted_filepath:  Path of the file containing predicted income level values
    :return: 
    """
    original_subdistrict_dict = {}
    original_values = []
    predicted_values = []
    thresh_vals = []
    acc = 0
    prec = 0
    recall = 0
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

    str1 = str(pearsonr(original_values[:, 0], predicted_values[:, 0]))
    str2 = str(pearsonr(original_values[:, 1], predicted_values[:, 1]))
    str3 = str(pearsonr(original_values[:, 2], predicted_values[:, 2]))
    
    print("\nPoverty prediction after thresholding on class [0]: ")
    t = 0.1
    while t < 1.0:
        p1m = np.copy(original_values[:, 0])
        p1m[p1m >= t] = 1
        p1m[p1m < t] = 0
        frac = np.sum(p1m) / len(p1m)
        ot = [1 if i >= t else 0 for i in original_values[:, 0]]
        pt = [1 if i >= t else 0 for i in predicted_values[:, 0]]
        acc = str(accuracy_score(ot, pt))
        prec = str(precision_score(ot, pt))
        recall = str(recall_score(ot, pt))
        thresh_vals.append([t, acc, prec, recall])
        t += 0.1

    return str1, str2, str3, thresh_vals

def compare_dev_predictions(original_filepath, predicted_filepath):
    """
    Compare actual and predicted income levels
    :param original_filepath: Path of the file containing actual income level values
    :param predicted_filepath:  Path of the file containing predicted income level values
    :return: 
    """
    # original_village_dict = {}
    # original_values = []
    # predicted_values = []
    # thresh_vals = []
    # acc = 0
    # prec = 0
    # recall = 0
    # data_original = pd.read_csv(original_filepath)
    # data_predicted = pd.read_csv(predicted_filepath)
    # header_list = list(data_predicted)[1:]
    # for ii, row in data_original.iterrows():
    #     original_subdistrict_dict[row['village_code']] = [row[header] for header in header_list]
    # for ii, row in data_predicted.iterrows():
    #     predicted_values.append([row[header] for header in header_list])
    #     original_values.append(original_subdistrict_dict[row['village_code']])
    # original_values = np.array(original_values)
    # predicted_values = np.array(predicted_values)

    # str1 = str(pearsonr(original_values[:, 0], predicted_values[:, 0]))
    # str2 = str(pearsonr(original_values[:, 1], predicted_values[:, 1]))
    # str3 = str(pearsonr(original_values[:, 2], predicted_values[:, 2]))


    data_original = pd.read_csv(original_filepath, index_col=False)
    data_predicted = pd.read_csv(predicted_filepath, index_col=False)

    pearsr0 = []
    pearsr1 = []
    pearsr2 = []
    r2_0 = []
    r2_1 = []
    r2_2 = []

    # First indicator
    for i in range(0,9):
        indx = '0_'+str(i)
        pearsr0.append(str(pearsonr(data_original[indx],data_predicted[indx])))
        #r2_0.append(r2_score(data_original[indx],data_predicted[indx]))

    # Second indicator
    for i in range(0,6):
        indx = '1_'+str(i)
        pearsr1.append(str(pearsonr(data_original[indx],data_predicted[indx])))
        #r2_1.append(r2_score(data_original[indx],data_predicted[indx]))
    
    for i in range(0,10):
        indx = '2_'+str(i)
        pearsr2.append(str(pearsonr(data_original[indx],data_predicted[indx])))
        #r2_2.append(r2_score(data_original[indx],data_predicted[indx]))
        
    return pearsr0, pearsr1, pearsr2
