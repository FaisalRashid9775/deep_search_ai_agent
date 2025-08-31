#Features

1. Modular multi-agent pipeline

2. Uses Tavily for live web research

3. Context-aware personalization via user profiles

4. Conflict detection between research sources

5. Final report generation for users

Setup & Installation

Clone repo

git clone https://github.com/your-username/my_uv_project.git
cd my_uv_project


Create virtual environment (UV recommended)

uv venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows


Install dependencies

uv pip install -r requirements.txt


Environment variables

Create a .env file:

OPENAI_API_KEY=your-openai-api-key
GOOGLE_API_KEY=your-gemini-api-key
TAVILY_API_KEY=your-tavily-api-key

▶️ Running the System

Run the main entrypoint:

python main.py


Expected output:

System will analyze user info

Break query into research plan

Perform deep research with Tavily

Detect conflicts if any

Generate final report

# Example Research Questions

You can test the system with questions like:

1. “Pros and cons of Agentic AI at work in 2025”

2. “How will quantum computing impact businesses by 2030?”

3. “What are the risks and benefits of autonomous vehicles in cities?”

4. “Compare renewable vs nuclear energy for sustainable future.”

🤖 Agents Overview
1. Main Agent

Entry point of the system

Calls userInformation tool for personalization

Delegates to planning_Agent for structured breakdown

Orchestrates full workflow

2. Planning Agent

Breaks down user query into 3 parts

Creates structured research plan

Hands off tasks to lead_research_Agent

3. Lead Research Agent

Core research coordinator

Uses multiple_agent for research

Sends potential conflicts to conflict_agent

Final output routed to report_agent

4. Multiple Agent

Runs Tavily-powered searches

Provides short research snippets

Feeds results to lead_research_Agent

5. Conflict Agent

Analyzes research results

Detects conflicting information

Sends findings to report_agent

6. Report Agent

Collects all research + conflict analysis

Produces final report for user

Handles cases where no data is available

🔧 Tools
🕵️ Search Tool

Wraps Tavily API

Fetches latest, reliable web results

👤 User Information Tool

Personalizes answers

Adds context like user’s name, city, interests

📂 Project Structure
my_uv_project/
│── agents/        # All agent definitions
│── tools/         # Search + user info tools
│── config/        # Settings and API configs
│── main.py        # Runner entrypoint
│── README.md

✅ Example Run (Console Output)
searching for: Pros and cons of Agentic AI at work in 2025
Final Report:
Agentic AI at work in 2025 offers both opportunities and risks...