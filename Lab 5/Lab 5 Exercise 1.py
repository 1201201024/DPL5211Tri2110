def meter_to_cm(m):
    cm = m * 100
    return cm


def get_meter():
    m = float(input("Enter meter : "))
    cm = meter_to_cm(m)
    print("{:.2f} meters equal to {:.2f} centimeters ".format(m, cm))


def cm_to_meter(cm):
    m = cm / 100
    return m


def get_cm():
    cm = float(input("Enter centimeter : "))
    m = cm_to_meter(cm)
    print("{:.2f} centimeters equal to {:.2f} meters ".format(cm, m))


def main():
    print("======================================")
    print("                MENU")
    print("======================================")
    print("  1.    Convert centimeter to meter")
    print("  2.    Convert meter to centimeter")
    print("======================================")
    choice = float(input("Enter your choice : "))
    if (choice == 1):
        get_cm()
    elif (choice == 2):
        get_meter()
    else:
        print("Invalid choice")


main()