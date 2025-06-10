import pandas as pd

def load_data():
    return pd.read_csv("sub_dataset_3.csv")

df = load_data()
df = pd.DataFrame(df)

# Character to remove
char_to_remove = ' title="Hosted by imgur.com" />'

# Remove the character from the 'text' column
df['short_text'] = df['short_text'].str.replace(char_to_remove, '', regex=False)

output_file = "sub_dataset_3.csv"
df.to_csv(output_file, index=False)  # Set index=False to avoid saving row indices to the CSV
