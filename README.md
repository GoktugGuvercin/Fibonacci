# Fibonacci

Fibonacci sequence is a series of numbers, where each number is calculated as a sum of two preceding ones, starting with $0$ and $1$. Its mathematical representation is given as follows:

$$F(1) = 1, \ \ F(2) = 1, \ \ F(n) = F(n - 1) + F(n - 2), \ \ \ for \ n > 2$$

$$ <1, 1, 2, 3, 5, 8, 13, 21, 34, 55, \cdots>$$

The sum of first $n$ fibonacci numbers is equal to $F(n + 2) - 1$, and the ratio of two consecutive fibonacci numbers converge to $1.61803$ as $n$ goes to the infinity, which is called golden ratio. Apart from these, a special square property is satisfied between the terms $<n, n+1, 2n+1>$ in a way that the sum of squares of two smaller terms refers to the biggest term:

$$lim_{n \rightarrow \infty} \frac{F(n + 1)}{F(n)} \approx 1.61803$$

$$F(n + 2) - 1 = \sum_{n = 1}^N F(n)$$

$$F(n)^2 + F(n + 1)^2 = F(2n + 1)$$