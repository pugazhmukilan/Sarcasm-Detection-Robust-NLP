import json
import csv
import string
import Data_Preprocessor 
def Headline_preprocess_tocsv():
    Sarcasm = []
    Headline = []

    # Open the file and process each line separately
    with open('src/Sarcasm_Headlines_Dataset.json', 'r') as f:
        for line in f:
            try:
                data = json.loads(line.strip())  # Parse each line as a separate JSON object
                data['headline'] = Data_Preprocessor.preprocessor(data['headline'])
                Sarcasm.append(data['is_sarcastic'])
                Headline.append(data['headline'])
            except json.JSONDecodeError as e:
                print(f"Error parsing line: {e}")



    with open ('src/Headline_Dataset.csv',mode= 'w',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Sentence","is_Scarcastic"])
        for headline_sentence, sarcasm_label in zip(Headline, Sarcasm):
            writer.writerow([headline_sentence, sarcasm_label])

    print("File has been saved")

Headline_preprocess_tocsv()



