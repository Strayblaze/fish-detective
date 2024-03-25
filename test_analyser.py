# test_analyser.py
import sys
import os

# Append the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Now import the module

from analyser import scan_file

def test_scan_file():
    # Replace 'your_api_key_here' with your actual VirusTotal API key
    api_key = 'b23e2e4e2f42a8faf14c41bbc823fa1949cbd8cefe19fae94ad3cd1bcd26c8ef'
    file_path = 'something.txt'  # This file should exist and be accessible

    # Test the function with a valid file
    report = scan_file(api_key, file_path)
    assert report is not None
    assert 'data' in report
    assert 'attributes' in report['data']
    assert 'last_analysis_stats' in report['data']['attributes']

    # Test the function with an invalid file path
    invalid_file_path = 'non_existent_file.txt'
    report = scan_file(api_key, invalid_file_path)
    assert report is None

    # Test the function with invalid API key
    invalid_api_key = 'invalid_api_key'
    report = scan_file(invalid_api_key, file_path)
    assert report is None
