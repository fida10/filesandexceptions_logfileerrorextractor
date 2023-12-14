""" 
Practice Question 6: Log File Error Extractor

Task:
Create a function extract_errors that reads a log file and extracts lines 
that contain the word 'ERROR'. The function should return a list of these lines. 
Handle any file reading exceptions gracefully.
"""

def extract_errors(log_file):
    print(f'Log file: {log_file}')
    log_file_as_lines = open(log_file, 'r').readlines()
    errors = []
    for line in log_file_as_lines:
        if 'ERROR' in line:
            errors.append(line.strip())

    return errors