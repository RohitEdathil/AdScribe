from .vector import VectorRepository
import pinecone
from os import environ
from langchain.embeddings.base import Embeddings


class PineconeRepository(VectorRepository):
    def __init__(self, embedding: Embeddings):
        super().__init__(embedding)
        api_key = environ["PINECONE_API_KEY"]
        env = environ["PINECONE_ENV"]
        index = environ["PINECONE_INDEX"]

        if api_key is None or env is None or index is None:
            raise Exception(
                "PINECONE_API_KEY, PINECONE_ENV, and PINECONE_INDEX must be set in the environment"
            )

        pinecone.init(
            api_key=api_key,
            environment=env,
        )
        self.index = pinecone.Index(index)

    def ingest(self, product):
        vector = [
            (product.id, values)
            for values in self.embedding.embed_documents([str(product)])
        ]
        self.index.upsert(vectors=vector)
