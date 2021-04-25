# picoyplaca_predictor

## Introduction to PicoyPlaca
PicoyPlaca is a policy that originated in Bogota, Colombia back in 1998, which implements driving restrictions with the goal to reduce traffic. This organization limits acces into a pre-determined urban area for vehicles with specific lcense plate endings on a specific date adn time. 

The restriction which I chose to apply in the predictor, was the one with the following restrictions:

* Plates ending in **5, 6, 7, 8** are resticted from driving in the pre-established urban area on Monday
* Plates ending in **9, 0, 1, 2** are resticted from driving in the pre-established urban area on Tuesday
* Plates ending in **3, 4, 5, 6** are resticted from driving in the pre-established urban area on Monday
* Plates ending in **7, 8, 9, 0** are resticted from driving in the pre-established urban area on Monday
* Plates ending in **1, 2, 3, 4** are resticted from driving in the pre-established urban area on Monday
* No restrictions apply on Saturday and Sunday
* Traffic is restricted between 6 and 9 am, and between 5 and 8 pm.

## Technologies 
* Python 3.9

## Run
* python3 main.py

## Testing
The testing is done using unittest framework.
