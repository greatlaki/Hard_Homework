import time


N = 1000000

functions_division_4 = {
    0: lambda n: n / 4,
    1: lambda n: 3 * (n - 1) / 2 + 2,
    2: lambda n: 3 * (n - 2) / 2 + 4,
    3: lambda n: 3 * (n - 3) / 2 + 5,
}

values_and_steps = {
    1: 0,
    2: 1,
    4: 2,
    8: 3,
    16: 4,
}


def counting_steps(number: int, count=0) -> None:
    dic = {}
    while number not in values_and_steps.keys():
        dic.update({number: count})
        number = functions_division_4[number % 4](number)
        count += 2
    number_count = values_and_steps[number] + count
    for j in dic:
        dic[j] = number_count - dic[j]
    values_and_steps.update(dic)


start = time.time()
print(range(N - 1, N//2, -2))
for i in range(N - 1, N//2, -2):
    counting_steps(i)

max_key = max(values_and_steps, key=values_and_steps.get)
print(f"The number {max_key} has {values_and_steps[max_key]} steps")

print(f"Time: {time.time() - start} seconds")