#https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        command = input().split()
        cmd_type = command[0]
        
        if cmd_type == "insert":
            i = int(command[1])
            e = int(command[2])
            lst.insert(i, e)
        elif cmd_type == "print":
            print(lst)
        elif cmd_type == "remove":
            e = int(command[1])
            lst.remove(e)
        elif cmd_type == "append":
            e = int(command[1])
            lst.append(e)
        elif cmd_type == "sort":
            lst.sort()
        elif cmd_type == "pop":
            lst.pop()
        elif cmd_type == "reverse":
            lst.reverse()