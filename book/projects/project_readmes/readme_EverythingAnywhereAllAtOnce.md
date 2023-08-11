# Everything, Anywhere, All At Once (EAAAO!)

## Team Members

The following people contributed to our project throughout the week:
* Project lead: [Shanshan Li](https://github.com/sophie8910)
* Project lead: [Adrian Marziliano](https://github.com/AdrianMarzil)
* Team member: [Romina Piunno](https://github.com/RomiP)
* Team member: [Michael Studinger](https://science.gsfc.nasa.gov/sed/bio/michael.studinger)
* Team member: [Zach Fair](https://github.com/zachghiaccio)
* Team member: [Philipp Arndt](https://github.com/fliphilipp)
* Team member: [David Shean](https://github.com/dshean)
* Team member: [Zheng Liu](https://github.com/liuzheng-arctic)

![example teaser image](https://raw.githubusercontent.com/fliphilipp/images/main/example_plot%20(1).jpg)

## Project Goals

Our team was motivated to resolve a common need among the ICESat-2 science community regarding the uncertainty of the satellite's flight paths and timing.
Our goal for the week was to design a simple Python script to help researchers better plan their field site visits to align with ICESat-2 flyovers.


## Project Outcomes
We were successful in creating a Python class which receives a user-input Area of Interest (AOI), finds the potential ICESat-2 data points within a specified radius of this AOI, and draws the three track lines (beam pairs) associated with these data points. The code outputs an interactive map of these data points and tracks overlayed onto the highlighted AOI. The script also allows for this output to be saved as a GeoJSON file which can then be saved on a mobile device to allow for planning in the field.

Zheng Liu pitched this idea to the ICESat-2 Hackweek group on August 7, 2023.

The group completed tasks for this project as follows:
* Michael created a user interface that accepted a single latitude/longitude AOI point and created a search polygon with a desired radius. Output is search polygon as GeoDataFrame and GeoJSON file.
* Philipp downloaded ICESat-2 time-specific orbit (cycle) KML's from the 'Technical Specs' page (https://icesat-2.gsfc.nasa.gov/science/specs) and converted them to a Geodataframe
* Adrian clipped the orbit Geodataframe using the AOI circle polygon
* Zachary drew the beam pairs for the clipped ground tracks
* Shanshan created the interactive map output to display the beam pairs, AOI, and time stamps for the user-input latitude/longitude
* Romina synthesized these tasks into a single workflow and designed the code's architecture
* David assisted in advising the group on designing a project framework, file formatting, and processing efficiency
* All team members offered peer support and guidance to each other

The project acted as a catalyst for learning about how ICESat-2 data are stored, how to process the data into useful frameworks, and software design. In developing this project, team members were able to experience first-hand the quirks and limitations of the data, but also brainstorm and develop new applications.

## Files
Example:
* `.gitignore`
<br> Globally ignored files by `git` for the project.
* `environment.yml`
<br> `conda` environment description needed to run this project.
* `README.md`
<br> Description of the project. [EverythingAnywhereAllAtOnce](https://github.com/ICESAT-2HackWeek/EverythingAnyWhereAllAtOnce)
* `main.ipynb`
<br> Where the class is defined. Also contains a sample use-case.

## Notebooks
Here is where we've stored individual contributions from each of our team members. This collection of rough work tells a story of exceptional problem-solving. These individual contributions were later compiled into one final Python class. 
  
## Future Efforts

There are multiple ideas to improve this work to increase the effectiveness of ICESat-2 flight prediction.
There are currently no plans for this team to continue work on this project after the 2023 Hackweek, but we are open to suggestions and future collaboration.

![whiteboard notes](https://raw.githubusercontent.com/fliphilipp/images/main/PXL_20230809_234808751.MP.jpg)
