#!/usr/bin/env python3
"""
Usage: read_write_heap.py pid search_string replace_string
Find and replace a string in the heap of a running process.
"""

import sys

def usage():
    print("Usage: read_write_heap.py pid search_string replace_string")
    sys.exit(1)

if len(sys.argv) != 4:
    usage()

pid = sys.argv[1]
search = sys.argv[2].encode()
replace = sys.argv[3].encode()

try:
    pid = int(pid)
except Exception:
    usage()

if len(replace) > len(search):
    print("Error: replace_string longer than search_string")
    sys.exit(1)

maps_path = f"/proc/{pid}/maps"
mem_path = f"/proc/{pid}/mem"

try:
    with open(maps_path, "r") as f:
        heap_start = heap_end = None
        for line in f:
            if "[heap]" in line:
                addr = line.split()[0]
                heap_start, heap_end = [int(x, 16) for x in addr.split("-")]
                break

    if heap_start is None:
        print("Error: heap not found")
        sys.exit(1)

    with open(mem_path, "r+b") as mem:
        mem.seek(heap_start)
        heap = mem.read(heap_end - heap_start)

        idx = heap.find(search)
        if idx == -1:
            print("Error: search_string not found")
            sys.exit(1)

        mem.seek(heap_start + idx)
        mem.write(replace.ljust(len(search), b"\x00"))

        print(f"Replaced '{search.decode()}' with '{replace.decode()}'")

except Exception:
    print("Error: cannot access process memory")
    sys.exit(1)
