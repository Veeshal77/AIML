**Excel‑Driven Customer Support Agent (POC)**
A lightweight, local, Python‑based agentic workflow that reads customer issues from Excel, retrieves relevant knowledge‑base entries, 
applies rule‑based reasoning, and writes resolutions back into the dataset. This Proof of Concept demonstrates how retrieval + reasoning + action 
can be implemented without cloud infrastructure or complex orchestration.

**Features**
Excel‑based data layer — no database required

Knowledge‑base retrieval using keyword matching

Hybrid reasoning engine (KB → rule‑based fallback)

Agentic workflow (retrieve → reason → act)

CLI interface for interacting with issues

Local execution — runs entirely on your laptop

**Project Structure**
customer-support-agent/
│
├── customer.xlsx              # 1000 synthetic customer issues
├── knowledge_base.xlsx        # Issue types, keywords, resolutions
│
├── tools.py                   # Excel read/write + KB retrieval functions
├── main.py                    # Agent workflow + CLI
│
├── .env                       # API keys (optional for future LLM use)
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

**How the Agent Works**
1. Retrieval
Loads the selected issue from customer.xlsx
Searches knowledge_base.xlsx for matching symptoms

2. Reasoning
If KB match found → uses KB resolution
If no match → falls back to rule‑based logic

3. Action
Writes the generated resolution and updated status back into Excel
Allows user confirmation before updating

**Setup Instructions**
1. Clone the repository
2. git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

2. Create a virtual environment
python -m venv agent-env
Activate it:
Windows:
agent-env\Scripts\activate

macOS/Linux
source agent-env/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the agent
python main.py

**Excel Files**
customer.xlsx
Contains 1000 synthetic issues with:
IssueId
IssueText
AgentSuggestedResolution
Status

knowledge_base.xlsx
Contains issue categories with:
IssueType
Symptoms (comma‑separated keywords)
ResolutionSteps

**POC Steps Implemented**
Installed Python + created virtual environment
Created customer.xlsx with 1000 issues
Created knowledge_base.xlsx with 9 issue categories
Implemented Excel tooling (tools.py)
Implemented KB retrieval logic
Implemented rule‑based fallback reasoning
Built CLI agent (main.py)
Added Excel write‑back functionality

**Future Enhancements**
Replace rule‑based logic with LLM reasoning
Add multi‑step agent planning
Add Streamlit UI
Add logging + traceability
Expand knowledge base
