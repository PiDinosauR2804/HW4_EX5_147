# TODO: [part d]
# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import argparse
import utils
import pandas as pd

def main():
    accuracy = 0.0

    # Compute accuracy in the range [0.0, 100.0]
    ### YOUR CODE HERE ###
    # index_london = []
    london_correct = 0
    all = 0
    df = pd.read_csv('birth_dev.tsv', sep='\t', header=None, names=['question', 'place'])
    for idx, row in df.iterrows():
        if row['place'] == 'London':
            london_correct += 1
        all += 1

    accuracy = london_correct/all
    ### END YOUR CODE ###

    return accuracy

if __name__ == '__main__':
    accuracy = main()
    with open("london_baseline_accuracy.txt", "w", encoding="utf-8") as f:
        f.write(f"{accuracy*100}%\n")
