# TestScript

# function-with-input

Configure file path and command to run your functions
``` py
# File name must be .in for input and .out for output. The same file name are recognized as the set of test data.
INPUT_FILE_PATH = ""  
OUTPUT_FILE_PATH = "" 
FUNC_FILE_PATH = ""   # the location of the function
RUN = "" 
```

Run this command
```
python test_main.py
```

You can set up config.py in your terminal by executing
```
python config_setup.py
``` 

*Note

The data which is printed at the end in the function is used for the test

``` swift
func exapmle() -> Int {
  output1 = 1
  output2 = 2

  print(output1)
  print(output2) // This output2 is used for the comparison
  return output2
}
```
