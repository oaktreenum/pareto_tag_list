# Script to get tag list of PDBs to open from Pareto front file
# Allon Goldberg, Research Assistant, Flatiron Institute, 7/2024

import re

def main(pareto_silent_file):

    with open(pareto_silent_file, 'r') as file:
        lines = file.readlines()
    
    tags = []
    for line in lines:
        # Split line by arbitrary spaces (whitespace) into columns
        columns = re.split(r'\s+', line.strip())
        #Save name of peptoid
        if columns[0] != 'CHAIN_ENDINGS':
            continue
        else: 
            tag = columns[-1]
            tags.append(tag)
            continue

    # Convert each element to string and join with a space
    taglist = ' '.join(str(x) for x in tags)

    # Print the result
    print(taglist)
        


if __name__ == "__main__":
    import sys
    if sys.argv[1] == 'help':
        print("Usage: python pareto_tag_list.py <input_pareto_file>")
    else:
        file_input = sys.argv[1]
        main(file_input)        