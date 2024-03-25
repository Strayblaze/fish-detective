import requests
import time

def check_file_with_virustotal(api_key, file_path):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': api_key}
    
    try:
        with open(file_path, 'rb') as file:
            files = {'file': (file_path, file)}
            response = requests.post(url, files=files, params=params)
            if response.status_code == 200:
                json_response = response.json()
                scan_id = json_response.get('scan_id')
                if scan_id:
                    print("File successfully uploaded to VirusTotal.")
                    print("Waiting for scan results...")
                    time.sleep(200)  # Wait for a few seconds before checking the report
                    report_url = f'https://www.virustotal.com/vtapi/v2/file/report'
                    report_params = {'apikey': api_key, 'resource': scan_id}
                    report_response = requests.get(report_url, params=report_params)
                    if report_response.status_code == 200:
                        report_text = report_response.text
                        print("Scan report:")
                        print(report_text)
                        if '"detected":true' in report_text:
                            print("The file is malicious.")
                        else:
                            print("The file is clean.")
                    else:
                        print("Failed to fetch the report.")
                else:
                    print("Failed to obtain scan ID from the response.")
            else:
                print("Failed to upload the file to VirusTotal.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
api_key = 'b23e2e4e2f42a8faf14c41bbc823fa1949cbd8cefe19fae94ad3cd1bcd26c8ef'
file_path = 'C:\\Users\\windows.bat'
check_file_with_virustotal(api_key, file_path)