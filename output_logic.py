from typing import Dict, Tuple

def output_tag_count(tag_counts: Dict[str, int]) -> None:
    """Writes tag counts to a text file.

    Args:
        tag_counts: A dictionary containing tag counts.
    """
    file_name = input("Enter output file name for tag count file-> ").strip() or 'tag_count_OUTPUT.txt'

    with open(file_name, 'w') as file:
        for tag, count in tag_counts.items():
            file.write(f"{tag}, {count}\n")

    print(f"The tag count file is written as output in the .txt file with name -> {file_name}")


def output_port_protocol_combination(port_protocol_counts: Dict[Tuple[str, str], int]) -> None:
    """Writes port/protocol counts to a text file.

    Args:
        port_protocol_counts: A dictionary containing port/protocol counts.
    """
    file_name = input("Enter output file name for port/protocol count file-> ").strip() or 'port-protocol_count_OUTPUT.txt'

    with open(file_name, 'w') as file:
        for (port, protocol), count in port_protocol_counts.items():
            file.write(f"{port}, {protocol}, {count}\n")

    print(f"The port/protocol count file is written as output in the .txt file with name -> {file_name}")