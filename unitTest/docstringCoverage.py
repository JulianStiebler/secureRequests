import subprocess
import re
import sys

def get_docstring_coverage(directory):
    # Run the docstr-coverage command
    result = subprocess.run(['docstr-coverage', directory], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = result.stdout.decode('utf-8')
    
    # Print the entire output for debugging
    print("Command output:")
    print(output)
    
    # Extract the coverage percentage using regex
    match = re.search(r'Total coverage: ([\d.]+)%', output)
    if match:
        coverage = match.group(1)
    else:
        print("Failed to match regex pattern.")
        coverage = '0'
    
    return coverage

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python docstringCoverage.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    coverage = get_docstring_coverage(directory)
    print("Extracted coverage:")
    print(coverage)
