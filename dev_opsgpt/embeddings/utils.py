from functools import lru_cache
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from configs.model_config import embedding_model_dict


@lru_cache(1)
def load_embeddings(model: str, device: str):
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model_dict[model],
                                       model_kwargs={'device': device})
    return embeddings