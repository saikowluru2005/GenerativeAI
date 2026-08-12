from langchain_community.document_loaders import TextLoader

data=TextLoader("Sample.txt")

docs=data.load()
print(docs)