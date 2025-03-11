import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(0)

# Generate 7 random samples with sample size 200
sample_size = 200
num_samples = 7
mean = 100
std_dev = 20

samples = [np.random.normal(mean, std_dev, sample_size) for _ in range(num_samples)]

# Plot unimodal density curves
plt.figure(figsize=(10, 6))
for sample in samples:
    sns.kdeplot(sample, label='Sample')
plt.title('Unimodal Density Curves of Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()  # Ensure this is called to display the plot

# Generate multimodal density curve by combining samples
combined_sample = np.concatenate(samples)
plt.figure(figsize=(10, 6))
sns.kdeplot(combined_sample, label='Combined Sample')
plt.title('Multimodal Density Curve of Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()  # Ensure this is called to display the plot

# Generate and plot histogram for blood pressure distribution
blood_pressure_mean = 80
blood_pressure_std_dev = 20
blood_pressure_sample = np.random.normal(blood_pressure_mean, blood_pressure_std_dev, sample_size)

plt.figure(figsize=(10, 6))
plt.hist(blood_pressure_sample, bins=30, density=True, alpha=0.6, color='g', label='Blood Pressure Histogram')
sns.kdeplot(blood_pressure_sample, color='r', label='KDE')
plt.title('Distribution of Diastolic Blood Pressure for Men')
plt.xlabel('Blood Pressure')
plt.ylabel('Density')
plt.legend()
plt.show()  # Ensure this is called to display the plot