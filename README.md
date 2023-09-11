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

## Database structure

The MongoDB database is assumed to have data with the following structure:

#### users

```json
{
  "_id": {
    "$oid": "64fae3f706a5f0554f808dc8"
  },
  "name": "Bob",
  "age": "40-50",
  "email": "bob3@gmail.com",
  "gender": "male",
  "interest": [
    "basketball",
    "travelling",
    "music",
    "cooking"
  ],
  "industry": "sports",
  "purchases": [
    "64fadb4406a5f0554f808dbc"
  ]
}
```

#### products

```json
{
  "_id": {
    "$oid": "64faca6c06a5f0554f808db8"
  },
  "name": "MacBook Pro 13",
  "price": 129900,
  "desc": "Chip: Apple M2 chip\n8-core CPU with 4 performance cores and 4 efficiency cores\n10-core GPU\n16-core Neural Engine\n100GB/s memory bandwidth\nDisplay: Retina display\n33.74 cm / 13.3-inch (diagonal) LED-backlit display with IPS technology\n2560x1600 native resolution at 227 pixels per inch with support for millions of colours\n500 nits brightness\nBattery and Power:Up to 20 hours Apple TV app movie playback\nUp to 17 hours wireless web\nMemory: 8GB unified memory (Configurable to: 16GB or 24GB)\nStorage:256GB SSD (Configurable to: 512GB, 1TB or 2TB)\nOr, 512GB SSD (Configurable to: 1TB or 2TB)\nCharging and Expansion: Two Thunderbolt / USB 4 ports with support for Charging, DisplayPort, Thunderbolt 3 (up to 40 Gbps), \nUSB 4 (up to 40Gbps), USB 3.1 Gen 2 (up to 10 Gbps), and a headphone jack.\nWireless: Wi-Fi (802.11ax Wi-Fi 6 wireless networking IEEE) and Bluetooth (Bluetooth 5.0 wireless technology)\nCamera: A built-in FaceTime HD camera\n"
}
```

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
