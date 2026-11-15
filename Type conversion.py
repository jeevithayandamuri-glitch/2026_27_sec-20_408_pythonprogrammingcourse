#Type conversion
str_value="110"
int_value=int(str_value)
float_value=float(int_value)
str_value=str(float_value)
print(f"integer value:{int_value},{type(int_value)}")
print(f"float value:{float_value},{type(float_value)}")
print(f"string value:{str_value},{type(str_value)}")