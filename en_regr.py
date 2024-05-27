import pickle
import pandas as pd 
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error, r2_score

ed = pd.read_csv('energy_dataset_.csv')
print(ed.head())

# Target
y1 = 'GHG_Emission_Reduction_tCO2e'
y2 = 'Jobs_Created'
X_train= ed.drop(columns = [y1,y2])
y_train = ed[y1]


lasso = Lasso(alpha=0.1)  
lasso.fit(X_train, y_train)
y_pred_train = lasso.predict(X_train)

print(y_pred_train[0])


rmse_train = mean_squared_error(y_train, y_pred_train, squared=False)
print(f"RMSE: {rmse_train:.2f}")


model_filename = 'modely1.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(lasso, file)

print(f"Modello salvato in {model_filename}")









