def main():
    first_run = True

    while True:
        if first_run:
            print("\nWelcome to stoaCalc :)")
            first_run = False

        print("\nPlease choose a shape to calculate area:")
        print("1. Rectangle")
        print("2. Square")
        print("3. Triangle")
        print("4. Circle")
        print("5. Parallelogram")
        print("6. Trapezoidal")
        print("7. Ellipse")
        print("8. Exit")

        user_choice = input("Type in choice number: ")

        match user_choice:
            case "1":
                print(f"Rectangle Area: {rect_area()}")
            case "2":
                print(f"Square Area: {square_area()}")
            case "3":
                print(f"Triangle Area: {triangle_area()}")
            case "4":
                print(f"Circle Area: {circle_area()}")
            case "5":
                print(f"Parallelogram Area: {parallelogram_area()}")
            case "6":
                print(f"Trapezoidal Area: {trapezoidal_area()}")
            case "7":
                print(f"Ellipse Area: {ellipse_area()}")
            case "8":
                print("Goodbye :)")
                break
            case _:
                print("Invalid choice. Please try again.")

def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def rect_area():
    length = get_positive_number("Enter the length of the rectangle: ")
    width = get_positive_number("Enter the width of the rectangle: ")
    return length * width

def square_area():
    side = get_positive_number("Enter the side length of the square: ")
    return side * side

def triangle_area():
    base = get_positive_number("Enter the base of the triangle: ")
    height = get_positive_number("Enter the height of the triangle: ")
    return 0.5 * base * height

def circle_area():
    radius = get_positive_number("Enter the radius of the circle: ")
    return 3.14 * radius * radius

def parallelogram_area():
    base = get_positive_number("Enter the base of the parallelogram: ")
    height = get_positive_number("Enter the height of the parallelogram: ")
    return base * height

def trapezoidal_area():
    base1 = get_positive_number("Enter the length of base1: ")
    base2 = get_positive_number("Enter the length of base2: ")
    height = get_positive_number("Enter the height of the trapezoid: ")
    return 0.5 * (base1 + base2) * height

def ellipse_area():
    a = get_positive_number("Enter the length of the semi-major axis (a): ")
    b = get_positive_number("Enter the length of the semi-minor axis (b): ")
    return 3.14 * a * b

main() 