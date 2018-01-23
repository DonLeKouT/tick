
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import numpy as np
from tick.online import OnlineForestClassifier
from tick.simulation import weights_sparse_exp
from tick.linear_model import SimuLogReg
from sklearn.ensemble import RandomForestClassifier

np.set_printoptions(precision=2)

n_samples = 30000
n_features = 30
n_classes = 2

nnz = 5
w0 = np.zeros(n_features)
w0[:nnz] = 1

# TODO: Seed

# w0 = weights_sparse_exp(n_features, nnz=nnz)

X, y = SimuLogReg(weights=w0, intercept=None, n_samples=n_samples,
                  cov_corr=0.1, features_scaling='standard',
                  seed=123).simulate()
y = (y + 1) / 2

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=123)

rf = RandomForestClassifier(n_estimators=10, criterion="entropy",
                            random_state=123)
of = OnlineForestClassifier(n_classes=n_classes, n_trees=10, seed=123,
                             step=1., use_aggregation=True)

print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

rf.fit(X_train, y_train)
of.fit(X_train, y_train)

y_pred_rf = rf.predict_proba(X_test)[:, 1]
y_pred_of = of.predict_proba(X_test)[:, 1]

print("AUC rf=", roc_auc_score(y_test, y_pred_rf))
print("AUC of=", roc_auc_score(y_test, y_pred_of))


import matplotlib.pyplot as plt

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.stem(rf.feature_importances_)
plt.title('Breiman Random Forest', fontsize=16)
plt.subplot(1, 3, 2)
plt.stem(of.feature_importances)
plt.title('Online Forest', fontsize=16)
plt.subplot(1, 3, 3)
plt.stem(w0)
plt.title('Model weights', fontsize=16)

plt.show()
plt.tight_layout()
# print(clf.feature_importances)