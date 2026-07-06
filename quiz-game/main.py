from termcolor import colored
from random import shuffle

# Quiz data.
# Each question contains:
# - the question text
# - four answer options
# - the correct option letter

# declaring dictionary key constants

QUESTION = "question"
OPTIONS = "options"
ANSWER = "answer"


def show_question(question, question_index):
    """Display the current question with its number."""
    print(f"Question {question_index}. {question[QUESTION]}")


def show_options(options):
    """Display all answer options for the current question."""
    for letter, option in options[OPTIONS].items():
        print(f"{letter.upper()}. {option}")


def get_answer():
    """Prompt the user until a valid answer is entered."""
    while True:
        answer = input("Your answer: ").lower().strip()

        # Accept only A, B, C, or D.
        if answer not in ("a", "b", "c", "d"):
            print("Invalid input ⛔")
            continue

        return answer


def compare_answers(answer_input, right_answer, question_dict):
    """Compare the player's answer with the correct answer."""
    if answer_input == right_answer:
        print(colored("Correct answer 👊", "green"))
        return 1

    print(colored("Wrong answer ❌", "red"))

    # Reveal the correct answer after an incorrect response.
    correct = (
        f"The correct answer is "
        f"{question_dict[ANSWER].upper()}. "
        f"{question_dict[OPTIONS][right_answer]}"
    )
    print(colored(correct, "green"))

    return 0


def display_result(result, quiz):
    """Display the player's final score."""
    print(f"You got {result} out of {len(quiz)}")


def play_quiz(quiz):
    """Run the quiz from start to finish."""
    result = 0

    # shuffle question on different code run
    shuffle(quiz)

    # Loop through every question while numbering them from 1.
    for dict_index, question_dict in enumerate(quiz, start=1):
        show_question(question_dict, dict_index)
        show_options(question_dict)

        right_answer = question_dict[ANSWER]
        answer_input = get_answer()

        result += compare_answers(
            answer_input,
            right_answer,
            question_dict,
        )

        # Leave a blank line before the next question.
        print()

    display_result(result, quiz)
    print()


def main():
    quiz = [
        {
            QUESTION: "Which of these is the largest ocean on Earth ?",
            OPTIONS: {
                "a": "Atlantic",
                "b": "Indian",
                "c": "Arctic",
                "d": "Pacific",
            },
            ANSWER: "d",
        },
        {
            QUESTION: "The largest planet is ?",
            OPTIONS: {
                "a": "Venus",
                "b": "Jupiter",
                "c": "Earth",
                "d": "Pluto",
            },
            ANSWER: "b",
        },
        {
            QUESTION: "Which is the most populated continent ?",
            OPTIONS: {
                "a": "Africa",
                "b": "Europe",
                "c": "Asia",
                "d": "North America",
            },
            ANSWER: "c",
        },
    ]
    play_quiz(quiz)


# Run the program only when executed directly.
if __name__ == "__main__":
    main()
