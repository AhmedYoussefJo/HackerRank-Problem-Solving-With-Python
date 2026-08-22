#https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true
if __name__ == '__main__':
    s = input().strip()
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    
    sorted_chars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    for char, count in sorted_chars[:3]:
        print(f"{char} {count}")