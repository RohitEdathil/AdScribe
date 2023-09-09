# AdScribe

A system to generate personalized marketing content using LLM.

## Modes

The system is designed to run in two modes which can be switched using `LLM` environment variable.

| Mode     | Embedding          | LLM          |
| -------- | ------------------ | ------------ |
| `openai` | `OpenAIEmbeddings` | `GPT`        |
| `other`  | `mpnet-base-v2`    | `Llama2-13B` |

## Installation

### Clone the repository

```bash
git clone https://github.com/RohitEdathil/AdScribe.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Additional dependencies for `other` mode

```bash
CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python
pip install sentence-transformers

```

**Note:** `llama-cpp-python` is installed with `CUDA` support by default. If you want to install without `CUDA` support, remove `CMAKE_ARGS="-DLLAMA_CUBLAS=on"` from the above command.

Download the Llama2 binary using:

```bash
wget https://huggingface.co/TheBloke/Firefly-Llama2-13B-v1.2-GGUF/resolve/main/firefly-llama2-13b-v1.2.Q2_K.gguf -O model.bin
```

## Environment variables

## General

| Variable | Description                                             |
| -------- | ------------------------------------------------------- |
| `LLM`    | `openai` or `other`, to set the mode as mentioned above |

## Pinecone

| Variable           | Description                      |
| ------------------ | -------------------------------- |
| `PINECONE_API_KEY` | API key for Pinecone             |
| `PINECONE_INDEX`   | Name of the Pinecone index       |
| `PINECONE_ENV`     | Name of the Pinecone environment |

### OpenAI

| Variable         | Description        |
| ---------------- | ------------------ |
| `OPENAI_API_KEY` | API key for OpenAI |

### MongoDB

| Variable    | Description     |
| ----------- | --------------- |
| `MONGO_URI` | URI for MongoDB |

## SMTP

| Variable        | Description          |
| --------------- | -------------------- |
| `SMTP_HOST`     | SMTP server host     |
| `SMTP_EMAIL`    | Sender email address |
| `SMTP_PASSWORD` | Sender password      |

## Usage

This system has two jobs:

### Ingest

Fetches product data from a general purpose database, converts it into text embeddings and stores it in a vector database.

```bash
python ingest.py
```

### Generate

Fetches user data from a general purpose database, fetches matching product embeddings from the vector database, generates personalized content and sends it to the user.

```bash
python generate.py
```

## Customization

### Prompt

The prompt template for generating personalized content is stored in `templates/prompt.template.txt`. This template is rendered using the user data fetched from the database and then used to fetch matching product embeddings from the vector database. Playing around with this template can help generate better personalized content and to adopt the tool for other use cases.

### Ingest

The file `templates/product.template.txt` contains the template for product description. This template is rendered using the product data fetched from the database and then embedded into the vector database.

### Generate

The file `templates/user.template.txt` contains the template for user description. This template is rendered using the user data fetched from the database and then used to fetch matching product embeddings from the vector database. The product embeddings are then used to generate personalized content.

## Extending

Currently the general classes have the following concrete implementations:

- `BusinessRepository`: `MongoRepository`
- `VectorRepository`: `PineconeRepository`
- `Delivery` : `MailDelivery`

The base classes can be extended to support other databases and delivery paradigms.
