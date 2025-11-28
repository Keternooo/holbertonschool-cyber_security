#!/usr/bin/env python3
"""
A script to find and replace a string in the heap memory of a running process.

Usage:
    ./read_write_heap.py pid search_string replace_string

Arguments:
    pid: The process ID to inspect.
    search_string: The string to search for in the heap.
    replace_string: The string to replace it with.
"""

import os
import sys
import signal

def usage():
    print("Usage: ./read_write_heap.py pid search_string replace_string")
    sys.exit(1)

def read_write_heap(pid, search_string, replace_string):
    try:
        pid = int(pid)
    except ValueError:
        print("PID must be an integer.")
        usage()

    maps_path = f"/proc/{pid}/maps"
    mem_path = f"/proc/{pid}/mem"

    try:
        with open(maps_path, "r") as maps_file:
            heap_start = heap_end = None
            for line in maps_file:
                if "[heap]" in line:
                    addr = line.split()[0]
                    heap_start, heap_end = [int(x, 16) for x in addr.split("-")]
                    break

        if heap_start is None:
            print("Error: heap segment not found.")
            sys.exit(1)

    except FileNotFoundError:
        print("Process not found.")
        sys.exit(1)

    search_bytes = search_string.encode()
    replace_bytes = replace_string.encode()

    if len(replace_bytes) > len(search_bytes):
        print("Replacement string cannot be longer than search string.")
        sys.exit(1)

    os.kill(pid, signal.SIGSTOP)

    try:
        with open(mem_path, "r+b") as mem:
            mem.seek(heap_start)
            heap_data = mem.read(heap_end - heap_start)

            offset = heap_data.find(search_bytes)
            if offset == -1:
                print("String not found in heap.")
                os.kill(pid, signal.SIGCONT)
                sys.exit(1)

            mem.seek(heap_start + offset)
            mem.write(replace_bytes.ljust(len(search_bytes), b'\x00'))

            print(f"Successfully replaced '{search_string}' with '{replace_string}'.")

    except PermissionError:
        print("Permission denied. Try using sudo.")
    except Exception as e:
        print("Unexpected error:", e)

    finally:
        os.kill(pid, signal.SIGCONT)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage()

    read_write_heap(sys.argv[1], sys.argv[2], sys.argv[3])
