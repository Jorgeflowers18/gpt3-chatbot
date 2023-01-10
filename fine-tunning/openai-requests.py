import os
import openai
openai.api_key = "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"
#openai.api_key = os.getenv("OPENAI_API_KEY")
l1 = openai.Model.list()
print(l1)
for i in l1:
    print(i) 
