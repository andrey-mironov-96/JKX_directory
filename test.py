def my_print():
    return print(4+5)

def switch(case:int):
    try:
        __switch={0:my_print,
                  }
        return __switch[case]
    except:
        print("error",end="")


