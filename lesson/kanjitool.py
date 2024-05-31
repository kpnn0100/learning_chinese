import pandas as pd
import os
import argparse
# Create a sample DataFrame
# Get the current file path
index_file = os.path.join(os.path.dirname(__file__), "index.txt")
hsk_level_file = os.path.join(os.path.dirname(__file__), "hsk.txt")
current_path = os.path.abspath(__file__)
hsk_level =1
# Get the relative path to the CSV file
csv_path = os.path.join(os.path.dirname(current_path), '..', 'resource')
prefix = "hsk"
def getShuffledKanjiDataFrame(hsk=1):
    if hsk <1:
        hsk = 1
    if hsk>6:
        hsk = 6
    df = pd.DataFrame()
    for i in range(1,hsk):
        csv_path = os.path.join(os.path.dirname(current_path), '..', 'resource', f'{prefix}{i}.csv')
        df.append(pd.read_csv(csv_path))
    # Shuffle the DataFrame with a fixed seed
    shuffled_df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    return shuffled_df
def getWordRange(start, end):
    df = getShuffledKanjiDataFrame()
    selected_words = df.iloc[start:end]
    return selected_words
def getTodayWords(learning_rate):
    if not os.path.exists(index_file):
        with open(index_file, "w") as file:
            file.write("0")
            number = 0
    else:
        with open(index_file, "r") as file:
            number = int(file.read())
    if args.increment:
        number += 1
        with open(index_file, "w") as file:
            file.write(str(number))
        exit()
    start = number * learning_rate
    end = start + learning_rate
    selected_words = getWordRange(start, end)
    print(selected_words)
    return selected_words
def getOldWords(learning_rate):
    if not os.path.exists(index_file):
        with open(index_file, "w") as file:
            file.write("0")
            number = 0
    else:
        with open(index_file, "r") as file:
            number = int(file.read())
    if args.increment:
        number += 1
        with open(index_file, "w") as file:
            file.write(str(number))
        exit()
    start = 0
    end = (number) * learning_rate

    if number == 0:
        end = learning_rate
    print (f"start: {start}, end: {end}")
    selected_words = getWordRange(start, end)
    print(selected_words)
    return selected_words

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--increment", action="store_true", help="Increment the index by 1")
parser.add_argument("-p", "--decrement", action="store_true", help="Decrement the index by 1")
parser.add_argument("-hsk", "--hsk", type=int, default=1, help="Number of words to learn per session")
args = parser.parse_args()

if not os.path.exists(hsk_level_file):
    with open(hsk_level_file, "w") as file:
        file.write("1")
        hsk_level = 1
else:
    with open(hsk_level_file, "r") as file:
        hsk_level = int(file.read())
if args.hsk:
    hsk_level = args.hsk
    with open(hsk_level_file, "w") as file:
        file.write(str(hsk_level))

if not os.path.exists(index_file):
    with open(index_file, "w") as file:
        file.write("0")
        number = 0
else:
    with open(index_file, "r") as file:
        number = int(file.read())
if args.increment:
    number += 1
    print(f"lesson {number}")
    with open(index_file, "w") as file:
        file.write(str(number))
if args.decrement:
    number -= 1
    number = max(0, number)
    print(f"lesson {number}")
    with open(index_file, "w") as file:
        file.write(str(number))
exit()