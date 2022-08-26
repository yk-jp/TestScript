import sys
import unittest
import os
from pathlib import Path
import glob
import subprocess
# custom
import config


# extract filename without extension
def extract_filename(path):
    filenames = map(lambda path: Path(path).stem, glob.glob(path))
    return sorted(filenames)


def extract_data_from_file(path, filename) -> str:
    target_file = open(f"{config.INPUT_FILE_PATH}/{filename}", 'r')
    data = "".join(target_file.readlines())
    target_file.close()
    return data


class TestMain(unittest.TestCase):
    def test_main(self):
        file_path = f"{config.INPUT_FILE_PATH}/*in"
        filenames = extract_filename(file_path)

        for filename in filenames:
            with self.subTest(filename=filename):
                input_data = extract_data_from_file(
                    config.INPUT_FILE_PATH, f"{filename}.in")
                input_data = input_data.strip()

                output_data = extract_data_from_file(
                    config.OUTPUT_FILE_PATH, f"{filename}.out")
                output_data = output_data.strip()

                command = f"cd {config.FUNC_FILE_PATH} && echo $'{input_data}' | {config.RUN}"
                res = subprocess.run(
                    command, capture_output=True, text=True, shell=True)

                target = res.stdout.strip()
                target = target.splitlines()[-1]

                self.assertEqual(str(target), str(output_data))


if __name__ == '__main__':
    unittest.main()
