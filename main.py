from tkinter import *

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    if weight_metric.get() == "lbs":
        weight *= 0.453592  # Convert pounds to kilograms
    if height_metric.get() == "in":
        height *= 0.0254  # Convert inches to meters
    bmi = weight / (height ** 2)
    result_label.config(text=f"BMI: {bmi:.2f}")

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    category_label.config(text=f"Category: {category}")

root = Tk()
root.title("BMI Calculator")

# Entry fields for weight and height
weight_label = Label(root, text="Weight:")
weight_label.grid(row=0, column=0, padx=10, pady=10)

weight_entry = Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

height_label = Label(root, text="Height:")
height_label.grid(row=1, column=0, padx=10, pady=10)

height_entry = Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

# Dropdowns for choosing weight and height metric
# weight_metric_label = Label(root, text="Weight Metric:")
# weight_metric_label.grid(row=0, column=2, padx=10, pady=10)

weight_metric = StringVar()
weight_metric.set("kg")
weight_metric_dropdown = OptionMenu(root, weight_metric, "kg", "lbs")
weight_metric_dropdown.grid(row=0, column=3, padx=10, pady=10)

# height_metric_label = Label(root, text="Height Metric:")
# height_metric_label.grid(row=1, column=2, padx=10, pady=10)

height_metric = StringVar()
height_metric.set("cm")
height_metric_dropdown = OptionMenu(root, height_metric, "m", "in")
height_metric_dropdown.grid(row=1, column=3, padx=10, pady=10)

# Button to calculate BMI
calculate_button = Button(root, text="Calculate", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Labels to display the result and category
result_label = Label(root, text="")
result_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

category_label = Label(root, text="")
category_label.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()
