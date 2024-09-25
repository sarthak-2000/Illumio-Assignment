def capture_flow_log_data()-> list[list]:
    """
    Reads space-separated flow log data from a specified .txt file and returns a list of lists 
    containing necessary data only.

    Parameters:
    file_path (str): The path to the .txt file containing flow log data.

    Returns:
    list: A list of lists with extracted necessary data.
    """
    file_path = input("Please Enter the File Path Alongwith the filename for flow log data (.txt file) -> ").strip() or 'flow_log_data.txt'
    try:
        with open(file_path, 'r') as file:
            # Read all lines, strip each line, filter out empty lines, and split remaining lines by spaces
            flow_log_data = [line.strip().split() for line in file if line.strip()]
        
        # Extract necessary data (6th and 7th entries) from the flow log data
        necessary_data = extract_necessary_data(flow_log_data)
        print(necessary_data)
        return necessary_data

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except IndexError:
        print("Error: The log entries do not contain enough columns.")
        return []


def extract_necessary_data(logs: list)-> list:
    """
    Extracts necessary data from the flow log entries.

    Parameters:
    logs (list): A list of lists containing the flow log data.

    Returns:
    list: A list of lists containing the necessary data.
    """
    return [[entry[6], entry[7]] for entry in logs if len(entry) > 7]





def capture_tag_data()-> dict:
    """
    Reads tag data from a specified .txt file and converts it into a dictionary format.

    The dictionary has tuples as keys formed by the first two comma-separated values of each line,
    and values are tuples containing the last comma-separated value in both lowercase and original case.

    Parameters:
    file_path (str): The path to the .txt file containing tag data.

    Returns:
    dict: A dictionary with tuples as keys and tuples as values.
    """
    tag_data = {}
    file_path = input("Please Enter the File Path Alongwith the filename for tag data (.txt file) -> ").strip() or 'tag_data2.txt'

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Strip whitespace and check for non-empty lines
                line = line.strip()
                if line:  # Proceed only if the line is not empty
                    # Split by comma and extract values
                    values = line.split(',')
                    # Ensure there are at least three values
                    if len(values) >= 3:
                        # Create a tuple from the first two values also, converting the protocol value in lowercase
                        key_tuple = (values[0].strip(), values[1].strip().lower())
                        # Create a tuple for the last value in lowercase and original case
                        
                        last_value = values[2].strip()
                        value_tuple = (last_value.lower(), last_value)
                        
                        # Add to the dictionary
                        tag_data[key_tuple] = value_tuple
                    else:
                        print(f"Warning: Line skipped due to insufficient values: '{line}'")

        # Print the result to check
        for key, value in tag_data.items():
            print(f"    {key} : {value},")
        
        return tag_data

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
