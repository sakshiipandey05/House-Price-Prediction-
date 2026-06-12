import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = {
    'Area':[1000,1200,1500,1800,2000,2200,2500,2800,3000,3500],
    'Bedrooms':[2,2,3,3,3,4,4,4,5,5],
    'Bathrooms':[1,2,2,2,3,3,3,4,4,5],
    'Parking':[1,1,2,2,2,2,3,3,3,4],
    'Price':[25,30,40,45,55,60,70,80,90,100]
}

df = pd.DataFrame(data)

X = df[['Area','Bedrooms','Bathrooms','Parking']]
y = df['Price']

model = LinearRegression()

model.fit(X,y)

pickle.dump(model, open('house_model.pkl','wb'))

print("House Price Model Saved Successfully")