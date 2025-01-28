import numpy as np
import pandas as pd
from scipy.stats import norm

# Load the dataset from the CSV file
file_path = "https://github.com/shahid3167/Ensemble_Learning_with_Semantic_Feature_Fusion/blob/main/Dataset/Statistical_Analyses_Dataset/Average_Accuracy_Dataset.csv"
# Ensure the URL is properly formatted for downloading raw data
raw_path = file_path.replace("/blob/", "/").replace("github.com", "raw.githubusercontent.com")

# Read the CSV file
data = pd.read_csv(raw_path)

# Define the models and their corresponding data
models = {
    "FCN": data["FCN-Average-Accuracy"],
    "CNN": data["CNN-Average-Accuracy"],
    "GRU": data["GRU-Average-Accuracy"],
    "LSTM": data["LSTM-Average-Accuracy"],
    "Ensemble": data["Ensemble-Average-Accuracy"]
}

# Function to calculate descriptive statistics
def calculate_statistics(data):
    n = len(data)  # Sample size
    mean = np.mean(data)
    sd = np.std(data, ddof=1)  # Sample standard deviation
    z_critical = norm.ppf(0.975)  # Z critical value for 95% CI
    margin_error = z_critical * (sd / np.sqrt(n))  # Margin of error
    ci_lower = mean - margin_error
    ci_upper = mean + margin_error

    return {
        "Sample Size": n,
        "Mean": round(mean, 2),
        "SD": round(sd, 2),
        "Critical Value (z)": round(z_critical, 2),
        "Error Range": round(margin_error, 2),
        "95% CI": f"[{round(ci_lower, 2)}, {round(ci_upper, 2)}]"
    }

# Calculate statistics for all models
statistics = {model: calculate_statistics(data) for model, data in models.items()}

# Create a DataFrame to display the results
stats_df = pd.DataFrame(statistics).T
stats_df.index.name = "Model Name"
stats_df.reset_index(inplace=True)

# Add a column for the performance metric
stats_df.insert(1, "Performance Metric", "Average-Accuracy")

print(stats_df)

