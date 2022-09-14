import numpy as np
import pandas as pd

#Read data and conditions for BMI classification as fata files
 
data_file = './data.json'
criteria_file = './criteria.csv'

#Calculate BMI and assign the levels using numpy functions

def bmi_classify(data_file, criteria_file):
    df = pd.read_json(data_file)
    dict_df = pd.read_csv(criteria_file)

    df['BMI'] = df.apply(lambda row: row.WeightKg/((row.HeightCm/100) ** 2), axis=1)

    criteria = [
        df['BMI'] <= 18.4,
        (df['BMI'] >= 18.5) & (df['BMI'] <= 24.9),
        (df['BMI'] >= 25) & (df['BMI'] <= 29.9),
        (df['BMI'] >= 30) & (df['BMI'] <= 34.9),
        (df['BMI'] >= 35) & (df['BMI'] <= 39.9),
        df['BMI'] >= 40
    ]

    bmi_category_levels = list(dict_df['BMI Category'])

    health_risk_levels = list(dict_df['Health risk'])

    df['BMI Category'] = np.select(criteria, bmi_category_levels, default=0)
    df['Health Risk'] = np.select(criteria, health_risk_levels, default=0)

    return df


def get_weight_category_count(df, weight_category):
    return df['BMI Category'].value_counts().get(weight_category)

#Test basic assertions
 
def test_get_overweight_count1():
    assert get_weight_category_count(completed_dataframe, 'Overweight') == 1


def test_get_underweight__count2():
    assert get_weight_category_count(completed_dataframe, 'Underweight') is None

#Test the bmi classify criteria on given input and obtain count of overweight people

bmi_df = bmi_classify(data_file, criteria_file)
overweight_bmi_count = get_weight_category_count(bmi_df, 'Overweight')

print(bmi_df)
print('\n')
print('The count of overweight people based on bmi criteria is: ' + str(overweight_bmi_count))

