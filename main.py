import core_logic
from capturing_flow_log_data import capture_flow_log_data
from capturing_tag_data import capture_tag_data

def main():
    list_of_logs_obtained = capture_flow_log_data()
    dictionary_containing_tags = capture_tag_data()
    tags_output, protocols_output = core_logic.process_logs_and_count_tags(list_of_logs_obtained, dictionary_containing_tags, tag_mappings)
    
    print("---------------------final_Print-----------------------")
    print(tags_output)
    print(protocols_output)
    
main()