#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

def print_stats(accumulated_size, code_tally):
    """Print accumulated metrics.

    Args:
        accumulated_size (int): The accumulated read file size.
        code_tally (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(accumulated_size))
    for code in sorted(code_tally):
        print("{}: {}".format(code, code_tally[code]))

if __name__ == "__main__":
    import sys

    total_bytes = 0
    status_code_count = {}
    known_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_stats(total_bytes, status_code_count)
                line_count = 1
            else:
                line_count += 1

            parts = line.split()

            try:
                total_bytes += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if parts[-2] in known_codes:
                    if parts[-2] not in status_code_count:
                        status_code_count[parts[-2]] = 1
                    else:
                        status_code_count[parts[-2]] += 1
            except IndexError:
                pass

        print_stats(total_bytes, status_code_count)

    except KeyboardInterrupt:
        print_stats(total_bytes, status_code_count)
        raise

