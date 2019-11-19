# fibonacci.py

def fib():
    fibs = [1, 2]

    for i in range(1,9):

         fib_n = fibs[i] + fibs[i-1]
         fibs.append(fib_n)

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
