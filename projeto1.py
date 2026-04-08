import PyPDF2
import os

merger = PyPDF2.PdfMerger()

file_list = os.listdir("file")
file_list.sort()
print(file_list)


for file in file_list:
    if ".pdf" in file:
        merger.append(f"file/{file}")

merger.write("Final PDF.pdf")