#3.	Read From File (Single Input)

def read_single_input_from_file(filename):
    try:
        with open(filename, 'r') as file:
            line = file.readline().strip()
            length, width = map(float, line.split(','))

            if length <= 0 or width <= 0:
                raise ValueError("Dimensions must be positive numbers")

            return length, width

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except ValueError as e:
        print(f"Invalid input in file: {e}")
        return None

def calculate_area_from_file(filename):
    dimensions = read_single_input_from_file(filename)

    if dimensions:
        length, width = dimensions
        area = length * width

        print(f"\nFile Input Results:")
        print(f"Rectangle Area: {length} * {width} = {area} square units")

        return area

    return None

filename = '/content/rectangle_input.txt'
calculate_area_from_file(filename)