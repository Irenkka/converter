import sys
import csv
import converter

def convert_temperature(input_file, output_parameter, output_file):
    conversion_function = converter.c_to_f if output_parameter == 'farenheit' else converter.f_to_c

    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        #skip header
        next(reader)

        for row in reader:
            date, temp = row

            # Split temperature string into value and unit
            temp = temp.strip()
            temp_parts = temp.split('°')
            if len(temp_parts) != 2:
                raise ValueError(f"Invalid temperature format in CSV: {temp}")

            temp_value, temp_unit = temp_parts

            if (output_parameter == 'farenheit' and temp_unit == 'C') or \
               (output_parameter == 'celsius' and temp_unit == 'F'):
                temp_value = conversion_function(temp_value)

            temp_unit = 'F' if output_parameter == 'farenheit' else 'C'
            converted_temp = f"{temp_value}°{temp_unit}"

            writer.writerow([date, converted_temp])

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main.py <input_filename> <output_unit> <output_filename>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_parameter = sys.argv[2]
    output_file = sys.argv[3]

    if output_parameter not in ['celsius', 'farenheit']:
        print("Output unit must be 'celsius' or 'farenheit'")
        sys.exit(1)

    try:
        convert_temperature(input_file, output_parameter, output_file)
        print(f"Conversion successful. Output written to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

