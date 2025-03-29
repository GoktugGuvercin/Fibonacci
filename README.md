# Fibonacci

Fibonacci sequence is a series of numbers, where each number is calculated as a sum of two preceding ones, starting with $0$ and $1$. Its mathematical representation is given as follows:

$$F(0) = 0, F(1) = 1, F(n) = F(n - 1) + F(n - 2), for \ n > 2$$

$$ <0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55>$$

Fibonacci numbers satisfy the following properties:

- **Golden Ratio:** $lim_{n \rightarrow \infty} \frac{F(n + 1)}{F(n)} \approx 1.61803$

- **Sum Property:** $F(n + 2) - 1 = \sum_{n = 1}^N F(n)$

- **Square Property:** $F(n)**2 + F(n + 1)**2 = F(2n + 1)$