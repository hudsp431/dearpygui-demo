#Wind Chill calculator
import dearpygui.dearpygui as dpg

# Generate unqiue Ids for all widgets
dpg.create_context()
wind_id = dpg.generate_uuid()
temp_id = dpg.generate_uuid()
output_id = dpg.generate_uuid()
# Call back functions
def get_results():
    wind = dpg.get_value(wind_id)
    temp = dpg.get_value(temp_id)
    windchill = calculate_windchill(wind, temp)
    output = get_output(wind, temp, windchill)
    dpg.set_value(output_id, output)

def calculate_windchill(w, t):
    #35.74 + 0.6215×T - 35.75×V0.16 + 0.4275×T×V0.16
    return int(35.74 + 0.6215 * t - 35.75 * w**0.16 + 0.4275 * t * w**0.16)

def get_output(w, t, wc):
    output = "Witj a windspeed of {} mph".format(w)
    output += "\nand a temperature of {} F".format(t)
    output += "\The temperature feels like{} F".format(wc)
    return output

dpg.create_viewport(title='Windchill Calculator', width=600, height=300)

with dpg.window(label="Windchill Calculator", width=600, height=300):
    dpg.add_text("Hello, welcome to the Windchill Calculator")
    dpg.add_input_int(label="Wind Speed",width=100, tag=wind_id, min_value=0, min_clamped=True)
    dpg.add_input_int(label="Temperature",width=100, tag=temp_id, default_value=0, 
        max_value=40, max_clamped=True)
    dpg.add_button(label="Enter", callback=get_results)
    dpg.add_button(label="clear")
    dpg.add_text("", tag=output_id)
    

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()