newc.ipynb,omcars.ipynb - Source code for data preprocessing and model development.
price.py - Deployed Streamlit application for price prediction.
car_price.png - screenshot of streamlit app
Approach:
 Data Processing
Imported all city’s dataset which is in unstructured format.
Converted it into a  structured format.
Added a new column named ‘City’ and assign values for all rows with the name of the respective city.
Concatenate all datasets and make it as a single dataset.
Handled Missing Values: Identify and fill or remove missing values in the dataset.
For numerical columns, used techniques like mean, median, or mode imputation.depending upon its skew value

Standardising Data Formats:
Checked for all data types and do the necessary steps to keep the data in the correct format.
Eg. If a data point has string formats like 70 kms, then remove the unit ‘kms’ and change the data type from string to integers.

Encoding Categorical Variables: Converted categorical features into numerical values using encoding techniques.
Use one-hot encoding for nominal categorical variables.

Normalizing Numerical Features: Scale numerical features to a standard range, usually between 0 and 1.( For necessary algorithms)
Appled Min-Max Scaling 
Removed Outliers: Identifed and removed  outliers in the dataset to avoid skewing the model.
Used IQR (Interquartile Range) method or Z-score analysis.



 Exploratory Data Analysis (EDA)
Descriptive Statistics: Calculate summary statistics to understand the distribution of data.
Mean, median, mode, standard deviation, etc.

Data Visualization: Created visualizations to identify patterns and correlations.
Used scatter plots, histograms, box plots, and correlation heatmaps.

Feature Selection: Identify important features that significantly impact the car prices.
Used techniques like correlation analysis, feature importance from models.

 Model Development
 
Train-Test Split: Split the dataset into training and testing sets to evaluate model performance.
Common split ratios are 70-30 or 80-20.

Model Selection: Choose appropriate machine learning algorithms for price prediction.
Linear Regression, Decision Trees, Random Forests, Gradient Boosting Machines, etc.
values showed that randomforest model performed well 

Model Training: Trained the selected models on the training dataset.

Use cross-validation techniques to ensure robust performance.
Hyperparameter Tuning: Optimize model parameters to improve performance.
Use techniques like Grid Search or Random Search.

 Model Evaluation
Performance Metrics: Evaluate model performance using relevant metrics.
Mean Absolute Error (MAE), Mean Squared Error (MSE), R-squared.
Model Comparison: Compare different models based on evaluation metrics to select the best performing model.

obtained accuracy - 
 Deployment
Streamlit Application: Deploy the final model using Streamlit to create an interactive web application.
Allow users to input car features and get real-time price predictions.
User Interface Design: Ensure the application is user-friendly and intuitive.
Provide clear instructions and error handling.
obtained(R-Squared Score: 0.8691390591709017) 87% accuracy
