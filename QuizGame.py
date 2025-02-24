def quiz_game():
    questions = [
        {"question": "What is the capital of France", "options": ["A. Paris", "B. Rome", "C. Madrid"], "answer": "A"},
        {"question": "What is 5 + 7?", "options": ["A. 10", "B. 12", "C, 14"], "answer": "B"},
        {"question": "Which planet is known as the Red Planet?", "options": ["A. Venus", "B. Mars", "C. Mercury"], "answer": "B"},
        {"question": "What year was the French Revolution?", "options": ["A. 1892", "B. 1704", "C. 1789"], "answer": "C"}
    ]

    score = 0
    for q in questions:
        print(f"\n{q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Enter your answer (A/B/C): ").strip().upper()
        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")
            