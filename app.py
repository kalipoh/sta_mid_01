import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Displaying the problem
st.subheader("Problem")
st.markdown("""
A **market research agency** conducted a survey of **200 customers** who purchased various electronic products in the Jakarta area. 
Each customer was asked to provide a **satisfaction rating** for the products they purchased, using a **scale of 1 to 5**, where:

- **1** means "Very Dissatisfied"
- **2** means "Dissatisfied"
- **3** means "Neutral"
- **4** means "Satisfied"
- **5** means "Very Satisfied"

The survey results are summarized in the following table:
""")

# Customer satisfaction survey data
ratings = [1, 2, 3, 4, 5]
frequencies = [30, 45, 50, 40, 35]

data = pd.DataFrame({"Rating (x)": ratings, "Frequency (f)": frequencies})

# Displaying data table
st.table(data.set_index("Rating (x)"))

st.markdown("""
**Tasks:**
1. Create a **probability distribution** for the random variable x.
2. Draw a **histogram** based on the probability distribution.
3. Calculate the **mean and variance** of the probability distribution.

ANSWER
""")
st.header("QUESTION 1")
st.write("Customer Survey Data")

data = {
    1: 30,
    2: 45,
    3: 50,
    4: 40,
    5: 35
}

df_data = pd.DataFrame(list(data.items()), columns=['Rating (x)', 'Frequency (f)'])
st.table(df_data.set_index('Rating (x)'))  # Remove initial index

total_respondents = sum(data.values())
st.write(f"**Total Respondents (N):** {total_respondents}")

st.write("Calculating Probability for Each Rating")

probabilities = {}
for rating, frequency in data.items():
    p = frequency / total_respondents
    probabilities[rating] = p
    st.write(f"P({rating}) = {frequency} / {total_respondents} = {p:.3f}")

# Create probability DataFrame with 'Rating (x)' column
prob_data = {'Rating (x)': list(probabilities.keys()), 'Probability P(x)': list(probabilities.values())}
df_probability = pd.DataFrame(prob_data)

df_distribution = pd.merge(df_data, df_probability, on='Rating (x)')
st.table(df_distribution.set_index('Rating (x)'))  # Remove initial index

st.write("""
**Thus, the probability distribution using the formula:**
P(x) = f / N
""")

st.write("""
**Formula Explanation:**
P(x) = f / N
 - P(x): Probability of each rating value x
 - f: Frequency of rating x (number of occurrences for specific rating)
 - N: Total frequency (total number of respondents)
""")


st.header("QUESTION 2")
st.write("Histogram")
image = Image.open("histo.png")
st.image(image, caption='Probability Distribution Histogram', use_container_width=True)

image = Image.open("histog.png")
st.image(image, caption='Probability Distribution Histogram', use_container_width=True)

image = Image.open("grafik.png")
st.image(image, caption='Probability Distribution Histogram', use_container_width=True)

image = Image.open("bunder.png")
st.image(image, caption='Probability Distribution Histogram', use_container_width=True)

image = Image.open("grfk.png")
st.image(image, caption='Probability Distribution Histogram', use_container_width=True)


st.header("QUESTION 3")
st.write("Mean")

def calculate_probability_distribution_mean(data):
    """Calculate mean (average value) of probability distribution."""
    df = pd.DataFrame(data)
    df['x * P(x)'] = df['Rating (x)'] * df['Probability P(x)']
    mean = df['x * P(x)'].sum()
    return mean, df  # Return mean and DataFrame

def display_results(data, mean):
    """Display survey data and mean calculation results."""
    df = pd.DataFrame(data)
    st.write("Survey Data:")
    st.table(df.set_index('Rating (x)'))
    st.write(f"Mean (μ): {mean}")

def display_calculation_steps(df, mean):  # Accepts DataFrame df
    """Display mean calculation steps."""
    multiplications = [f"{x} * {px}" for x, px in zip(df['Rating (x)'], df['Probability P(x)'])]
    multiplication_results = df['x * P(x)'].tolist()

    st.write("Mean Calculation Steps (μ):")
    st.write(f"μ = ({' + '.join(multiplications)})")
    st.write(f"μ = {multiplication_results}")
    st.write(f"μ = {mean}")

# Survey data
survey_data = {
    'Rating (x)': [1, 2, 3, 4, 5],
    'Frequency (f)': [30, 45, 50, 40, 35],
    'Probability P(x)': [0.150, 0.225, 0.250, 0.200, 0.175]
}

# Calculate mean and get DataFrame
mean_result, df_result = calculate_probability_distribution_mean(survey_data)

# Display results
display_results(survey_data, mean_result)
display_calculation_steps(df_result, mean_result)  # Using returned DataFrame


def calculate_probability_distribution_variance(data, mean):
    """Calculate variance of probability distribution."""
    df = pd.DataFrame(data)
    df['(x - μ)^2'] = (df['Rating (x)'] - mean) ** 2
    df['P(x) * (x - μ)^2'] = df['Probability P(x)'] * df['(x - μ)^2']
    variance = df['P(x) * (x - μ)^2'].sum()
    return variance, df  # Return variance and DataFrame

def display_variance_results(data, mean, variance):
    """Display variance calculation results."""
    df = pd.DataFrame(data)
    st.write("Variance Calculation Method (σ^2):")
    st.table(df)
    st.write(f"Variance (σ^2): {variance}")

def display_variance_calculation_steps(df, mean, variance):
    """Display variance calculation steps."""
    step_1 = [f"({px} * ({x} - {mean})^2)" for x, px in zip(df['Rating (x)'], df['Probability P(x)'])]
    step_2 = [(px * (x - mean) ** 2) for x, px in zip(df['Rating (x)'], df['Probability P(x)'])]
    step_3 = [f"{v:.3f}" for v in step_2]

    st.write("Variance Calculation Steps (σ^2):")
    st.write(f"σ^2 = ({' + '.join(step_1)})")
    st.write(f"σ^2 = ({' + '.join(map(str, step_2))})")
    st.write(f"σ^2 = {' + '.join(step_3)}")
    st.write(f"σ^2 = {variance}")

# Survey data
survey_data = {
    'Rating (x)': [1, 2, 3, 4, 5],
    'Probability P(x)': [0.150, 0.225, 0.250, 0.200, 0.175]
}

# Previously calculated mean
mean_result = 3.025

# Calculate variance and get DataFrame
variance_result, df_result = calculate_probability_distribution_variance(survey_data, mean_result)

# Display results
display_variance_results(survey_data, mean_result, variance_result)
display_variance_calculation_steps(df_result, mean_result, variance_result)