# edit-distance
About this project:
Using Python to figure out the edit distance between two strings.

Reflection: 
To calculate the minimum edit cost, a similar algorithm can be used. Instead of building a matrix to store edit distance, we can build a matrix to store the minimum cost. Instead of initializing the top row in a matrix as an increasing sequence of numbers incrementing by 1 each time, we could increment by the cost of insertion. Similarly, we can initialize the first column starting from 0 and increment each value by the cost of deletion. When we compute the minimum values between insertion, deletion, and substitution, instead of adding 1 to the lowest edit, we'll add the cost associated with edit. The minimum edit cost will again be the last entry in our matrix. 

Installation Instructions:
1. Download the code from this repository 
2. Navigate to the correct directory containing the code folder using the "cd" command in terminal
3. Once in the correct folder, run the test suite using the command: "python3 test_edit_distance.py". It should return: 
"Ran 1 test in 0.000s

OK"

Time Complexity: O(m * n), Space Complexity: O(m * n) 
where m is the length of word1 + 1 and n is the length of word2 + 1

Brainstorming Document:
I linked the google document I used to brainstorm this problem. It includes helpful visualizations of the algorithm matrix. 
https://docs.google.com/document/d/1xEhgZ-tAn6zTn00vXlucm1MjRlCjx1X2wlLkb9Ymnxw/edit?usp=sharing

