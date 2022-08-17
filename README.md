# edit-distance
About:
Using Python and dynamic programming, I create an algorithm to compute the edit distance between two strings.

Reflection: 
To calculate the minimum edit cost, a similar algorithm to edit distance can be used. Instead of building a matrix to store edit distance, we can build a matrix to store the minimum cost. 

Let's talk about how we would go about building our matrix. The first step is always intiliazting the top row and first column of our matrix, which allows us to then compute the remaining values of our matrix.

Instead of initializing the top row in our matrix as an increasing sequence of numbers incrementing by 1 each time, we increment by the cost of insertion. 
For example pretend insertion costs 2: 
The top row: 0, 1, 2, 3 becomes 0, 2, 4, 6

Similarly, we can initialize the first column starting from 0 and increment each value by the cost of deletion. 

When we compute the minimum values between insertion, deletion, and substitution, instead of adding 1 to the lowest edit, we'll add the cost associated with that edit. For example, say insertion gives us the mininum edit cost, our new value will be the insertion value plus 2, assuming insertion costs 2. 

The minimum edit cost will again be the last entry in our matrix. 

Installation Instructions:

1. Download the code from this repository 
2. Navigate to the correct directory containing the code folder using the "cd" command in terminal
3. Once in the correct folder, run the test suite using the command: "python3 test_edit_distance.py"

Note: this was ran on a MacOS system using VSCode and Python 3.10.6

Repository Structure:
- edit_distance.py contains the edit distance algorithm
- test_edit_distance.py contains unit tests for various cases (run this file)

Programming Complexities:
1. Time Complexity: O(m * n)
2. Space Complexity: O(m * n) 
Note: m is the length of word1 + 1 and n is the length of word2 + 1

Brainstorming Document:
I'm linking the google document that showcases my thoughtprocess and approach to the edit distance algorithm. It also includes helpful visualizations of the algorithm matrix that I created. 
https://docs.google.com/document/d/1xEhgZ-tAn6zTn00vXlucm1MjRlCjx1X2wlLkb9Ymnxw/edit?usp=sharing

