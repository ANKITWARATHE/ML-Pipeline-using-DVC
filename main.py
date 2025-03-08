import os

print("Running the data ingestion script")
os.system("python src/data_ingestion.py")

print("Running the data preprocessing script")
os.system("python src/data_preprocessing.py")

print("Running the feature engineering script")
os.system("python src/feature_engineering.py")

print("Running the model building script")
os.system("python src/model_building.py")

print("Running the model evaluation script")
os.system("python src/model_evaluation.py")