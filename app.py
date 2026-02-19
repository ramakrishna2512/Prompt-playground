import streamlit as st
import ollama

st.set_page_config(layout="wide", page_title="Prompt Playground")

# ---------- SESSION ----------
if "prompt_library" not in st.session_state:
    st.session_state.prompt_library = {}

if "selected_prompt" not in st.session_state:
    st.session_state.selected_prompt = ""

# ---------- OLLAMA SAFE CALL ----------
def ask_llama(system_prompt, user_input, model, temp):
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            options={"temperature": temp}
        )
        return response["message"]["content"]

    except Exception as e:
        return f"❌ Ollama Error:\n\n{e}\n\n👉 Try:\n• run ollama run {model}\n• disable GPU\n• use smaller model"

# ---------- LAYOUT ----------
col_main, col_right = st.columns([3,1])

# ===== MAIN =====
with col_main:
    st.title("Prompt Tester")

    user_input = st.text_area(
        "User Input",
        placeholder="Enter your question...",
        height=120
    )

    if st.button("▶ Run", use_container_width=True):
        if st.session_state.selected_prompt == "":
            st.warning("Select a prompt first")
        elif user_input.strip() == "":
            st.warning("Enter input")
        else:
            with st.spinner("Thinking..."):
                result = ask_llama(
                    st.session_state.selected_prompt,
                    user_input,
                    st.session_state.model,
                    st.session_state.temp
                )
            st.subheader("Response")
            st.write(result)

# ===== RIGHT PANEL =====
with col_right:
    st.subheader("⚙ Settings")

    # MODEL SELECTOR
    st.session_state.model = st.selectbox(
        "Model",
        [
            "llama3",
            "llama3:8b-instruct",
            "mistral",
            "phi3"
        ]
    )

    # TEMPERATURE
    st.session_state.temp = st.slider(
        "Temperature",
        0.0, 2.0, 1.0
    )

    st.divider()
    st.subheader("📚 Prompt Library")

    if st.session_state.prompt_library:
        selected_name = st.selectbox(
            "Select Prompt",
            list(st.session_state.prompt_library.keys())
        )
        st.session_state.selected_prompt = st.session_state.prompt_library[selected_name]
    else:
        st.info("No prompts saved")

    st.divider()
    st.subheader("➕ Add Prompt")

    name = st.text_input("Prompt Name")

    content = st.text_area(
        "Prompt Content",
        height=200,
        placeholder="Paste your long system prompt..."
    )

    if st.button("💾 Save Prompt", use_container_width=True):
        if name and content:
            st.session_state.prompt_library[name] = content
            st.success("Saved!")
            st.rerun()
        else:
            st.warning("Enter name & content")

    if st.session_state.prompt_library:
        if st.button("🗑 Delete Selected"):
            del st.session_state.prompt_library[selected_name]
            st.rerun()