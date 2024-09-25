import core_logic
from input_logic import capture_flow_log_data, capture_tag_data
from output_logic import output_tag_count, output_port_protocol_combination

def main():
    list_of_logs_obtained = capture_flow_log_data()
    dictionary_containing_tags = capture_tag_data()
    tags_output, protocols_output = core_logic.process_logs_and_count_tags(list_of_logs_obtained, dictionary_containing_tags)
    print("---------------------final output to (.txt) file-----------------------")
    output_tag_count(tags_output)
    output_port_protocol_combination(protocols_output)
    
    
    
main()
