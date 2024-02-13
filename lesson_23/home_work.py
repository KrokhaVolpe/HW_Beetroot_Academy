import time
from typing import List, Tuple

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} took {runtime:.4f} secs")
        return result
    return wrapper


@timer #O(log n)
def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res


@timer #O(O(n^2)
def question2(n: int) -> int:
	for _ in range(10):
		n **= 3
	return n

@timer #O(n!)
def question3(first_list: List[int], second_list: List[int])-> List[int]:
   temp: List[int] = first_list[:]
   for el_second_list in second_list:
      flag = False
      for check in temp:
         if el_second_list == check:
            flag = True
            break
      if not flag:
         temp.append(second_list)
   return temp


@timer #O(n)
def question4(input_list: List[int]) -> int:
  res: int = 0
  for el in input_list:
    if el > res:
      res = el
  return res


@timer #O(n)
def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res

@timer #O(1) 
def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n




first_list_1 = list(range(1, 1001))
second_list_1 = list(range(501, 1501))
first_list_2 = list(range(1, 10001))
second_list_2 = list(range(5001, 15001))


question1(first_list_1, second_list_1)
question1(first_list_2, second_list_2)
print("="*20)

question2(5)
question2(50)
print("="*20)

question3(first_list_1, second_list_1)
question3(first_list_2, second_list_2)
print("="*20)

question4(list(range(1, 1001)))
question4(list(range(1, 10001)))
print("="*20)

question5(10)
question5(100)
print("="*20)

question6(256)
question6(1024)


