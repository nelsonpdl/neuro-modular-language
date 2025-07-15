# action.py

def execute_actions(sections):
    signal_patterns = sections.get("signal_patterns", [])
    
    # Simulación de fallback si está vacío
    if not signal_patterns:
        print("⚠️ No signal patterns found. Injecting test signal for simulation.\n")
        signal_patterns = ["test signal: fake pain"]

    leads = []
    for i in range(5):  # Simula 5 leads encontrados
        lead = {
            "platform": "LinkedIn",
            "user_handle": f"user_{i}",
            "detected_signal": signal_patterns[i % len(signal_patterns)],
            "lead_type": "B2B SaaS",
            "intent_level": "high" if i % 2 == 0 else "medium"
        }
        leads.append(lead)

    print("✅ Leads harvested:\n")
    for lead in leads:
        print(lead)
