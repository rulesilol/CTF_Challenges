**Solution Writeup**\
We know that we can build $\frac{budget}{fenceCost}$ amount of fencing. For example, if the budget is $640 and the price of fencing is $8/m, then we can build up to 80m of fencing. In other words, $2\times$ Width + Length is $\frac{budget}{fenceCost}$. We first give half the fecing to the length and the rest to the widths. We first give half the fencing to the length, $\frac{1}{2} \times\frac{budget}{fenceCost}$, and then give the other half to the widths. However, there is two widths. Thus each widths only gets $\frac{1}{4}$ of the total fencing i.e. $\frac{1}{4} \times\frac{budget}{fenceCost}$.Therefore, length is $\frac{1}{2} \times\frac{budget}{fenceCost}$ and width is $\frac{1}{4} \times\frac{budget}{fenceCost}$. The area is given by length $\times$ width, giving us the solution.\
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