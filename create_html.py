import os
from html import escape

def create_html(all_job_postings):
    with open((os.path.dirname(os.path.abspath(__file__))) + "/html/job_postings.html", "w", encoding="utf-8") as file:

        file.write('<!DOCTYPE html>')          

        file.write('<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n')

        file.write('<link href="https://fonts.googleapis.com/css2?family=Love+Ya+Like+A+Sister&family=Open+Sans:ital,wght@0,300;0,400;0,700;1,400&display=swap" rel="stylesheet">\n')

        file.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Job Postings</title>\n<link rel="stylesheet" href="../css/normalize.css">\n<link rel="stylesheet" href="../css/styles.css"></head>\n<body>\n')
        
        file.write('<script src="../js/modernizr.js"></script>\n')

        file.write('<div class="container">\n<header class="main">')
		
        file.write("<h1>DARBO SKELBIMAI</h1>\n")

        file.write("<ul>\n")
        for posting in all_job_postings:
            for title, link in posting.items():
                file.write(f"<li><a href='{link}'>{escape(title)}</a></li>\n")
        file.write("</ul>\n")

        file.write('</header>\n</div>\n')

        file.write("</body>\n</html>")
