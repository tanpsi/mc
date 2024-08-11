from handler import solve

if __name__ == "__main__":
    print("Use natural math input (actually pythonic); exit/quit to quit")
    while True:
        try:
            if (i:=input('> ').strip()) in ("quit", "exit"):
                raise EOFError
        except EOFError:
            print("\nBye!")
            break
        print(solve(i))
