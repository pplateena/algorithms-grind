class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for n in range(1, n+1):
            if n % 5 == 0 and n % 3 == 0:
                answer.append("FizzBuzz")
            elif n % 3 == 0:
                answer.append("Fizz")
            elif n % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(n))

        return answer

    class Solution:
        def fizzBuzz(self, n: int) -> list[str]:
            return ["FizzBuzz" if n % 15 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else str(n) for n in range(1, n + 1)]