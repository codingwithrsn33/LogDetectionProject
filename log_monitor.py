import json

# Load rules
with open("rules.json", "r") as rule_file:
    rules = json.load(rule_file)

# HTML report: header with style and search
html_header = """
<html>
<head>
    <title>Suspicious Activity Report</title>
    <style>
        body { font-family: Arial; margin: 20px; }
        input[type="text"] { width: 300px; padding: 8px; margin-bottom: 10px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        tr:hover { background-color: #f5f5f5; }
    </style>
    <script>
        function searchLogs() {
            var input = document.getElementById("searchInput");
            var filter = input.value.toLowerCase();
            var rows = document.getElementsByClassName("logRow");

            for (var i = 0; i < rows.length; i++) {
                var line = rows[i].getElementsByTagName("td")[0];
                var reason = rows[i].getElementsByTagName("td")[1];
                if (line && reason) {
                    var text = line.textContent + " " + reason.textContent;
                    rows[i].style.display = text.toLowerCase().includes(filter) ? "" : "none";
                }
            }
        }
    </script>
</head>
<body>
    <h2>Suspicious Activity Report</h2>
    <input type="text" id="searchInput" onkeyup="searchLogs()" placeholder="Search logs...">
    <p><strong>Total Suspicious Logs:</strong> {count}</p>
    <table>
        <tr><th>Log Line</th><th>Reason</th></tr>
"""

html_footer = """
    </table>
</body>
</html>
"""

# Process logs and generate outputs
with open("logs.txt", "r") as log_file, \
     open("suspicious_logs.txt", "w") as out_file, \
     open("report.html", "w") as html_file:

    rows = []
    count = 0

    for line in log_file:
        for rule in rules:
            if rule["keyword"].lower() in line.lower():
                description = rule["description"]
                log_clean = line.strip()

                # Write to suspicious_logs.txt
                out_file.write(log_clean + "  <-- " + description + "\n")

                # Write HTML row with class="logRow"
                row = f"<tr class='logRow'><td>{log_clean}</td><td>{description}</td></tr>\n"
                rows.append(row)
                count += 1
                break

    # Inject total count and write HTML
    html_file.write(f"{html_header.replace('{count}', str(count))}")
    html_file.writelines(rows)
    html_file.write(html_footer)

print("✅ Suspicious report generated: suspicious_logs.txt and report.html")
