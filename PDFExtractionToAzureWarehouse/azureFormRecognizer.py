from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from pathlib import Path

endpoint = "https://dataextractionpdf.cognitiveservices.azure.com/"
key = "CognitiveServiceKey"

client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

with open("Sample.pdf", "rb") as f:
    poller = client.begin_analyze_document("prebuilt-receipt", document=f)
    result = poller.result()

'''
for page in result.pages:
    for line in page.lines:
        print(line.content)
'''

for page_num, page in enumerate(result.pages, start=1):
    print(f"\n--- Page {page_num} ---")
    for table_idx, table in enumerate(result.tables):
        print(f"\nTable {table_idx + 1}:")
        for row_idx, row in enumerate(table.cells):
            if row.row_index == 0:
                print("\nHeader:")
            if row.column_index == 0:
                print()  # New line for each row
            print(f"{row.content}", end="\t")

