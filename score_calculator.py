def calculate_average_score(feedback_list):
    if not feedback_list:
        return 0.0
    total_score = sum(entry["score"] for entry in feedback_list)
    return total_score / len(feedback_list)


def generate_summary(feedback_list):
    average = calculate_average_score(feedback_list)
    return f"Average Feedback Score: {average:.2f}"
