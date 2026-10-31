# ==================== FUNCTIONS ====================

# Void function
def fg_void_identity():
    print("---------------------")
    print("| Rameyza Alya S    |")
    print("|      Bintaro      |")
    print("---------------------")


def fg_int_add(value1=10, value2=5):
    l_int_result = value1 + value2
    return l_int_result


def fg_int_subtract(value1=10, value2=5):
    l_int_result = value1 - value2
    return l_int_result


def fg_int_multiply(value1=10, value2=5):
    l_int_result = value1 * value2
    return l_int_result


def fg_float_divide(value1=10, value2=5):
    l_float_result = value1 / value2
    return l_float_result


def fg_int_modulus(value1=10, value2=5):
    l_int_result = value1 % value2
    return l_int_result


# ==================== MAIN PROGRAM ====================

fg_void_identity()

g_str_menu = ""

while g_str_menu != "stop":
    g_str_menu = input("Enter Menu (+|-|/|*|%|stop): ")

    if g_str_menu == "stop":
        print("Program stopped. Thank you for using my program.")

    else:
        g_int_value1 = int(input("Enter Value 1: "))
        g_int_value2 = int(input("Enter Value 2: "))

        if g_str_menu == "+":
            g_int_result = fg_int_add(g_int_value1, g_int_value2)
            print("The result of addition", g_int_value1, "+", g_int_value2, "is", g_int_result)

        elif g_str_menu == "-":
            g_int_result = fg_int_subtract(g_int_value1, g_int_value2)
            print("The result of subtraction", g_int_value1, "-", g_int_value2, "is", g_int_result)

        elif g_str_menu == "*":
            g_int_result = fg_int_multiply(g_int_value1, g_int_value2)
            print("The result of multiplication", g_int_value1, "*", g_int_value2, "is", g_int_result)

        elif g_str_menu == "/":
            g_float_result = fg_float_divide(g_int_value1, g_int_value2)
            print("The result of division", g_int_value1, "/", g_int_value2, "is", g_float_result)

        elif g_str_menu == "%":
            g_int_result = fg_int_modulus(g_int_value1, g_int_value2)
            print("The result of modulus", g_int_value1, "%", g_int_value2, "is", g_int_result)

        print()