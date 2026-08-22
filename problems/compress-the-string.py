#https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
def slv(string):
    l, r = 0, 0
    d = []

    while l < len(string):
        currcnt = 0
        while r < len(string) and ord(string[l]) == ord(string[r]):
            currcnt += 1
            r += 1

        d.append((currcnt ,int(string[l])))
        l = r

    return d

if __name__ == '__main__':
    s = input().strip()
    print(*slv(s))
