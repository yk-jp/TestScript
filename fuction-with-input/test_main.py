import sys
import unittest
import os
from pathlib import Path
import glob
from io import StringIO
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
                output_data = extract_data_from_file(
                    config.OUTPUT_FILE_PATH, f"{filename}.out")
                function_res = os.system(
                    f"cd {config.FUNC_FILE_PATH} && echo $'{input_data}' | {config.RUN}")

                self.assertEqual(str(function_res).strip(), str(output_data).strip())

if __name__ == '__main__':
    unittest.main()
