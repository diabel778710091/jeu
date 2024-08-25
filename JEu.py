import streamlit as st

# Liste des questions et réponses
questions = [
    {"question": "Quelle est la capitale de la France?", "options": ["Paris", "Londres", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "Quel est le plus grand océan du monde?", "options": ["Atlantique", "Indien", "Arctique", "Pacifique"], "answer": "Pacifique"},
    {"question": "Quelle est la formule chimique de l'eau?", "options": ["H2O", "CO2", "O2", "NaCl"], "answer": "H2O"},
]

def main():
    st.title("Quiz Interactif")
    st.write("Répondez aux questions suivantes pour tester vos connaissances!")

    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.show_final_message = False

    if st.session_state.question_index < len(questions):
        question = questions[st.session_state.question_index]

        st.write(f"**Question {st.session_state.question_index + 1}:** {question['question']}")
        selected_option = st.radio("Choisissez une option:", options=question['options'], key=f"radio_{st.session_state.question_index}")

        if st.button("Valider la réponse"):
            if selected_option:
                if selected_option == question['answer']:
                    st.success("Bonne réponse!")
                    st.session_state.score += 10
                else:
                    st.error(f"Mauvaise réponse! La bonne réponse était: {question['answer']}")

                st.session_state.question_index += 1

                if st.session_state.question_index >= len(questions):
                    st.session_state.show_final_message = True

    if st.session_state.show_final_message:
        st.write(f"**Votre score final est:** {st.session_state.score}")
        max_score = len(questions) * 10
        if st.session_state.score == max_score:
            st.balloons()
            st.write("🎉 Félicitations ! Vous avez répondu correctement à toutes les questions ! 🎉")
        else:
            st.write("Merci d'avoir joué ! Vous pouvez recommencer le quiz.")
            if st.button("Recommencer le quiz"):
                reset_quiz()

def reset_quiz():
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.show_final_message = False

if __name__ == "__main__":
    main()
