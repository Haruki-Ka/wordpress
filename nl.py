import sys

def nl(input_file=None):
    try:
        if input_file:
            with open(input_file, 'r') as f:
                lines = f.readlines()
        else:
            lines = sys.stdin.readlines()
        
        for i, line in enumerate(lines, 1):
            print(f"{i:6}  {line}", end='')
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        nl(sys.argv[1])
    else:
        nl()
