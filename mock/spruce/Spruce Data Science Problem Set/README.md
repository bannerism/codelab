# Spruce Data Science Problem Set

Hello! Thank you for your interest in a role on the Data Science team 
at Spruce! We are excited to get to know you better throughout the interview
process. On our team, we combine skills in the domains of mathematics, computer
science, and business acumen to develop creative solutions for Spruce operations
team members and clients.

On this team we mostly develop in Python and store data in  our PostgreSQL database. To succeed on this team means being familiar with using these tools
on a daily basis. We do not expect you to know everything and one of the best
parts of being on the team is that we all learn from each other all the time.

Please take some time to demonstrate your competency in the core elements of
our stack and show off some of your skills! This problem set can be completed in
about 30 minutes, but do not worry if it takes you much longer or shorter to complete.

Honesty and integrity are also key traits that make a successful data scientist at Spruce. As you attempt this skills challenge, please refrain from looking up answers on the internet, collaborating with a friend, or consulting with a popular large language model (e.g. Chat GPT). We promise this will be the last time we ask you not to use one of these resources.

_You may, however, refer to Python
documentation to refresh yourself on built-in functions, syntax, or modules._

As you solve these problems please keep the following goals top of mind:
1. My code solves the problem as asked.
2. My code is readable, interpretable, and well-commented.
3. My code is robust to edge cases or outliers.
4. My code runs efficiently and uses memory efficiently.

Lastly, our team is big on test-driven development and code coverage. While you are not required to write unit tests, please feel free to include a few
if you'd like to spend the extra time to show off. Good luck!

## SQL
> ### Q1
> Given the following two tables, `employees` and `salaries`, write a SQL query to retrieve the average salary for each department:
>
> Table: `employees`
> 
> |emp_id|name|department_id|
> |---|---|---|
> |1|Alice|1|
> |2|Bob|2|
> |3|Charlie|1|
> |4|David|2|
> |5|Eve|3|
>
> Table: `salaries`
> |salary_id|emp_id|amount|
> |---|---|---|
> |1|1|5000|
> |2|2|6000|
> |3|3|5500|
> |4|4|6500|
> |5|5|7000|
>
> Your query should return the following result:
> |department_id|average_salary|
> |---|---|
> |1|5250|
> |2|6250|
> |3|7000|

## Python
> ### Q2
> Your teammate wrote a Python function called is_palindrome that takes a string as input and returns True if the string is a palindrome (reads the same forwards and backwards), and False otherwise. The function should be case-insensitive and should ignore any non-alphanumeric characters. For example, is_palindrome("12321") should return True. However, this function does not seem to be working on more complex strings. Please fix your teammate's code so we can get the hotfix deployed ASAP!
>
> Here are a few test cases to check your work.
> 
> ```python
> print(is_palindrome("12321"))  # True
> print(is_palindrome("A man, a plan, a canal, Panama!"))  # True`
> print(is_palindrome("Python"))  # False
> print(is_palindrome("Madam Arora teaches malayalam"))  # True
> print(is_palindrome("Hello, World!"))  # False
> ```

> ### Q3
> You previously wrote a Python function called unique_elements that takes a list of integers as input and returns a new list containing only the unique elements from the original list. You successfully wrote a function that did this, but now the stakeholder has let you know that the order of the elements in the new list should be the same as their first occurrence in the original list. For example, unique_elements([4, 2, 3, 2, 1, 4, 5, 4]) should return [4, 2, 3, 1, 5].
>
> Here are a few test cases to check your work.
> 
> ```python
> print(unique_elements([4, 2, 3, 2, 1, 4, 5, 4]))  # [4, 2, 3, 1, 5]
> print(unique_elements([3, 3, 3, 3, 3]))  # [3]
> print(unique_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))  # [1, 2, 3, 4, 5]
> print(unique_elements([]))  # []
> ```

> ### Q4
>Write a Python class called BankAccount that represents a bank account. The class should have the following methods:
> 
> * `__init__(self, name, initial_balance)`: Initializes the bank account with the given `name` and initial_balance.
> 
> * `deposit(self, amount)`: Adds the given `amount` to the account balance.
> 
> * `withdraw(self, amount)`: Subtracts the given `amount` from the account balance.
> 
> * `get_balance(self)`: Returns the current account balance.
>
> Here's an example usage of the `BankAccount` class:
>
>
> ```python
> account = BankAccount("John Doe", 1000)
> account.deposit(500)
> account.withdraw(200)
> print(account.get_balance())  # Output: 1300
>```
> Here are a few test cases to check your work.
> 
> ```python
> account = BankAccount("John Doe", 1000)
> print(account.get_balance())  # 1000
> account.deposit(500)
> print(account.get_balance())  # 1500
> account.withdraw(200)
> print(account.get_balance())  # 1300
> account.withdraw(1500)  # Insufficient funds.
> ```
> You want to go above and beyond to impress your users. Using your knowledge of bank accounts, create and implement another useful method for the BankAccount class. Be sure to give it a docstring and comments so your team knows about the additional functionality!