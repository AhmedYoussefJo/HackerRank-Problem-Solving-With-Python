#https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())
    arr.sort(key=lambda x: x[k])
    
    for row in arr:
        print(*(row))
