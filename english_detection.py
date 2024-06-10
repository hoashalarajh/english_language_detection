from detect_lang import is_english
from tqdm import tqdm  # For progress bars

texts = ["Hello this is my game",
         "Thalapathy Vijay is The greatest of all time",
         "gasaf bafasfasf asfasfas gasfreasfasf afasfa",
         "I am waiting for long time, are you here?",
         "enna pesureenga neenga? puriyalaye enakku..."]

# Check if the texts are in English and store the result in a list
english_checks = [is_english(text) for text in tqdm(texts, desc="Checking if texts are in English")] 

# implementing a logic to express which is english and non english
texts_index = 0
for bool_val in english_checks:
    if bool_val == True:
        print (f"{texts[texts_index]} is English.")
    else:
        print (f"{texts[texts_index]} is not english, please try to input english texts only...")
    texts_index = texts_index + 1
