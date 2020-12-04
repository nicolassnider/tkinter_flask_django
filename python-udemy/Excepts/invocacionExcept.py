try:
    n=None

    if n is None:
        raise ValueError()
    if n==0:
        raise FileExistsError()
        
except ValueError:
    print("error de null")
except FileExistsError:
    print("file error")
