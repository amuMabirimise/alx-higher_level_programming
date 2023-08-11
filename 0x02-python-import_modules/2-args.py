#!/usr/bin/python3

if __name__ == "__main__":
    import  sys
    arguments = sys.argv[1:]
    num_args = len(arguments)

    if num_args == 0:
        print("Number of argument(s) : .")
    elif num_args == 1:
        print("Number of argument(s) : 1:")
        print("1: {}".format(arguments[0]))
    else:
        print("Number of argument(s) : {}:".format(num_args))
        for i, arg in enumerate(arguments, start=1):
            print("{}: {}".format(i, arg))

