# Sonde (Upper Air Sounding Message) Decoder

_Windows_ desktop application for decoding meteorological upper-air sounding messages made with **_Python_**, **Qt5**, and **_Qt Designer_**.

## Installation

> Download Sonde_v1a.zip [here](https://github.com/zvsuarez/sonde/releases).

## Usage

Users can open **_.txt_** files that contain sounding data and the raw code will be automatically inserted in the input text field.

![text file](https://user-images.githubusercontent.com/64736073/134905719-d7852422-68e4-4de3-add6-29213f21cfdc.PNG)

or copying from websites that upload soundings and pasting it on the input text field.

![reference](https://user-images.githubusercontent.com/64736073/146811308-36d3ba5c-156f-4b07-a6f3-45ba79257d5f.PNG)

Before decoding the data, **=** should be omitted at the end. This is to ensure that **Sea Surface Data** are decoded properly and not return an **Invalid** result.

![sonde filled](https://user-images.githubusercontent.com/64736073/146811852-cfead339-cf13-4154-ac1c-5a414837548c.PNG)

Errors will be raised once an incorrect format and syntax is detected.

## Output

A dialog window containing the result will appear once **Decode** is clicked. 

![result](https://user-images.githubusercontent.com/64736073/146811505-b856f48a-df95-400c-a2df-4f550aef7666.PNG)

**_.xlsx_** and **_.xls_** are the currently available formats for saving. Implementations to save as **_.csv_** will be pushed at an unidentified date.

## References/User Guide

References for analysing the sounding results for: _Solar_, _Radiosonde_, _Tracking System_, and _Cloud_ data are included in the release package of the software. The **_Federal Meteorological Handbook No. 3_** is also available [here](https://www.icams-portal.gov/publications/fmh/FMH3/00-entire-FMH3.pdf).