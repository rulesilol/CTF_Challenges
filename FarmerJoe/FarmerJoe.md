Difficulty Level: Medium
Farmer Joe wants to has many cows and wants to build a rectangular fence for his cows and has an
infinitely long wall he can build his fence against. Therefore, he only needs to build three sides of the fence
However, he has only has limited budget. Can you help him find the largest area he can make his fence, given the 
budget and cost of fencing material?
P.S. Round the area down to the nearest integer. Joe hates paying land taxes!!!

**Input:**\
The first input is Joe's budget - *float* \
The second input is the cost per metre of fencing - *float*

**Output:**\
The maximum area possible given the Joe's budget and cost of fencing - *integer*

**Example:**\
Input: budget=640.0, fenceCost=8.0\
Output: 800\
**Explanation**:\
Having a fence with a length of 40 and a width of 20 means 80m of fencing material and will cost $640. This will give
an area of 800, which is the maximum area.

```
                                  Length
                  ┌────────────────────────────────────────┐
                  │                                        │
                  │                                        │
                  │                                        │
            Width │                                        │ Width
                  │                                        │
                  │                                        │
┌─────────────────┴────────────────────────────────────────┴─────────────────┐
│                                   Wall                                     │
└────────────────────────────────────────────────────────────────────────────┘
```