import re

def format_contributor(contrib):
    """
    Helper function to format the contributor details properly.
    Replaces common formatting errors with a standardized format.
    """
    name_str = 'Name: ['
    contrib = contrib.replace('：', ':')  # Handle colon variations
    contrib = contrib.replace('htpps', 'https')  # Fix common typo in URLs
    contrib = contrib.replace('Name:[', name_str)
    contrib = contrib.replace('Name : [', name_str)
    contrib = contrib.replace('Name :[', name_str)
    contrib = contrib.replace('Name: [ ', name_str)
    # Prepend heading and add double newlines
    contrib = '#### ' + contrib + '\n\n'
    return contrib

# Read the file and normalize the headings
with open('CONTRIBUTORS.md', 'r+') as file:
    new_file_data = []
    for line in file.readlines():
        # Replace all headings (up to ###) with ####
        line = re.sub('^#{1,3} ', '#### ', line)
        # Remove leading whitespaces from lines starting with "##"
        if line.startswith(' ##'):
            new_file_data.append(line.lstrip())
        else:
            new_file_data.append(line)
    
    # Rewrite the file with the cleaned-up content
    file.seek(0)
    file.truncate()
    file.writelines(new_file_data)

# Sorting contributors and saving them back to the file
with open('CONTRIBUTORS.md', 'r+') as file:
    # Split contributors by '####', clean up, and reformat
    contributors = [contributor.strip() for contributor in file.read().split('####') if contributor]
    contributors = [format_contributor(contrib) for contrib in contributors]
    # Sort contributors alphabetically
    contributors = sorted(contributors)
    
    # Write the sorted contributors back to the file
    file.seek(0)
    file.truncate()
    file.writelines(contributors)

