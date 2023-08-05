# main.py

import pandas as pd
from data_extraction import extract_article_text, save_article_to_file
from text_analysis import compute_text_analysis

# Read input URLs from "Input.xlsx"
input_df = pd.read_excel("Input.xlsx")

# Ensure the input DataFrame has all the required columns
required_columns = [
    "URL_ID",
    "URL"  # Add other required columns from "Input.xlsx" here
]
for column in required_columns:
    if column not in input_df.columns:
        raise ValueError(f"Input DataFrame is missing required column '{column}'")

# Initialize lists to store computed variables
computed_variables = {
    "positive_score": [],
    "negative_score": [],
    "polarity_score": [],
    "subjectivity_score": [],
    "avg_sentence_length": [],
    "percentage_of_complex_words": [],
    "fog_index": [],
    "avg_words_per_sentence": [],
    "complex_word_count": [],
    "word_count": [],
    "syllable_per_word": [],
    "personal_pronouns": [],
    "avg_word_length": [],
    "additional_positive_score": [],
    "additional_subjectivity_score": []

}

# Loop through each URL and extract article text
for index, row in input_df.iterrows():
    url = row["URL"]
    url_id = row["URL_ID"]
    article_title, article_text = extract_article_text(url)

    # Save the article text in a text file
    save_article_to_file(url_id, article_title, article_text)

    # Compute text analysis variables
    analysis_result = compute_text_analysis(article_text)

    # Append the computed variables to their respective lists
    for key, value in analysis_result.items():
        computed_variables[key].append(value)

# Add the computed variables to the input DataFrame
for key, value in computed_variables.items():
    input_df[key] = value

# Save the output DataFrame to "Output Data Structure.xlsx"
input_df.to_excel("Output Data Structure.xlsx", index=False)
