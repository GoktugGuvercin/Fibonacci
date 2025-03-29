# Fibonacci

Fibonacci sequence is a series of numbers, where each number is calculated as a sum of two preceding ones, starting with $0$ and $1$. Its mathematical representation is given as follows:

$$F(1) = 1, \ \ F(2) = 1, \ \ F(n) = F(n - 1) + F(n - 2), \ \ \ for \ n > 2$$

$$ <1, 1, 2, 3, 5, 8, 13, 21, 34, 55, \cdots>$$

Fibonacci numbers satisfy different properties, For example, the sum of first $n$ fibonacci numbers is equal to $F(n + 2) - 1$, and the ratio of two consecutive fibonacci numbers converge to $1.61803$ as $n$ goes to the infinity, which is called golden ratio. Apart from these, a square property also exists between the terms $\\{n, \ n+1, \ 2n+1\\}$ in a way that the sum of squares of two smaller terms refers to the biggest term:

$$F(n + 2) - 1 = \sum_{n = 1}^N F(n)$$

$$lim_{n \rightarrow \infty} \frac{F(n + 1)}{F(n)} \approx 1.61803$$

$$F(n)^2 + F(n + 1)^2 = F(2n + 1)$$

## Recursion and Dynamic Programming in Fibonacci

In fibonacci sequence, each term is computable as a sum of two preceeding terms. This leads to a straightforward recursive implementation where each calculation involves two recursive calls to the previous numbers. Nevertheless, this approach causes an exponential time complexity, as it repeatedly recalculates the same terms multiple times. 

Dynamic programming addresses this inefficiency by storing previously computed terms in a table so that it can retrieve any entry as requested. This makes sures that each term is calculated only once, and improves the performce from exponential to linear time complexity. The effect of memoization is directly reflected on recursion tree; huge part of it is completely pruned.

<p align="center">
  <img src="https://github.com/GoktugGuvercin/Fibonacci/blob/main/images/recursion_tree.png" width="700" title="Recursion Tree">
</p>

In the image given above, a recursion tree is constructed for the computation of $7$th term in fibonacci sequence. Once a term is computed, it is saved in fibonacci table. In that way, same recursive call is not made again. At this point, green circles are pruned recursive calls with the help of memoization. 