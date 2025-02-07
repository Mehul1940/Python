# Type Defination In Python

# Type Defination is added using [:] and the variable -> 

x: int = 0

def test(x: int) -> None:
   return x + 1

print(test(14))

def greet(name: str) -> None:
    return(f"Hello, {name}")

print(greet("John"))

from typing import Union, List, Dict, Tuple

number: list[int] = [1, 2, 3, 4, 5]
person: dict[str, str] = {"name": "John", "age": 18}
address: tuple[str, str] = ("Street", "City")
identifier: Union[str, int] = "123"
