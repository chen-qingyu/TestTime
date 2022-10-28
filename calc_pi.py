if __name__ == "__main__":
    N = 1E7
    x, y, hits = 0, 0, 0
    while x * x < N:
        y = 0
        while y * y < N:
            if x * x + y * y < N:
                hits += 1
            y += 1
        x += 1
    print(f"{(hits / N) * 4}")
