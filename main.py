from typing import List, Dict, Tuple

import core_logic
from input_logic import capture_flow_log_data, capture_tag_data
from output_logic import output_tag_count, output_port_protocol_combination

def main() -> None:
    """Main function to orchestrate the data processing pipeline.

    1. Captures flow log data.
    2. Captures tag data.
    3. Processes logs and counts tags using `core_logic`.
    4. Outputs tag counts and port/protocol combinations.
    """
    
    flow_logs = capture_flow_log_data()
    tags = capture_tag_data()
    tag_counts, port_protocol_counts = core_logic.process_logs_and_count_tags(flow_logs, tags)

    print("---------------------final output to (.txt) file-----------------------")
    output_tag_count(tag_counts)
    output_port_protocol_combination(port_protocol_counts)
    
    
    
if __name__ == "__main__":
    main()
