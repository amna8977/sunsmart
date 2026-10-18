# THIS IS SUNSMART!!
[https://amna8977.github.io/sunsmart/
](https://amna8977.github.io/sunsmart/)

intro
--
No matter where you are or who you are, you've probably experienced a sunburn. Sunburns are one of many side effects of prolonged exposure to UV, or ultraviolet, radiation (light). UV light comes from the sun, and while it helps you get vitamin D, it can sometimes be harmful. UV radiation can mutate skin cells, and these cells can build up and become skin cancer. Sunsmart aims to help people protect their skin using sunscreen, cover-ups, and other methods.

# pages 
`index.html`- this is the home page of Sunsmart
`tracker-basic.html`- this is a basic tracker
`tracker`- the more advanced tracker
`map-tracker.html`- a live UV map
`banner.html`- not part of the app, but open it for a surprise!

#  navigation
### Home Page
Welcome to the homepage of SunSmart!<br> 
this is where you can get UV information, and a little introductory video about UV
<img width="1875" height="975" alt="image" src="https://github.com/user-attachments/assets/cc5f46d0-f99b-4f8b-85a7-8224993c7e2a" />

### tracker basic
This is the simplest tracker in the app! <br>
It's use is simple: 
    <li>First, enter the city you wold like to see UV information about</li>
    <li> Second, if the city is wrong, choose the correct city in the drop-down menu. </li></li>
    <li>Finally, see the city's UV!! (bonus point- click check the code to see how the computer procecssed the data to get the UV)</li>
    <img width="1873" height="982" alt="image" src="https://github.com/user-attachments/assets/f36c5732-49e2-405e-b829-81a81e36a88a" />

    
### tracker
This is the most thorough UV tracker!! <br>
To use it, search for your city, then choose your skin sensitivity, skin tone, activity, and time outside. <br>

You can select your skin tone manually or estimate it using a camera or photo. Image processing happens on your device, and lighting can affect the estimate.<br>

The tracker displays a protection plan based on your choices. <br>
<img width="1863" height="962" alt="image" src="https://github.com/user-attachments/assets/3e0cd433-82c3-4af9-89be-4037551f166a" />
<img width="1867" height="982" alt="image" src="https://github.com/user-attachments/assets/281d5c02-4ade-4029-a615-3e2a91ea3ae9" />


### map tracker

Search for a place (even an address), move the map, or use your location. The tracker shows the place name, the nearest hourly UV forecast, local time, and protection tips.
<img width="1868" height="987" alt="image" src="https://github.com/user-attachments/assets/9e2f2cbd-1726-4268-af85-ec201a9bb0ff" />

# built with

HTML, CSS, JavaScript, and Python.

# apis

- open-meteo geocoding: finds cities and their coordinates.
- open-meteo forecast: provides UV information.
- nominatim: finds places and names locations on the map.
- OpenStreetMap: supplies the map images.
- leaflet: displays the interactive map.

### NOTES
Uses open-meteo api to find UV:
with name of city
10 results
lnguage
format
time there

OpenStreetMap- image pieces downloaded to draw the map background
