from termcolor import colored
from random import shuffle

# Dictionary keys used throughout the quiz.
QUESTION = "question"
OPTIONS = "options"
ANSWER = "answer"


def show_question(question, question_index):
    """Display the current question with its number."""
    print(f"Question {question_index}. {question[QUESTION]}")


def show_options(question_dict):
    """Display all answer options for the current question."""
    for letter, option in question_dict[OPTIONS].items():
        print(f"{letter.upper()}. {option}")


def get_answer():
    """Prompt the user until a valid answer is entered."""
    while True:
        answer = input("Your answer: ").lower().strip()

        # Accept only the available option letters.
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


def display_result(score, total_question):
    """Display the player's final score."""
    print(f"You got {score} out of {total_question}")


def play_quiz(quiz):
    """Run the quiz from start to finish."""
    result = 0

    # Work on a copy so the original quiz order remains unchanged.
    quiz = quiz.copy()
    shuffle(quiz)

    # Display each question, collect the answer, and update the score.
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

        print()

    display_result(result, len(quiz))
    print()


def main():
    """Create the quiz data and start the game."""
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


# Run the program only when this file is executed directly.
if __name__ == "__main__":
    main()