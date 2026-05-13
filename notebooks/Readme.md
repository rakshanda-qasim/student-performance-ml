Data Exploration
Observations
Most students score between 10 and 14, indicating average performance.
Previous grades (G1, G2) have a very strong correlation with the final grade (G3), making them strong predictors.
The number of past failures has a negative impact on final performance.
Study time and absences show weak correlation, suggesting other factors may influence performance.

Pre-processing Observation
No missing values found in the dataset.
Removed G1 and G2 to avoid data leakage
Converted categorical variables using one-hot encoding
Split data into training and testing sets (80/20)
Applied feature scaling using StandardScaler

Model Comparison
Three models were trained: Linear Regression, Decision Tree, and Random Forest
Performance was evaluated using MAE and RMSE
Random Forest performed best due to its ability to handle non-linear relationships