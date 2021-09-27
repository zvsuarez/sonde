# TEMPCodeur Upper-Air Sounding Decoder

Windows desktop application that decodes meteorological upper-air sounding data made with PyQt5 framework, Python, and Qt Designer.

![interface](https://user-images.githubusercontent.com/64736073/134896933-5c003f89-4de0-43e0-8ad0-86a78f73e8b9.PNG)

## Usage

>Users can open _*txt_ files that contain a sounding data and the raw code will be automatically inserted in the input text field.

![text file](https://user-images.githubusercontent.com/64736073/134905719-d7852422-68e4-4de3-add6-29213f21cfdc.PNG)

>or copying from websites that upload soundings and pasting it on the input text field also works.

![ogimet sounding](https://user-images.githubusercontent.com/64736073/134905999-5085073d-21a7-470f-ad6d-0577330dcc61.PNG)

>Before decoding the data, '_=_' should be omitted at the end. This is to ensure that Sea Surface Data can be decoded properly and not return an _Invalid_ result.

![tempcodeur with data](https://user-images.githubusercontent.com/64736073/134912641-cace1f20-b4bd-4dd2-8042-4989425acd9d.PNG)

Some buttons are disabled if the input text field is empty. Errors will be raised once an incorrect format and syntax is detected.

## Output

>A dialog window containing the result will appear once _Decode_ is clicked. 

![result window](https://user-images.githubusercontent.com/64736073/134913198-5560d038-d6a5-4ed8-8fb3-5d8c7a8cec6a.PNG)

>This can be saved as an _xlsx_ file, and can be opened with spreadsheet programs.

![output](https://user-images.githubusercontent.com/64736073/134913378-41661bc5-d338-468f-91e6-e27e99d15610.PNG)

## References/User Guide

References for analysing the sounding results especially the **_Solar_**, **_Radiosonde_**, **_Tracking System_**, and **_Cloud_** data are included in the release package of the software. The _Federal Meteorological Handbook No. 3_ is also available [here](https://www.icams-portal.gov/publications/fmh/FMH3/00-entire-FMH3.pdf).

## Credits

Icons are from **_Yusuke Kamiyamane's Fugue Icon set_**, **_FlatIcons_** and **_Freepik_**.
