### 🌟 AI-Powered FAQ Retrieval System 🚀
Welcome to the AI-Powered FAQ Retrieval System! This project combines cutting-edge AI technologies like LangChain, FAISS, and Google Generative AI to create an intelligent, context-aware FAQ solution. 💡

### ✨ Features
🔍 Vector Search: Efficiently retrieves relevant information using FAISS.
🧠 AI-Powered Embeddings: Leverages the sentence-transformers/all-MiniLM-L6-v2 model for high-quality embeddings.
🤖 Google Generative AI: Integrates Google's Gemini model to generate human-like responses.
📚 Contextual QA: Answers are strictly based on the provided context for accurate and reliable outputs.
🛠️ Customizable Prompts: Fine-tune the system's behavior using dynamic prompt templates.
🛠️ Prerequisites
🐍 Python 3.8+
📦 HuggingFace Transformers
⚡ LangChain
🔑 Google API Key with access to Generative AI features.
📦 Installation

### Clone the repository 🖥️:

bash
Copier
Modifier
git clone https://github.com/yourusername/ai-faq-retrieval.git
cd ai-faq-retrieval

### Install dependencies 📥:

bash
Copier
Modifier
pip install -r requirements.txt
Set up environment variables 🛡️: Create a .env file and add your Google API key:

### env
Copier
Modifier
GOOGLE_API_KEY=your_api_key_here
🚀 Usage

### Create the Vector Database:

bash
Copier
Modifier
python main.py
This processes the codebasics_faqs.csv file and saves the FAISS index.

### Query the System 🧑‍💻: Update the script's last line with your query, e.g.:

python
Copier
Modifier
print(chain("Do you have a JavaScript course?"))
Get Insights 💡: The system retrieves and generates an answer based on the FAQ dataset.

### 📂 File Structure
bash
Copier
Modifier

### 📦 project-directory
├── 📄 main.py                  # Main script
├── 📄 requirements.txt         # Dependencies
├── 📄 .env                     # API key configuration
├── 📄 codebasics_faqs.csv      # FAQ data

### 🌍 Contributing
Contributions are welcome! 🤗 Feel free to fork this repo, create a pull request, or open an issue.

### 💬 Feedback
We'd love to hear your thoughts! Share your feedback or questions via GitHub Issues. 😊

### 📝 License
This project is licensed under the MIT License. 📜 See the LICENSE file for details.
