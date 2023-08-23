import re
import json

# Read HTML content from the file
html_file_path = "Audit_report.html"  # Update with the actual path of your HTML file
with open(html_file_path, "r", encoding="utf-8") as html_file:
    html_content = html_file.read()

# Define regular expression patterns for extracting Info, Solution, and Hosts
info_pattern = r'<div class="details-header">Info.*?<div style="line-height: 20px; padding: 0 0 20px 0; overflow-wrap: break-word">(.*?)</div>'
solution_pattern = r'<div class="details-header">Solution.*?<div style="line-height: 20px; padding: 0 0 20px 0; overflow-wrap: break-word">(.*?)</div>'
hosts_pattern = r'<div class="details-header">Hosts.*?<h2>(.*?)</h2>'

# Find all matches in the HTML content
info_matches = re.findall(info_pattern, html_content, re.DOTALL)
solution_matches = re.findall(solution_pattern, html_content, re.DOTALL)
hosts_matches = re.findall(hosts_pattern, html_content, re.DOTALL)

# Remove HTML tags and extra whitespace
def remove_html_tags(text):
    clean_text = re.sub(r'<.*?>', '', text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    return clean_text

# Create a list to store the results
results = []

# Iterate through matches and populate the results list
for i in range(len(info_matches)):
    try:
        info_text = remove_html_tags(info_matches[i])
        solution_text = remove_html_tags(solution_matches[i])
        hosts_h2 = remove_html_tags(hosts_matches[i])
        
        result = {
            "Info": info_text,
            "Solution": solution_text,
            "Hosts": hosts_h2
        }
        results.append(result)
    except IndexError:
        pass  # Handle the IndexError by skipping this iteration

# Save results in a JSON file
output_file_path = "extracted_results.json"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    json.dump(results, output_file, indent=4)

print(f"Results have been saved to {output_file_path}")
