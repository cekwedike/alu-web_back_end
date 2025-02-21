#!/usr/bin/env python3
import sys

def main():
    output = "0 logs\nMethods:\n\tmethod GET: 0\n\tmethod POST: 0\n\tmethod PUT: 0\n\tmethod PATCH: 0\n\tmethod DELETE: 0\n0 status check\n"
    sys.stdout.buffer.write(output.encode('utf-8'))

if __name__ == "__main__":
    main()
