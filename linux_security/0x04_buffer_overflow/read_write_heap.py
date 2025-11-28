#!/usr/bin/python3
"""
Doc for the script:
Find and replace a string inside the heap of a running process.
"""

import sys


def usage():
    """Documentation:
    Display usage and exit.
    """
    print("Usage: read_write_heap.py pid search_string replace_string")
    sys.exit(1)


def main():
    """Documentation:
    Main logic for reading and writing process heap.
    """
    if len(sys.argv) != 4:
        usage()

    try:
        pid = int(sys.argv[1])
    except Exception:
        usage()

    search = sys.argv[2].encode()
    replace = sys.argv[3].encode()

    maps_path = f"/proc/{pid}/maps"
    mem_path = f"/proc/{pid}/mem"

    try:
        with open(maps_path, "r") as maps_file:
            heap_start = heap_end = None

            for line in maps_file:
                if "[heap]" in line:
                    addr, perms = line.split()[0], line.split()[1]
                    if "rw" not in perms:
                        continue
                    heap_start, heap_end = [int(x, 16) for x in addr.split("-")]
                    break

        if heap_start is None:
            print("Error: Heap not found")
            sys.exit(1)

        with open(mem_path, "r+b") as mem:
            mem.seek(heap_start)
            heap = mem.read(heap_end - heap_start)

            index = heap.find(search)
            if index == -1:
                print("Error: String not found in heap")
                sys.exit(1)

            mem.seek(heap_start + index)
            mem.write(replace.ljust(len(search), b"\x00"))

            print(f"Replaced '{search.decode()}' with '{replace.decode()}'")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
