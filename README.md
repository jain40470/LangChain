
# LangChain Tutorials 

This repository offers a collection of tutorials and demonstrations to help users understand and implement LangChain, a framework for developing applications powered by large language models (LLMs).

## 🧠 About LangChain

[LangChain](https://www.langchain.com/) is an open-source framework designed to simplify the integration of LLMs into applications.
It provides tools and abstractions for building complex applications like chatbots, document summarizers, and more.
LangChain supports both Python and JavaScript, offering flexibility for developers.

## 📁 Repository Contents

- **`Langchain_essential.ipynb`**: A notebook covering the fundamental concepts and components of LangChain, including chains, prompts, and memory.
- **`langchain_tut.ipynb`**: An in-depth tutorial demonstrating advanced features of LangChain, such as agents, tools, and integrations with external APIs.
- **`app_demo_langserve.py`**: A Python script showcasing how to deploy a LangChain application using LangServe, enabling it to run as a production-ready API.
- **`requirements.txt`**: Lists all the Python dependencies required to run the notebooks and scripts in this repository.

## 🛠️ Getting Started

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jain40470/LangChain.git
   cd LangChain
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the notebooks:**
   ```bash
   jupyter notebook
   ```
   Open the desired notebook (`Langchain_essential.ipynb` or `langchain_tut.ipynb`) in your browser to start exploring.

5. **Run the LangServe demo:**
   ```bash
   python app_demo_langserve.py
   ```
   This will start a local server hosting your LangChain application.

## 📚 Tutorials Overview

### Langchain_essential.ipynb

This notebook introduces the core components of LangChain:

- **Chains**: Sequences of calls to LLMs or other utilities.
- **Prompts**: Templates for interacting with LLMs.
- **Memory**: Mechanisms to store and retrieve information across interactions.

It provides hands-on examples to illustrate how these components work together to build intelligent applications.

### langchain_tut.ipynb

This advanced tutorial delves into:

- **Chat Models Integration**
- **Embedding Model**
- **Similarity Checking (cosine_similarity)**
- **Prompts in Langchain**
- **Structured Outputs in Langchain**
- **Chains and Runnable Concept**
- **LCEL**
- **Agents**: Components that make decisions about which actions to take.
- **Tools**: External functionalities that agents can utilize, such as web search or calculators.
- **Integrations**: Connecting LangChain with external APIs and services to enhance capabilities.

The notebook includes practical examples demonstrating how to build complex workflows using these features.

### app_demo_langserve.py

This script demonstrates how to deploy a LangChain application using LangServe:

- **LangServe**: A tool to host LangChain applications as APIs.
- **Deployment**: Setting up a local server to serve your LangChain application.

Running this script will start a server, making your application accessible via HTTP requests.

## 🤝 Contributing

Contributions are welcome!
If you have suggestions, improvements, or additional tutorials to add, feel free to fork the repository and submit a pull request.

## 📄 License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.

## 📞 Contact

For questions or support, please open an issue in the repository or contact the maintainer directly.
