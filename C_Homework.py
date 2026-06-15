import sys

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    
    idx = 0
    t = int(input[idx])
    idx += 1
    
    for _ in range(t):
        n = int(input[idx])
        a = input[idx+1]
        m = int(input[idx+2])
        b = input[idx+3]
        c = input[idx+4]
        idx += 5
        
        # We use a list for the string for efficient prepending
        # But for n, m <= 10, simple concatenation is fine
        res = a
        for i in range(m):
            char = b[i]
            who = c[i]
            if who == 'V':
                res = char + res # Prepend
            else:
                res = res + char # Append
        print(res)

if __name__ == "__main__":
    solve()