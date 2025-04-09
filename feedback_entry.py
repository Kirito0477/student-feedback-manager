def collect_feedback():
    feedback_list = []

    while True:
        name = input("Enter student name (or 'q' to quit): ")
        if name.lower() == 'q':
            break
        score = int(input("Enter feedback score (1-10): "))
        feedback = input("Enter feedback comment: ")

        feedback_list.append({
            "name": name,
            "score": score,
            "feedback": feedback
        })

    return feedback_list
