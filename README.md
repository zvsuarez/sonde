# Sonde UASM (Upper Air Sounding Message) Decoder

A Windows desktop application for decoding meteorological upper-air sounding messages made with **_PyQt5_**, **_Python_**, and **_Qt Desig_**.

## Interface

![interface](https://user-images.githubusercontent.com/64736073/146811186-51ee6403-550e-4325-8d22-baac8f63ed2f.PNG)

## Usage

Users can open **_txt_** files that contain sounding data and the raw code will be automatically inserted in the input text field.

![text file](https://user-images.githubusercontent.com/64736073/134905719-d7852422-68e4-4de3-add6-29213f21cfdc.PNG)

or copying from websites that upload soundings and pasting it on the input text field also works.

![reference](https://user-images.githubusercontent.com/64736073/146811308-36d3ba5c-156f-4b07-a6f3-45ba79257d5f.PNG)

Before decoding the data, _=_ should be omitted at the end. This is to ensure that **Sea Surface Data** are decoded properly and not return an _Invalid_ result.

![sonde filled](https://user-images.githubusercontent.com/64736073/146811852-cfead339-cf13-4154-ac1c-5a414837548c.PNG)

Some buttons are disabled if the input text field is empty. Errors will be raised once an incorrect format and syntax is detected.

## Output

A dialog window containing the result will appear once _Decode_ is clicked. 

![result](https://user-images.githubusercontent.com/64736073/146811505-b856f48a-df95-400c-a2df-4f550aef7666.PNG)

This can be saved as an **_xlsx_** file, and can be opened with spreadsheet programs.

![excel](https://user-images.githubusercontent.com/64736073/146811546-09432f89-dbc6-4b26-b5e8-5384a1af8025.PNG)

## References/User Guide

References for analysing the sounding results especially the _Solar_, _Radiosonde_, _Tracking System_, and _Cloud_ data are included in the release package of the software. The **_Federal Meteorological Handbook No. 3_** is also available [here](https://www.icams-portal.gov/publications/fmh/FMH3/00-entire-FMH3.pdf).

## Credits

Icons are from **_Yusuke Kamiyamane's Fugue Icon set_**, **_FlatIcons_** and **_Freepik_**.
