import cv2
import numpy as np
import pyttsx3
import pyautogui
import time
import gradio as gr

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Create an image with four dots
def create_dot_image():
    img = np.ones((500, 500, 3), dtype=np.uint8) * 255
    
    dots = [(100, 100, (0, 0, 255)),  # Red
            (200, 300, (0, 255, 0)),  # Green
            (350, 200, (255, 0, 0)),  # Blue
            (400, 400, (0, 255, 255))]  # Yellow
    
    for x, y, color in dots:
        cv2.circle(img, (x, y), 20, color, -1)
    
    return img, dots

def move_cursor_and_speak(dots):
    for i, (x, y, color) in enumerate(dots, start=1):
        pyautogui.moveTo(x, y, duration=1)
        color_name = { (0, 0, 255): 'red', (0, 255, 0): 'green', (255, 0, 0): 'blue', (0, 255, 255): 'yellow'}.get(color, 'unknown')
        speak(f"This is dot {i}, it is {color_name}.")
        time.sleep(1)

def interactive_ai(query):
    response = f"Guru is explaining: {query}"
    speak(response)
    return response

# Gradio UI
with gr.Blocks() as ui:
    gr.Markdown("# 🏫 TutAI - Interactive Learning with Guru")
    gr.Markdown("### Say 'Hey Guru' to start learning!")
    
    query_input = gr.Textbox(placeholder="Ask Guru anything...", label="Your Question")
    output = gr.Textbox(label="Guru's Response")
    submit_btn = gr.Button("Ask Guru")
    
    submit_btn.click(interactive_ai, inputs=[query_input], outputs=[output])

if __name__ == "__main__":
    image, dots = create_dot_image()
    cv2.imshow("Dots", image)
    cv2.waitKey(2000)  # Show image for 2 seconds
    cv2.destroyAllWindows()
    move_cursor_and_speak(dots)
    ui.launch()
