Upon Joe's request, Jane has implemented a PhysicalInfo class (in Python) to store
the following information from physical examination of patients.
- Date of examination
- Patient's Name
- Patient's Gender
- Patient's Height
- Patient's Temperature
This class provides the following setter methods.
- set_date(string)
- set_name(string)
- set_gender(string)
- set_height(int)
- set_temperature(float)
If the values are invalid, then these setter methods will raise a ValueError
exception. If not, then they will merely return. The specification for valid values
are as follows:
● Name should
○ be a string
○ can only contain alphanumeric, ' ', or '-' character
○ contain at least 2 alphanumeric characters
○ contain at least one character from English alphabet
● Gender should
○ be a string
○ be either 'M' or 'F'
● Height should
○ be an integer
○ be a value between 17 and 84 (both inclusive)
○ measured in inches
● Temperature should
○ be a float
○ be a value between 95 and 104 (both inclusive)
○ measured in fahrenheit
● Date should be valid
○ be a year between 1900 and 2100 (both inclusive)
○ be in (MM-DD-YYYY) format
