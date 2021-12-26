from bs4 import BeautifulSoup
import re

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
    
tags = doc.find_all("input", type="text")
for tag in tags:
    tag['placeholder'] = "Changed"
with open("index2.html", "w") as file:
    file.write(str(doc))

        