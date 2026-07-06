from termcolor import colored

quiz = [
    {
        "question": "What is the largest ocean on Earth?",
        "options": {
            "a": "Atlantic",
            "b": "Indian",
            "c": "Arctic",
            "d": "Pacific",
        },
        "answer": "d",
    },
    {
        "question": "Which of these is the largest planet?",
        "options": {
            "a": "Venus",
            "b": "Jupiter",
            "c": "Earth",
            "d": "Pluto",
        },
        "answer": "b",
    },
    {
        "question": "Which is the most populated continent?",
        "options": {
            "a": "Africa",
            "b": "Europe",
            "c": "Asia",
            "d": "North America",
        },
        "answer": "c",
    },
]


def show_question(question, question_index):
    print(f"Question {question_index}. {question['question']}")


def show_option(options):
    for letter, option in options["options"].items():
        print(f"{letter.upper()}. {option.capitalize()}")


def correct_answer(answer):
    return answer["answer"]


def get_answer():
    while True:
        answer = input("Your answer: ").lower().strip()
        if answer not in ("a", "b", "c", "d"):
            print("Invalid input ⛔")
            continue
        return answer


def compare_answers(answer_input, right_answer, question):
    if answer_input == right_answer:
        color_text = colored("Correct answer👊", "green")
        print(color_text)
        return 1

    color_text = colored("Wrong answer ❌", "red")
    print(color_text)
    color_correct_answer = f"The correct answer is {question['options'][right_answer]}"
    print(colored(color_correct_answer, "green"))
    return 0


def display_result(result):
    print(f"You got {result} out of {len(quiz)}")


def play_quiz():
    result = 0
    question_index = 0
    for question_dict in quiz:
        show_question(question_dict, question_index)
        question_index += 1
        show_option(question_dict)
        right_answer = correct_answer(question_dict)
        answer_input = get_answer()
        result += compare_answers(answer_input, right_answer, question_dict)
    display_result(result)


if __name__ == "__main__":
    play_quiz()
