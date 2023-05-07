import PySimpleGUI as sg

layout = [
    [sg.Input(key="-INPUT-"),
     sg.Spin(values=("km to mile", "kg to pound", "sec to min"), key="-UNITS-"),
     sg.Button(button_text="Convert", key="-CONVERT_BUTTON-")],
    [sg.Text(text="Output: ", key="-OUTPUT-")]
]

window = sg.Window("Converter", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-CONVERT_BUTTON-":
        input_value = values["-INPUT-"]
        if input_value.replace(".", "").isnumeric():
            match values["-UNITS-"]:
                case "km to mile":
                    output = round(float(input_value) * 0.6214, 2)
                    output_string = f"{input_value} km are {output} miles."
                case 'kg to pound':
                    output = round(float(input_value) * 2.2046, 2)
                    output_string = f"{input_value} kg are {output} pounds"
                case "min to sec":
                    output = round(float(input_value) / 60, 2)
                    output_string = f"{input_value} seconds are {output} minutes"

            window["-OUTPUT-"].update(output_string)

        else:
            print('You must enter the number!')

window.close()