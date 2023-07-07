# Preliminary Work

Our hackweeks focus on applied, hands-on learning, with participants engaging in extended periods of small-group work. Our tutorials are designed to offer a broad snapshot of data science tools to support your applied investigations. We are different from a more traditional summer school in that we do not provide a comprehensive, in-depth training in fundamental tools. Rather, our goal is to inform you about the types of tools we think are best suited to working with your datasets, leaving details of implementation to be supported through peer-learning and office hours.

## Typical Workflows and Tools

Here are a few specific scenarios of how hackweek participants typically engage with data science tools during an event:

* Connecting to a [Jupyter Notebook](https://jupyter.org/) environment and using the command line to pull lesson content for a morning of tutorial training.
* Modifying a text file, committing it to Git and pushing changes to GitHub, for others on your team to view and edit.
* Opening CSV tabular data in Pandas and using filtering functions to remove outliers.
* Accessing a cloud-hosted remote sensing image using Rasterio and plotting it on an interactive map.
* Exploring multi-dimensional climate grids using xarray.

These are examples of the types of activities we do at a hackweek in a collaborative setting. We invite you to reflect on your comfort level with tasks such as these so that you can arrive at the hackweek with a clarity on where to dedicate your energy. If wish to focus more energy on learning and implementing new tools, we will support you with helpers and office hours, and you may have a bit less time for applied group work. If you are already proficient in a lot of tools you may find you can dedicate more energy to applied project work, which we support through facilitated group activities.

## {{hackweek}} Software Carpentry Session

We strongly suggest that participants who are just beginning to learn Python and collaborative data science tools to complete our recorded ([Software Carpentry Trailing](swc)) in advance of the hackweek. You may choose whichever topics you'd like to brush up on or learn. 

## Required setup

```{attention}
Please make sure to find some time to go through the below material before
the hackweek.

__Upon completion you__:
<div>
  <input type="checkbox" name="a1">
  <label for="a1">Joined the Slack workspace</label>
</div>
<div>
  <input type="checkbox" name="a2">
  <label for="a2">Created a EarthData Login</label>
</div>
<div>
  <input type="checkbox" name="a3">
  <label for="a3">Created a GitHub account</label>
</div>
<div>
  <input type="checkbox" name="a4">
  <label for="a4">Can login to the JupyterHub</label>
</div>
<div>
  <input type="checkbox" name="a5">
  <label for="a5">Setup the `git` command after logging into the JupyterHub</label>
</div>
```

### GitHub Account

Everyone attending {{ hackweek }} will require obtaining a GitHub account.
Visit our [GitHub instruction page](github) to learn how!

### Slack Account

All of our communication throughout the hackweek will be done using the
{{ '[`{hackweek}` Slack workspace]({url})'.format(hackweek=hackweek, url=slack_workspace_url)}}.
With your invite to the hackweek, you should also have received a separate
email to join the Slack workspace. Upon accepting the invite, please take a moment to
[complete your Slack profile](https://slack.com/help/articles/204092246-Edit-your-profile).
Having your name and picture with your Slack account helps us and your peers
to identify you on Slack and builds a more personal community throughout
the week.

### JupyterHub

We will offer all tutorials within the Jupyter Hub computing environment.
Visit our [Introduction to Jupyter Hub](jupyterhub) page to learn more!

### Git

All content of the hackweek will be shared via GitHub and interacting with the
website will be done via the `git` command.
Visit [Setting up the `git` command](git) to learn how to configure that!

### EarthData Login

We'll have you download some data from NSIDC for your tutorials and projects.
Visit our [Earthdata](earthdata) page to learn how to access and Earthdata
login account if you don't already have one!

## Supplemental Material

### Python

Dive deeper into how [Python is managed and installed](supplemental/python) on
the JupyterHub and how you can install that on your personal machine.

### Conda
A basic intro to manage Python environments using the
[conda package manager](supplemental/conda)
