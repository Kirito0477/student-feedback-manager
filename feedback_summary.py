def show_summary(feedback_list):
    print("---- Feedback Summary ----")
    for entry in feedback_list:
        print(f"{entry['name']} ({entry['score']}): {entry['feedback']}")
