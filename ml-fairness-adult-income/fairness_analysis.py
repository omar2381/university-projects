import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

import aif360
from aif360.algorithms.preprocessing import DisparateImpactRemover
from aif360.datasets import BinaryLabelDataset
from aif360.algorithms import Transformer

import warnings 
warnings.filterwarnings(action = 'ignore') 



df = pd.read_csv("./adult.csv",header= None)

df = df.rename(columns={0: "age",
                        1: "job_type",
                        2: "fnlwgt",
                        3: "degree",
                        4:"education-num", 
                        5: "marital_status", 
                        6: "occupation",
                        7: "relationship", 
                        8: "race", 
                        9: "sex", 
                        10: "gain", 
                        11: "loss", 
                        12: "hours", 
                        13: "origin", 
                        14: "income"})

del df['degree'] 
df = df[df['income'].notna()]
df = df.reset_index(drop= True)
total = df.shape[0]
ran_state = 21
test_size = 0.3

#function which graphs all the groups
def graph():
    for col in df.columns:
        col = "degree"
        fig, ax = plt.subplots()
        sns.countplot(x = col, data = df, order=df[col].value_counts().iloc[:3].index)
        ax.set_xlabel(col,fontsize=17);
        plt.show()

#function for subsampling x data
def subsample_x(x):
    del x["race"]

    temp = pd.DataFrame(np.zeros(((int(x.shape[0]/2)), 1)))
    race = pd.DataFrame(np.ones(((int(x.shape[0]/2)+1), 1)))

    race = race.append(temp, ignore_index=True)

    x.insert(0, 'race', race)

    return x

#function to convert data into decimal format
def decimalise(frame):
    count = 1
    frame = pd.get_dummies(frame,dummy_na = True)
    x = np.zeros(frame.shape[0]).T
    for col, data in frame.iteritems():
        if col == "NaN":
            data.values = data.values*0
        temp = data.values*(count) 
        x = np.add(temp,x)
        count = count + 1
    x = pd.DataFrame(x)
    return(x)

#function to convert data into binary format
def binarify(frame,trait):
    frame = pd.get_dummies(frame,dummy_na = True)[trait]
    return frame

#function to calculate disparate impact
def calc_ds(ds, col1, priv_Val, unpriv_val, col2, val):
    temp = ds[ds[col1] == priv_Val]
    priv = len(temp[temp[col2] == val])/len(temp)

    temp = ds[ds[col1] == unpriv_val]
    unpriv = len(temp[temp[col2] == val])/len(temp)

    return unpriv/priv

#task2 which consists of feature selection and calculating original disparate impact
def task2(df):
    print("----------------------------------------------")
    #the privilaged race and sex and income respectively
    r = " White"
    s = " Male"
    i = " >50K"
    o = " United-States"

    # 0 means <=50K while 1 means >50K
    df["income"] = binarify(df["income"],i)

    # 0 means  Female while 1 means  Male
    df["sex"] = binarify(df["sex"],s)

    # 0 implies any race that is not  White while 1 means  White
    df["race"] = binarify(df["race"],r)

    # 0 implies any origin that is not  United-States while 1 means  United-States
    df["origin"] = binarify(df["origin"],o)

    # 0: Nan, 1 = ?, 2 = Federal-gov, 3 = Local-gov, 4 = Never-worked, 5 = Private, 6 = Self-emp-inc, 7 = State-gov, 8 = Without-pay 
    df["job_type"] = decimalise(df["job_type"])

    # 0 = Nan, 1 = Divorced, 2 = Married-AF-spouse, 3 = Married-civ-spouse, 4 = Married-spouse-absent, 5 = Never-married, 6 = Separated, 7 = Widowed
    df["marital_status"] = decimalise(df["marital_status"])

    # 0 = Nan, 1 = Husband, 2 = Not-in-family, 3 = Other-relative, 4 = Own-child, 5 = Unmarried, 6 = Wife
    df["relationship"] = decimalise(df["relationship"])

    # 0 = Nan, 1 = ?, 2 = Adm-clerical, 3 = Armed-Forces, 4 = Craft-repair, 5 = Exec-managerial, 6 = Farming-fishing, 
    # 7 =  Handlers-cleaners, 8 =  Machine-op-inspct, 9 = Other-service, 10 = Priv-house-serv, 
    # 11 = Prof-specialty, 12 = Protective-serv, 13 = Sales, 14 = Tech-support, 15 = Transport-moving   
    df["occupation"] = decimalise(df["occupation"])

    x = pd.concat([df["sex"],df["race"],df["origin"],df["job_type"],df["marital_status"],df["relationship"],df["occupation"],df["fnlwgt"],df["education-num"],df["gain"],df["loss"],df["hours"],df["age"]], axis = 1)
    y = df["income"]

    #printing the updated dataframe head
    print(df.head())

    priv = df[df['race'] == 1] # 85.4%
    unpriv = df[df['race'] != 1] # 14.5%
    print("Total percentage of white: " + str((priv.shape[0]/total)*100) + " or exactly " + str(priv.shape[0]))
    print("Total percentage of non-white: " + str((unpriv.shape[0]/total)*100) + " or exactly " + str(unpriv.shape[0]))

    priv_sex = df[df['sex'] == 1] #67%
    unpriv_sex = df[df['sex'] != 1] #33%
    print("Total percentage of male: " + str((priv_sex.shape[0]/total)*100) + " or exactly " + str(priv_sex.shape[0]))
    print("Total percentage of female: " + str((unpriv_sex.shape[0]/total)*100) + " or exactly " + str(unpriv_sex.shape[0]))

    cat = calc_ds(df, "race", 1, 0 , "income", 1)
    print("disparate impact level is: " + str(cat))

    return x, y

#task3 which consists of logistic regression and calculating model dispareate impact
def task3 (x,y):
    print("----------------------------------------------")

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state = ran_state)

    sc_X = StandardScaler()

    x_train = sc_X.fit_transform(x_train)

    x_trans = sc_X.transform(x_test)

    lr = LogisticRegression(random_state=ran_state)

    lr.fit(x_train, y_train)

    y_pred = lr.predict(x_trans)

    acc = accuracy_score(y_test, y_pred)

    print("The Accuracy of the model is: " + str(acc))

    x_test.insert(0, 'income', y_pred)

    val = calc_ds(x_test, "race", 1, 0 , "income", 1)
    print("logistic regression disparate impact level is: " + str(val))

    return lr

#task4 whih consists of aif360 disparate impact remover and calculating mitigated disparate impact
def task4(lr):
    print("----------------------------------------------")
    bld = aif360.datasets.BinaryLabelDataset(favorable_label=1, unfavorable_label=0, df=df, label_names=['income'], protected_attribute_names=['race'])

    DIR = DisparateImpactRemover(repair_level = 1.0)
    dataset_transf_train = DIR.fit_transform(bld)
    temp = dataset_transf_train.convert_to_dataframe()[0]

    DIR_x = temp.drop(['income'], axis = 1)
    DIR_y = temp['income']

    scaler = StandardScaler()
    data_std = scaler.fit_transform(DIR_x)

    x_train, x_test, y_train, y_test = train_test_split(DIR_x, DIR_y, test_size=test_size, random_state = ran_state)

    lr.fit(x_train, y_train)

    y_pred = lr.predict(x_test)

    acc = accuracy_score(y_test, y_pred)

    print("The Accuracy of the model is: " + str(acc))

    x_test.insert(0, 'income', y_pred)

    val = calc_ds(x_test, "race", 1, 0 , "income", 1)
    print("the mitigated disparate impact is:  " + str(val))


x,y = task2(df)

#x = subsample_x(x)
#graph()

lr = task3(x,y)
task4(lr)

print("----------------------------------------------")
