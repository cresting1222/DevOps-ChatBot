

# <p align="center">DevOps-ChatBot</p>

<p align="center">
    <a href="README_en.md"><img src="https://img.shields.io/badge/document-英文版-white.svg" alt="EN doc"></a>
    <a href="README.md"><img src="https://img.shields.io/badge/文档-中文版-white.svg" alt="ZH doc"></a>
    <img src="https://img.shields.io/static/v1?label=license&message=MIT&color=white&style=flat" alt="License">
</p>


# News
- [2023.09.15] ...

<br>
<br>
<br>


# Introduction

💡 This project is inspired by the langchain-chatchat project and code interpreter, aiming to build an operations-oriented conversational AI using RAG, tool learning, and an independent sandbox environment, so that operations personnel can perform tasks without the need for development.


🤖️ DevOps-ChatBot is a plug-and-play application deployment designed for scenarios such as private deployment. It replaces traditional operations and maintenance Q&A websites like Stack Overflow by providing personalized documentation or open-source question-and-answer resources in the operations domain. The goal is to change the habit of troubleshooting by gradually shifting from searching various references to utilizing a large-scale model for question answering.

- Quickly retrieve technical documentation for open-source projects.
- Provide accurate and executable code examples.
- Support the automatic execution of toolchain workflows.


✅ 依托于开源的 LLM 与 Embedding 模型，本项目可实现全部使用开源模型离线私有部署。与此同时，本项目也支持 OpenAI GPT API 的调用。


# Usage Example
- Incorporate an independent sandbox environment.
- Provide code editing capabilities.

![devopsgpt_example](sources/docs_imgs/devopsgpt_example.png)

![Alt text](sources/docs_imgs/devopsgpt_example2.png)

# Tech RoadMap

![roadmap](sources/docs_imgs/roadmap.png)

from bottom to up

- Web Crawl: Regularly crawl web documents to ensure data timeliness (dependent on open-source continuous updates).
- Data Process: Clean, deduplicate, and categorize data from different crawling sources, while also supporting private document imports.
- Vector Database: Utilize Text Embedding models to obtain document embeddings and store them (using Milvus).
- Schedule Core: Responsible for the interaction and scheduling of components such as LLM (Language Model), Vector Database, etc. (using Langchain).
- Prompt Control: Categorize different types of questions from a developer and operations perspective, add prompt context to ensure controllability and completeness of answers.
LLM: Initially using GPT-4, with plans to provide proprietary models for scenarios such as private deployments with privacy concerns.
- Text Embedding: Initially using OpenAI Text Embedding model, with plans to provide proprietary models for scenarios such as private deployments with privacy concerns.
- SandBox: For generated results, such as code, provide interactive verification in an environment (FaaS) to allow users to validate and modify if uncertain about authenticity.
- Connector: API integration with peripheral platforms in the future, such as monitoring platforms, to facilitate interaction and operations (e.g., restarts).



# Dev Deployment

Please install the NVIDIA driver on your own. This project has been tested on Python 3.9.18 and CUDA 11.7 environment. The testing has been conducted on the Windows operating system.

1、prepare dev environment 

```bash
# 准备conda环境
conda create --name devopsgpt python=3.9
conda activate devopsgpt
```

```bash
# 安装相关依赖包
pip install -r requirements.txt
```


2. download LLM/Embedding models from huggingface

To download open-source LLM (Language Model) and Embedding models from HuggingFace, follow these steps:

To download the default LLM model, THUDM/chatglm2-6b, and the Embedding model, moka-ai/m3e-base, used in this project, you need to install Git LFS and then run the following commands:

Please install Git LFS first before running the download.
```bash
git lfs install
git lfs clone https://huggingface.co/shibing624/text2vec-base-chinese
```
<br>

3、prepare sandbox environment
- windows docker 安装
[Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/) supports 64-bit versions of Windows 10 Pro and must have Hyper-V enabled (if the version is v1903 or above, Hyper-V is not required), or 64-bit versions of Windows 10 Home v1903 or above.

  - [Windows10 Docker install detail](https://zhuanlan.zhihu.com/p/441965046)
  - [Docker From Beginner to Practice](https://yeasy.gitbook.io/docker_practice/install/windows)
  - [Error: Docker Desktop requires the Server service to be enabled 处理](https://blog.csdn.net/sunhy_csdn/article/details/106526991)
  - [install WSL or wait for ](https://learn.microsoft.com/zh-cn/windows/wsl/install)
<br>

- linux docker install
Please feel free to search on Baidu or Google for relevant installation instructions.
<br>

- mac docker install
comming soon

4、service activation

```bash
cd examples
bash start_webui.py
```


## Licenses
