#https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub = string[i:i + k]
        seen = "".join(dict.fromkeys(sub))
        print(seen)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)