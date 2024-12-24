import webbrowser
from datetime import datetime

# Get the current time when the script runs
current_time = datetime.now().strftime("%H:%M:%S")

# Create HTML content with a button linking to 'time_page.html'
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Time Page</title>
</head>
<body>
    <h1>Welcome! Click the button to view the time page.</h1>
    <p>This page contains a button that links to a separate page showing the time when it was generated.</p>
    
    <!-- Button that links to time_page.html -->
    <button onclick="window.location.href='time_page.html'">Go to Time Page</button>
    
</body>
</html>
"""

# Write the HTML to a file
file_name = "time_page2.html"
with open(file_name, "w") as file:
    file.write(html_content)

# Automatically open the file in a browser
webbrowser.open(file_name)

print(f"HTML file '{file_name}' created. Open it in your browser to see the button.")

