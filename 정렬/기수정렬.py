
'''

digit(d,k)
d=653
digit(d,1) -> 3
digit(d,2) -> 5
digit(d,3) -> 6
'''

def digit(d,k):
    result = 0
    if k==1:
        result = d%10
    if k==2:
        result = (d%100)//10
    if k==3:
        result = d//100
    if k==4:
        result = (d%10000)//1000
    if k==5:
        result = d//10000
    return result

def enqueue(queue, data):
    queue.append(data)

def dequeue(queue):
    if len(queue) == 0:
        print('공백')
        return -1
    else:
        data = queue.pop(0)
        return data

