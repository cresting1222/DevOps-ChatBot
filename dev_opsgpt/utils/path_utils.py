import os
from langchain.document_loaders import CSVLoader, PyPDFLoader, UnstructuredFileLoader
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from configs.model_config import (
    embedding_model_dict,
    KB_ROOT_PATH,
)


LOADERNAME2LOADER_DICT = {
    "UnstructuredFileLoader": UnstructuredFileLoader,
    "CSVLoader": CSVLoader,
    "PyPDFLoader": PyPDFLoader
}
LOADER2EXT_DICT = {"UnstructuredFileLoader": ['.eml', '.html', '.json', '.md', '.msg', '.rst',
                                          '.rtf', '.txt', '.xml',
                                          '.doc', '.docx', '.epub', '.odt', 
                                          '.ppt', '.pptx', '.tsv'],
               "CSVLoader": [".csv"],
               "PyPDFLoader": [".pdf"],
               }

EXT2LOADER_DICT = {ext: LOADERNAME2LOADER_DICT[k] for k, exts in LOADER2EXT_DICT.items() for ext in exts}

SUPPORTED_EXTS = [ext for sublist in LOADER2EXT_DICT.values() for ext in sublist]


def validate_kb_name(knowledge_base_id: str) -> bool:
    # 检查是否包含预期外的字符或路径攻击关键字
    if "../" in knowledge_base_id:
        return False
    return True

def get_kb_path(knowledge_base_name: str):
    return os.path.join(KB_ROOT_PATH, knowledge_base_name)

def get_doc_path(knowledge_base_name: str):
    return os.path.join(get_kb_path(knowledge_base_name), "content")

def get_vs_path(knowledge_base_name: str):
    return os.path.join(get_kb_path(knowledge_base_name), "vector_store")

def get_file_path(knowledge_base_name: str, doc_name: str):
    return os.path.join(get_doc_path(knowledge_base_name), doc_name)

def list_kbs_from_folder():
    return [f for f in os.listdir(KB_ROOT_PATH)
            if os.path.isdir(os.path.join(KB_ROOT_PATH, f))]

def list_docs_from_folder(kb_name: str):
    doc_path = get_doc_path(kb_name)
    return [file for file in os.listdir(doc_path)
            if os.path.isfile(os.path.join(doc_path, file))]

def get_LoaderClass(file_extension):
    for LoaderClass, extensions in LOADER2EXT_DICT.items():
        if file_extension in extensions:
            return LoaderClass