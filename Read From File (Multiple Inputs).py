#4.	Read From File (Multiple Inputs)

def read_multiple_inputs_from_file(filename):
    try:
        with open(filename, 'r') as file:
            inputs = [
                tuple(map(float, line.strip().split(',')))
                for line in file if line.strip()
            ]

            for length, width in inputs:
                if length <= 0 or width <= 0:
                    raise ValueError("All dimensions must be positive numbers")
            return inputs

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except ValueError as e:
        print(f"Invalid input in file: {e}")
        return None

def calculate_areas_from_multiple_inputs(filename):
    input_sets = read_multiple_inputs_from_file(filename)

    if input_sets:
        print("\nMultiple Input Results:\n")
        results = []

        for index, (length, width) in enumerate(input_sets, 1):
            area = length * width
            results.append(area)
            print(f"The area of Rectangle {index} with length {length} and width {width} is: {area} square units\n")

        return results
    return None

filename = '/content/multiple_rectangle_inputs.txt'
calculate_areas_from_multiple_inputs(filename)