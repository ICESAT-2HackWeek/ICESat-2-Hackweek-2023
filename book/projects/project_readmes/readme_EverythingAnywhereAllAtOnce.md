# Everything, Anywhere, All At Once (EAAAO!)

## Team Members

The following people contributed to our project throughout the week:
* Project lead: [Shanshan ](url to their webpage)
* Project lead: [Adrian Marziliano](https://github.com/AdrianMarzil)
* Helper: [name of person](url to their webpage)
* Team member: [Romina Piunno](https://github.com/RomiP)
* Team member: [Michael Studinger](https://science.gsfc.nasa.gov/sed/bio/michael.studinger)
* Team member: [Zach Fair](url to their webpage)
* Team member: [Phillip Arndt](url to their webpage)
* Team member: [David Shean](url to their webpage)
* Team member: [Zheng Liu](https://github.com/liuzheng-arctic)


## Project Goals

Our team was motivated to resolve a common frustration among the ICESat-2 science community regarding the uncertainty of the satellite's flight paths and timing.
Our goal for the week was to design a simple Python script to help researchers more succesffuly plan their field site visits to align with ICESat-2 flyovers.


## Project Outcomes
We were successful in creating a (notebook/function?) which receives a user-input AOI, finds the potential ICESat-2 data points within a (25km?) radius of this AOI, and draws the three track lines (beam pairs) associated with these data points, and outputs an interactive map of these data points and tracks along with. The script also allows for this output to be saved as a GeoJSON file which can then be saved on a mobile device to allow for planning in the field.

Zheng Liu pitched this idea to the ICESat-2 Hackweek group on August 7, 2023.

The group completed tasks for this project as follows:
* Michael created a user interface that accepted a single latitude/longitude AOI point and created a circle polygon (radius: 25km)
* Phillip downloaded ICESat-2 time specific orbit (cycle) kml's from the 'Technical Specs' page (https://icesat-2.gsfc.nasa.gov/science/specs) and converted them to a geodataframe
* Adrian (under Phillip's guidance) clipped the orbit geodataframe using the AOI circle polygon
* Zachary drew the beam pairs for the clipped 
* Shanshan created the interactive map output to display the beam pairs, AOI, and time stamps for the user-input latitude/longitude
* Romina synthesized these tasks into a single workflow and (notebook?) 
* David assisted in advising the group on designing a project framework, file formatting, processing efficiency, and 


## Files
Example:
* `.gitignore`
<br> Globally ignored files by `git` for the project.
* `environment.yml`
<br> `conda` environment description needed to run this project.
* `README.md`
<br> Description of the project. [Sample](https://geohackweek.github.io/wiki/github_project_management.html#project-guidelines)

## Folders

## Notebooks
Example: Links to relevant outputs are a great way to capture these outcomes, so long as the links are likely to remain valid for some time (this readme - with this list - will be archived as part of the Hackweek JupyterBook).
Some examples might be:
* [Example Workflow Jupyter Notebook](your notebook url here).
  

## Future Efforts

There are multiple ideas to improve upon this work to increase the effectiveness of ICESat-2 flight prediction.
There are currently no plans for this team to continue work on this project after the 2023 Hackweek, but we are open to suggestions and 

Have you built any great new collaborations you anticipate continuing after the Hackweek?
Is your team planning to keep meeting to continue hacking or draft a conference abstract or proposal?
Did you start doing some work that relates to your research and enables you to contribute to shared tools for working with ICESat-2 data products?
Please share your hopes and plans for the future here!
