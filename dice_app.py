import streamlit as st
import random

# Dice faces using Unicode characters
DICE_FACES = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅",
}

st.title("🎲 Dice Roller App")

st.write("Choose how many dice to roll and click the button!")

# Slider: how many dice to roll
num_dice = st.slider("Number of dice", min_value=1, max_value=6, value=2)

# Roll button
if st.button("Roll Dice"):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    
    # Show results as emoji
    dice_emojis = " ".join([DICE_FACES[r] for r in results])
    st.subheader(f"🎲 Results: {dice_emojis}")
    
    # Show total sum
    total = sum(results)
    st.success(f"Total: {total}")
else:
    st.info("Pick a number of dice and press the button above.")
