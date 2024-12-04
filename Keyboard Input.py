#2.	Keyboard Input

def calculate_area_interactive():
        length = float(input("Enter rectangle length: "))
        width = float(input("Enter rectangle width: "))
        if length <= 0 or width <= 0:
            raise ValueError("Dimensions must be positive numbers")
        else:
            area = length * width
            print(f"\nCalculation Results:")
            print(f"Rectangle Area with length {length} and width: {width} is {area} square units")

            return area

calculate_area_interactive()