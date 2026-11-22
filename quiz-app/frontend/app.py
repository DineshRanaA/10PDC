
import streamlit as st
import requests

import streamlit.components.v1 as components

def scroll_to_top():
    components.html(
        """
        <script>
            window.parent.document.querySelector(
                'section.main'
            ).scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        </script>
        """,
        height=0
    )

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Quiz Application",
    page_icon="📝",
    layout="centered"
)

API_URL = "http://127.0.0.1:8000"

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "questions" not in st.session_state:
    st.session_state.questions = []

if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

if "quiz_result" not in st.session_state:
    st.session_state.quiz_result = None


# --------------------------------------------------
# Application Title
# --------------------------------------------------

st.title("📝 Quiz Application")
st.write("Welcome to our Quiz Application!")

if st.session_state.get("scroll_top", False):

    scroll_to_top()

    st.session_state.scroll_top = False

st.divider()


# --------------------------------------------------
# Backend Connection
# --------------------------------------------------

with st.expander("Backend Connection", expanded=False):

    if st.button("Check Backend Connection"):

        try:
            response = requests.get(
                f"{API_URL}/health",
                timeout=5
            )

            if response.status_code == 200:
                st.success("Backend Connected Successfully!")
                st.json(response.json())

            else:
                st.error("Backend returned an error.")

        except requests.exceptions.RequestException as error:
            st.error(f"Backend connection failed: {error}")


# --------------------------------------------------
# Fetch Questions
# --------------------------------------------------

def load_questions():

    try:
        response = requests.get(
            f"{API_URL}/questions",
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        st.session_state.questions = data["questions"]

        st.session_state.quiz_submitted = False
        st.session_state.quiz_result = None

        return True

    except requests.exceptions.RequestException as error:

        st.error(f"Unable to fetch questions: {error}")
        return False

    except (KeyError, ValueError) as error:

        st.error(f"Invalid API response: {error}")
        return False


# --------------------------------------------------
# Start Quiz
# --------------------------------------------------

if st.button("🚀 Start Quiz", type="primary"):

    if load_questions():
        st.success(
            f"Quiz started! Total questions: "
            f"{len(st.session_state.questions)}"
        )
        st.rerun()


# --------------------------------------------------
# Quiz Questions
# --------------------------------------------------

questions = st.session_state.questions

if questions and not st.session_state.quiz_submitted:

    st.divider()

    st.subheader("📚 Answer the Questions")

    st.write(f"Total Questions: {len(questions)}")

    answer_mapping = {}

    with st.form("quiz_form"):

        for index, question in enumerate(questions):

            question_id = question["id"]

            st.markdown(
                f"### Question {index + 1}"
            )

            st.write(question["question"])

            options = question["options"]

            # Support both dictionary and list options
            if isinstance(options, dict):
                option_items = list(options.items())
            else:
                option_items = [
                    (chr(65 + i), option)
                    for i, option in enumerate(options)
                ]

            option_labels = []

            for key, value in option_items:

                label = f"{key}. {value}"

                option_labels.append(label)

                answer_mapping[(question_id, label)] = key

            selected_option = st.radio(
                "Select your answer:",
                options=option_labels,
                key=f"question_{question_id}",
                index=None
            )

            st.divider()

        submitted = st.form_submit_button(
            "Submit Quiz",
            type="primary",
            use_container_width=True
        )

        if submitted:

            unanswered = []

            answers = []

            for question in questions:

                question_id = question["id"]

                selected_option = st.session_state.get(
                    f"question_{question_id}"
                )

                if selected_option is None:
                    unanswered.append(question_id)
                    continue

                selected_answer = answer_mapping[
                    (question_id, selected_option)
                ]

                answers.append({
                    "question_id": question_id,
                    "answer": selected_answer
                })

            if unanswered:

                st.warning(
                    f"Please answer all questions. "
                    f"Unanswered questions: {len(unanswered)}"
                )

            else:

                try:

                    response = requests.post(
                        f"{API_URL}/submit",
                        json={"answers": answers},
                        timeout=10
                    )

                    response.raise_for_status()

                    st.session_state.quiz_result = response.json()

                    st.session_state.quiz_submitted = True

                    st.session_state.scroll_top = True

                    st.rerun()

                except requests.exceptions.RequestException as error:

                    st.error(f"Quiz submission failed: {error}")


# --------------------------------------------------
# Quiz Results
# --------------------------------------------------

if st.session_state.quiz_submitted:

    result = st.session_state.quiz_result

    st.divider()

    st.header("🎉 Quiz Results")

    total = result["total_questions"]
    correct = result["correct_answers"]
    wrong = result["wrong_answers"]
    score = result["score"]

    percentage = (
        (correct / total) * 100
        if total > 0 else 0
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Questions", total)
    col2.metric("Correct Answers", correct)
    col3.metric("Wrong Answers", wrong)

    st.subheader(f"Your Score: {score}/{total}")

    st.progress(int(percentage))

    st.write(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        st.success("Excellent! Great job! 🏆")

    elif percentage >= 50:
        st.info("Good effort! Keep practicing! 👍")

    else:
        st.warning("Keep learning. You can do better! 💪")

    st.divider()

    st.subheader("📋 Answer Review")

    question_lookup = {
        question["id"]: question
        for question in questions
    }

    for index, item in enumerate(result["results"]):

        question = question_lookup.get(item["question_id"])

        if question is None:
            continue

        st.markdown(f"### Question {index + 1}")

        st.write(question["question"])

        if item["is_correct"]:

            st.success(
                f"Your Answer: {item['selected_answer']} "
                f"— Correct!"
            )

        else:

            st.error(
                f"Your Answer: {item['selected_answer']}"
            )

            st.info(
                f"Correct Answer: {item['correct_answer']}"
            )

    st.divider()

    if st.button("🔄 Try Again", use_container_width=True):

        st.session_state.questions = []
        st.session_state.quiz_submitted = False
        st.session_state.quiz_result = None

        st.rerun()
