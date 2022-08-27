import os.path

filename = "config.py"


def file_exists():
    return os.path.exists(filename)


def main():
    res = "a"

    try:
        if file_exists():
            while res.lower() != "y" and res.lower() != "n":
                res = input(
                    "Config file already exists. Do you want to update it?  y/n \n")

            if res.lower() == "n":
                print("Set up was terminated")
                return

        input_file_path = input("Enter the file path for input data \n")
        output_file_path = input("Enter the file path for output data \n")
        func_file_path = input(
            "Enter the file path where the function is located \n")
        run_command = input("Enter the execute command \n")

        config_data = [
            f"INPUT_FILE_PATH = \"{input_file_path}\"",
            f"OUTPUT_FILE_PATH = \"{output_file_path}\"",
            f"FUNC_FILE_PATH = \"{func_file_path}\"",
            f"RUN = \"{run_command}\""
        ]

        config_file = open("config.py", "w")

        for data in config_data:
            config_file.write(f'{data}\n')

        config_file.close()

    except KeyboardInterrupt:
        print('Set up was termintated')
        return

    print("")
    print("Setup all done!")


if __name__ == '__main__':
    main()
