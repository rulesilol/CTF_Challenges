**Difficulty Level**: Medium\
Little Chris is afraid of deathly afraid of heights. He wants to know the how high the staircase will get 
before he steps on. Can you help him find the maximum height of the stairs?\
You are given a starting height, ending height and the spacing between the two. You must place the steps in such a way
that each step is one above or one below the previous step. The final step placed must lead onto the ending step. Each 
step is 1 unit by 1 unit square. You must create a staircase with the maximal height and return this height.

**Input:**\
The first input is starting height - *integer*\
The second input is the height the staircase must end on - *integer*\
The third input is the spacing between the start and end - *integer*

**Output:**\
The maximum height of the staircase created

**Example:**\
Input: startHeight=5, endHeight=6, length=6\
Output: 9\
**Explanation**:\
Our starting height is 5. So we can go up 4 steps (to a height of 9) before we are required to start moving down in order 
to reach the ending height. Therefore, the maximum height is 9.

<img src="./ExampleImage.png" width="700" />
