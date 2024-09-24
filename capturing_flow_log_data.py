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


def extract_necessary_data(logs):
    """
    Extracts necessary data from the flow log entries.

    Parameters:
    logs (list): A list of lists containing the flow log data.

    Returns:
    list: A list of lists containing the necessary data.
    """
    return [[entry[6], entry[7]] for entry in logs if len(entry) > 7]
