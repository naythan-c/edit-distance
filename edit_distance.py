def edit_distance(word1, word2):
    #Check if there's an empty string, if there is: raise an error
    if not word1 or not word2:
        raise ValueError("Empty strings are not allowed!")
    # Create our matrix
    matrix = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]

    # Fill the top row 
    for i in range(len(word2) + 1):
        matrix[0][i] = i

    # Fill the first column 
    for j in range(len(word1) + 1):
        matrix[j][0] = j

    # Iterate bottom up through our matrix, utilizing dynamic programming to fill our matrix until we figure out the edit distance
    for index1, character1 in enumerate(word1, 1):
        for index2, character2 in enumerate(word2, 1):
            if character1 == character2:  # if the last characters match, it's the same edit distance as without the last character
                # set matrix value to the value without the last character
                matrix[index1][index2] = matrix[index1 - 1][index2 - 1]
            else:
                # if the last characters don't match, find the minimum edit distance between the insert, delete, and replace edits
                matrix[index1][index2] = min(
                    matrix[index1][index2 - 1], matrix[index1 - 1][index2], matrix[index1 - 1][index2 - 1]) + 1

    # If you want to visualize the matrix, uncomment this line of code:
    # print('\n'.join(['\t'.join([str(cell) for cell in row])
    #       for row in matrix]))

    # Return the final value in our matrix, which corresponds with the edit distance
    return matrix[len(word1)][len(word2)]
