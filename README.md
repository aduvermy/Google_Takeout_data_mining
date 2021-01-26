# Google_Takeout_data_mining
Knowledge extraction from Google Takeout

The amount of data we produce every day is growing exponentially. Especially from smartphones, which contain a multitude of sophisticated sensors, from barometers and gyroscopes to GPS navigation and ambient light sensors. All of these technologies provide mobile data collection methods for apps so they can use your data to enrich your user experience. 

TakeOut by Google allows you to export your Google products. Exports are available as zip formatted downloads. Downloads may be very time consuming - Google will notify you via email after downloads are complete.

Google TakeOut can be found [here](https://takeout.google.com/settings/takeout).

You can export and download your data from the Google products you use, such as your:

    - Email
    - Documents
    - Calendar 
    - Photos
    - YouTube videos
    - Data about registration and account activity
    - ...


This project aims to illustrate how the huge amount of data collected by Google, could be used to improve user experience but is also a door open on user private life 

Please, check the content of your Google TakeOut and use our notebooks to investigating how collection data could be used by GAAFA or Netflix, or other companies owner of applications you use.

# Location History

By using the notebook ```location_history_data_mining.ipynb```, you will be allowed to import location_history.json and used its contents to visualize your data on an interactive map.

### installation required
```
pip install 
pip install 

```
Obviously, our tool is quite fun to remember parts of the world you have visited. 

Here we show a map time series get from GPS data obtained with a European road trip. 

insertion video

However, you should also be aware that this kind of visualization gives easy access to your daily habits.  By using a logical filter such as "from 0:00 am to 5:00 am I stay still and I am at home" our tool allows you to investigate your home location. Or by checking your position during work hours, it informs us about your job and potentially on your way of life.  

Currently, our app needs manual treatment, a possible perspective of our work would be to develop a machine-learning algorithm able to detect hotspots often print on this kind of image and so able to infer user residence location.

# Autors
Adeline, Elsa, Fanny, Fatima, Arnaud
