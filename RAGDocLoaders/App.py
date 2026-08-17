from langchain_community.document_loaders import WebBaseLoader

data=WebBaseLoader("https://www.policybazaar.com/?utm_source=affinity&utm_medium=native&utm_campaign=home3_siteplug")

docs=data.load()
print(docs)