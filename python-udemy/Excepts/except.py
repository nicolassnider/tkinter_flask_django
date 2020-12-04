while True:
    try:
        n=float(input("valor:\n"))
        print(13/n)

    except TypeError:
        print("Valor no permitido")
    except ValueError:
        print("Error de valor")
    except ZeroDivisionError:
        print("División por cero")
    except Exception as e:
        print("Error ->", type(e).__name__)
    else:
        print("ok")
        break