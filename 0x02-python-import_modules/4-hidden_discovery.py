#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4.pyc
    # Print sorted name from directory
    for name in sorted(dir(hidden_4.pyc)):
        # print only names that do not start with __
        if name[:2] != '__':
            print("{}".format(name))

