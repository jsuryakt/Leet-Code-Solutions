TC - O(n * n!)
Because if going column wise then the first col can be filled in n ways, next n-1 ways,
next col n-2 and so on until 1
n * (n-1) * (n-2) * (n-3) .... 1 = n!
​
Multiplication and not addition because if the first col position changes it will change all the other possibilities, just like we have 10 * 10 * 10 possible ways to fill _ _ _ slots by 0-9 digits
000 to 999, 1000 ways
​
SC - O(n) - for recursion
O(n^2) for ans
O(n^2) for board
​