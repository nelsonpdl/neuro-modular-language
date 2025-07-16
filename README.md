Neuro-Modular Language (.nml)
The Neuro-Modular Language (.nml) is a cognitive, modular, and functional language designed to structure prompts like executable code — unlocking precise reasoning, modular task flows, and autonomous decision logic in LLMs.

🧠 Why .nml?
Traditional prompt engineering is linear and fragile.
.nml introduces a neuro-inspired syntax that mimics how the brain organizes thought: by identity, intention, context, rules, memory and execution. Modular, scalable, and cognitively aligned.

🔧 Core Structure
A .nml file is built using execution-ready cognitive modules:

::identity
You are a financial AI agent trained to optimize tax strategy.

::intent
Your goal is to reduce IRS tax liability for U.S.-based 1099 freelancers.

::context
The user is a self-employed creative with irregular income.

::memory
User previously claimed deductions on home office, meals, and software.

::rules
- Never advise anything illegal.
- Prioritize deductions that reduce adjusted gross income.

::execution
Analyze user's last 3 expense categories and propose 3 deduction strategies.
.nml treats prompts like a neuro-executable script with reasoning stages, memory injection, and context modulation.

⚙️ Files in this Repo
main.py – orchestrator engine to execute .nml structure.
parser.py – parses .nml syntax into actionable blocks.
action.py – maps modules to execution logic.
example.nml – runnable sample prompt.

📦 How to Run
python main.py example.nml
Requires Python 3.8+ and an OpenAI-compatible LLM API key (set in .env).

🧩 Use Cases
Multi-layered decision agents
LLMs that simulate expert roles
Modular educational tutors
Executable coaching/consulting flows

## ⚔️ vs Traditional Prompting

| Feature              | Traditional Prompts       | .nml Modular Prompts         |
|----------------------|----------------------------|-------------------------------|
| **Structure**        | Linear                     | Hierarchical & Layered       |
| **Modularity**       | None                       | Full cognitive blocks         |
| **Reusability**      | Low                        | High                          |
| **Debuggability**    | Hard                       | Precise module trace          |
| **Identity & Intent**| Implicit                   | Explicit in core structure    |


🧠 Philosophy
Inspired by the prefrontal cortex, .nml treats prompts as living cognitive entities that think, decide, and evolve.
Built by Nelson Padilla — founder of Dynibyte, pioneer of CMA™ (Cognitive Modular Agents).

📜 License
To be added: [MIT] or [Open Core License] depending on roadmap.

🧪 Contribute
We’re just getting started.
Ideas? Issues? PRs? All welcome.
Want to build your own agent with .nml? Fork it.

🚀 This is not a prompt.
This is neuro-executable cognition.
Let’s redefine how LLMs think.

📜 License  
This project follows an **Open Core licensing model**.  
- The `.nml` core language and parser are open-source under the MIT License.  
- Advanced systems like **NOAP™**, **SAC™**, and **C.O.R.E Protocols™** are proprietary extensions and not part of the open-source core.
