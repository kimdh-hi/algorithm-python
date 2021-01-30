numbers = [2,1,3,4,1]
answer = []
l = len(numbers)
for i in range(l):
    for j in range(i + 1, l):
        sum = numbers[i] + numbers[j]
        print(sum)
        if sum not in answer:
            answer.append(sum)
        else:
            sum = 0
print(answer)