# Import the necessary libraries
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import tkinter as tk

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Define the function to analyze the feedback
def analyze_feedback(feedback):
    # Use the SentimentIntensityAnalyzer to get the sentiment score
    sentiment_score = sia.polarity_scores(feedback)
    # Get the compound sentiment score
    compound_score = sentiment_score['compound']
    # Determine if the feedback is positive or negative based on the compound score
    if compound_score >= 0:
        return "Good"
    else:
        return "Bad"

# Define the function to handle button click event
def submit_feedback():
    # Get the user's feedback from the text box
    feedback = feedback_textbox.get()
    # Analyze the feedback using NLP
    sentiment = analyze_feedback(feedback)
    # Display the result in the label
    result_label.config(text=f"The feedback is {sentiment}!")

# Create the main window
root = tk.Tk()
root.title("Restaurant Feedback")
root.config(background="green")


# Create the feedback label and text box
feedback_label = tk.Label(root, text="Enter your feedback:")
feedback_label.pack(padx=10, pady=10)
feedback_textbox = tk.Entry(root, width=50, font=("Arial", 12))
feedback_textbox.pack(padx=50,pady=50)

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=submit_feedback)
submit_button.pack(padx=20,pady=20)


# Create the label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
