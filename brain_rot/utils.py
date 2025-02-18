# Helper function to calculate the brain rot score
def calculate_rot(hours_scrolled, memes_watched):
    return min(100, hours_scrolled * 5 + memes_watched * 5)

# Function to provide tips based on brain rot score
def brain_rot_tip(rot_score):
    if rot_score < 30:
        return "🌟 Fantastic! Keep up the balance — maybe explore a new hobby, meditate, or cook something new! 🧘‍♂️🍳"
    elif rot_score < 70:
        return "🌀 You're on the edge! Take a mindful break — stretch, dance to your favorite song, or do a quick brain teaser! 🧩💃"
    else:
        return "🛑 Whoa! It's time for a digital detox — go for a nature walk, try journaling, or call a friend for a heart-to-heart chat! 🌿📞"
