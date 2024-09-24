def output_tag_count(dictionary_containing_tag_counts: dict):
    # Specify the file name
    file_name = input("Enter output file name for tag count file-> ").strip() or 'tag_count_output.txt'
    
    # Write the dictionary to the text file
    with open(file_name, 'w') as file:
        for key, value in dictionary_containing_tag_counts.items():
            file.write(f"{key}, {value}\n")
    print(f"The tag count file is written as output in the .txt file with name -> {file_name}")
            
            
def output_port_protocol_combination(dictionary_with_port_protocol_count: dict):
    file_name = input("Enter output file name for port/protocol count file-> ").strip() or 'port/protocol_count_output.txt'
    
    # Write the dictionary to the text file
    with open(file_name, 'w') as file:
        for key, value in dictionary_with_port_protocol_count.items():
            file.write(f"{key[0]},{key[1]},{value}\n")
    print(f"The port/protocol count file is written as output in the .txt file with name -> {file_name}")