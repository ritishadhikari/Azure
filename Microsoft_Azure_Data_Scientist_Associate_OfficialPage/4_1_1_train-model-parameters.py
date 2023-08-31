# This file is supposed to reside under a src directory
import argparse
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt


def main(args):
    df=get_data(path=args.training_data)
    X_train, X_test, y_train, y_test=split_data(df=df)
    model=train_model(reg_rate=args.reg_rate,
                      X_train=X_train,
                      y_train=y_train)
    evaluate_model(model=model,
                   X_test=X_test,
                   y_test=y_test)

def parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument("--training_data",dest="training_data",type=str)
    parser.add_argument("--reg_rate",dest="reg_rate",type=float, default=0.01)
    args=parser.parse_args()
    return args

def get_data(path):
    df=pd.read_csv(path)
    return df

def split_data(df):
    X= df[['Pregnancies','PlasmaGlucose','DiastolicBloodPressure','TricepsThickness',
    'SerumInsulin','BMI','DiabetesPedigree','Age']].values 
    y=df['Diabetic'].values
    X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.30, random_state=0)
    return X_train, X_test, y_train, y_test

def train_model(reg_rate,X_train,y_train):
    model=LogisticRegression(C=1/reg_rate,solver="liblinear")
    model.fit(X_train,y_train)
    return model

def evaluate_model(model,X_test,y_test):
    y_hat=model.predict(X_test)
    acc=np.average(y_test==y_hat)
    print(f"Accuracy:{acc}")

    y_scores=model.predict_proba(X_test)
    auc=roc_auc_score(y_test, y_scores[:,1])
    print(f"AUC:{auc}")

    fpr, tpr, thresholds=roc_curve(y_test,y_scores[:,1])
    fig=plt.figure(figsize=(6,4))
    plt.plot([0,1],[1,0],"k--")
    plt.plot(fpr, tpr)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title('ROC Curve')

if __name__=="__main__":
    args=parse_args()
    main(args)
    print("*" * 60)
    print("\n\n")