from constants import PROTOCOL_MAPPINGS


# def protocol_to_tags_converter(list_of_logs_obtained: list[list[str]]): 
#     for entry in list_of_logs_obtained:
#         protocol_obtained = PROTOCOL_MAPPINGS.get(entry[1], None)
#         entry[1] = protocol_obtained
    
#     list_of_tuples = [tuple(l) for l in list_of_logs_obtained]
#     print(list_of_tuples)
#     return list_of_tuples

# def tuples_counter(list_of_tuples, tags_obtained):
#     tags_output = {}
#     protocols_output = {}
#     for entry in list_of_tuples:
#         # Handling protocols_output
#         if entry not in protocols_output:
#             protocols_output[entry] = 0
#         protocols_output[entry] += 1
        
#         # Handling tags_output
#         tuple_containing_tag_entry = tags_obtained.get(entry, None)
#         if tuple_containing_tag_entry:
#             list_containing_tags = tags_obtained[entry]
#             if list_containing_tags[0] not in tags_output:
#                 tags_output[list_containing_tags[0]] = 0
#             tags_output[list_containing_tags[0]] += 1
#         else:
#             if "Untagged" not in tags_output:
#                 tags_output["Untagged"] = 0
#             tags_output["Untagged"] += 1 
    
#     print("Tags Output:", tags_output)
#     print("Protocols Output:", protocols_output)
    
    
def process_logs_and_count_tags(list_of_logs_obtained: dict, tags_obtained:dict) -> tuple[dict, dict] :
    """
    Converts protocol identifiers in the log entries to their respective tags and counts occurrences of each tag and protocol.

    Parameters:
    list_of_logs_obtained (list): A list of logs where each log is a list of strings.
    tags_obtained (dict): A dictionary mapping log entries to their respective tags.

    Returns:
    tuple: A tuple containing two dictionaries: tags_output and protocols_output.
    """
    # Initialize output dictionaries
    tags_output = {}
    protocols_output = {}
    
    # Process each log entry to convert protocols
    for entry in list_of_logs_obtained:
        # Convert protocol using the mapping
        protocol_obtained = PROTOCOL_MAPPINGS.get(entry[1], None)
        entry[1] = protocol_obtained
        
        # Create a tuple from the updated entry
        entry_tuple = tuple(entry)
        
        # Count occurrences in protocols_output
        if entry_tuple not in protocols_output:
            protocols_output[entry_tuple] = 0
        protocols_output[entry_tuple] += 1
        
        # Count occurrences in tags_output
        tuple_containing_tag_entry = tags_obtained.get(entry_tuple, None)
        if tuple_containing_tag_entry:
            list_containing_tags = tags_obtained[entry_tuple]
            if list_containing_tags[0] not in tags_output:
                tags_output[list_containing_tags[0]] = 0
            tags_output[list_containing_tags[0]] += 1
        else:
            if "Untagged" not in tags_output:
                tags_output["Untagged"] = 0
            tags_output["Untagged"] += 1 
    
    print("Tags Output:", tags_output)
    print("Protocols Output:", protocols_output)
    
    return tags_output, protocols_output
