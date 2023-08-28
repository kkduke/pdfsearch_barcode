import tkinter as tk

def cm_to_pixel():
    # Set the resolution to 300 dpi
    dpi = 300

    # Get the measurements in cm from the Entry widgets
    x_cm = float(x_entry.get())
    y_cm = float(y_entry.get())
    w_cm = float(w_entry.get())
    h_cm = float(h_entry.get())

    # Convert the measurements from cm to pixel
    x_pixel = int((x_cm / 2.54) * dpi)
    y_pixel = int((y_cm / 2.54) * dpi)
    w_pixel = int((w_cm / 2.54) * dpi)
    h_pixel = int((h_cm / 2.54) * dpi)

    # Display the pixel coordinates
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"x, y, w, h = {x_pixel}, {y_pixel}, {w_pixel}, {h_pixel}")

# Create a Tkinter window
root = tk.Tk()
root.geometry("500x300")  # Set the size of the window

# Create Label and Entry widgets for the measurements in cm
tk.Label(root, text="Abstand von links in cm:").pack()
x_entry = tk.Entry(root)
x_entry.pack()

tk.Label(root, text="Abstand von oben in cm:").pack()
y_entry = tk.Entry(root)
y_entry.pack()

tk.Label(root, text="Breite in cm:").pack()
w_entry = tk.Entry(root)
w_entry.pack()

tk.Label(root, text="Höhe in cm:").pack()
h_entry = tk.Entry(root)
h_entry.pack()

# Create a Button widget to trigger the conversion
convert_button = tk.Button(root, text="Convert to Pixel", command=cm_to_pixel)
convert_button.pack()

# Create a Text widget to display the pixel coordinates
result_text = tk.Text(root, height=2, width=30)
result_text.pack()

# Start the Tkinter event loop
root.mainloop()
