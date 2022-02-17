from category_encoders.target_encoder import TargetEncoder
from category_encoders import CatBoostEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

model_LR = make_pipeline(CatBoostEncoder(),
                          StandardScaler(),
                         LinearRegression()
)

model_LR.fit(X_train, y_train)