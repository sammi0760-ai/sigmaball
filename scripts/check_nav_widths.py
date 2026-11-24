# Test navbar width requirements across EN, ES, KO
nav_items = {
    "en": ["Simulation", "Workflow", "Features", "FAQ", "Notice", "Privacy Policy"],
    "es": ["Simulación", "Flujo", "Funciones", "Preguntas", "Aviso Legal", "Privacidad"],
    "ko": ["시뮬레이터", "워크플로우", "주요 기능", "자주 묻는 질문", "면책 공지", "개인정보처리방침"]
}

for lang, items in nav_items.items():
    total_chars = sum(len(x) for x in items)
    # Approx width in px assuming 8.5px per char + 22px gap
    approx_width = sum(len(x) * 9 + 22 for x in items)
    print(f"Lang [{lang}]: {total_chars} total chars, approx nav-links width: {approx_width}px")
