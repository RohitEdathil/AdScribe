from models.user import User
from models.prompt import Prompt
from repo.vector import VectorRepository
from langchain.chains import RetrievalQA
from langchain.embeddings.base import Embeddings
from langchain.llms.base import BaseLLM


class Generator:
    def __init__(self, vector_repo: VectorRepository, llm: BaseLLM):
        self.vector_repo = vector_repo
        self.embeddings = vector_repo.embedding
        self.qa = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_repo.vectorstore.as_retriever(),
        )

    def generate(self, user: User) -> str:
        prompt = str(Prompt(user))
        answer = self.qa.run(prompt)
        return answer
