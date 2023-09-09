from repo.mongo import MongoRepository
from repo.pinecone import PineconeRepository
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
from langchain.llms import OpenAI, LlamaCpp
from tqdm import tqdm
from generator.generator import Generator
from delivery.mail_delivery import MailDelivery
from os import getenv

if getenv("LLM") == "openapi":
    embedding = OpenAIEmbeddings()
    llm = OpenAI()
else:
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )
    llm = LlamaCpp(
        model_path="./model.bin",
        temperature=0.1,
        n_gpu_layers=43,
        n_ctx=3900,
    )


business_repo = MongoRepository()
vector_repo = PineconeRepository(embedding=embedding)
delivery = MailDelivery()

generator = Generator(vector_repo=vector_repo, llm=llm)

users = business_repo.get_users()
for user in tqdm(users, total=len(users), desc="Generating emails"):
    content = generator.generate(user)
    delivery.deliver(user, content)
print("Done!")
