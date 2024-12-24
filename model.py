import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

def train_and_save_model():
    data = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv')
    x = data.drop(['medv'], axis=1)
    y = data['medv']
    x_train , x_test , y_train , y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(x_train,y_train)
    
    with open('model.pkl', 'wb') as file:
        pickle.dump(model , file)    

if __name__ == "__main__" :
    train_and_save_model()
            