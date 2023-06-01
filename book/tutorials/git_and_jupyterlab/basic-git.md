# Basic Git/GitHub Skills Using `jupyterlab-git`

```{admonition} Learning Objectives
- Set up Git in the JupyterHub using [First time `git` setup](../../preliminary/git)
- Learn how to use the `jupyterlab-git` GUI in JupyterLab
- Practice 4 basic Git/GitHub skills: cloning, committing, push/pull
```

```{important}
Before we go over this tutorial we expect that you have already gone through this preparation material:
- [JupyterHub login setup](../../preliminary/jupyterhub)
```

## What is Git and GitHub?

**Git** A program to track your file changes and create a history of those changes. Creates a 'container' for a set of files called a repository.

**GitHub** A website to host these repositories and allow you to sync local copies (on your computer) to the website. *Lots* of functionality built on top of this.

![](../../img/git-repo-structure.png){width=200px}

## Some basic Git jargon

* **Repo** Repository. It is your code and the record of your changes. This record and also the status of your repo is a hidden folder called `.git` . You have a local repo and a remote repo. The remote repo is on GitHub (for in our case) is called `origin`. The local repo is on the JupyterHub.
* **Stage** Tell Git which changes you want to commit (write to the repo history).
* **Commit** Write a note about what change the staged files and "commit" that note to the repository record. You are also tagging this state of the repo and you could go back to this state if you wanted.
* **Push** Push local changes (commits) up to the remote repository on GitHub (`origin`).
* **Pull** Pull changes on GitHub into the local repository on the JupyterHub.
* **Git GUIs** A graphical interface for Git (which is command line). Today I will use `jupyterlab-git` which we have installed on JupyterHub.
* **Shell** A terminal window where we can issue `git` commands.


## Overview

Today I will cover the four basic Git/GitHub skills. We will not work with branches today and I won't cover much about merge conflicts. The goal for today is to first get you comfortable with the basic skills and terminology---and also get you set up on the JupyterHub. We will use what is called a  "trunk-based workflow".

### Simple Trunk-based Workflow:

* Make local (on your computer) changes to code.
* Record what those changes were about and commit to the code change record (history).
* Push those changes to your remote repository (aka origin)

We'll do this

![](../../img/git-linear-flow-2.png)

## Setting up Git

Before we can work with Git in JupyterLab, we need to do some set up.

[First time `git` setup](../../preliminary/git)

1. Tell Git who you are and to store your credentials (GitHub login info)

[Show me](https://youtu.be/3CLuOCJMfK0)

2. Get a Personal Access Token from GitHub

Copy the token! You will need it in the next step.

[Show me](https://youtu.be/tkioJhF_gO8)

3. Trigger Git to ask for your password (that personal access token)

You will do this by cloning a private repo. Open a shell and issue this command

```shell
git clone https://github.com/snowex-hackweek/github_setup_check.git
```

It will ask for your GitHub username and password. At the password part, paste in the Personal Access Token.


## `jupyterlab-git`

When the instructions say to use or open or click on `jupyterlag-git`, click the icon in the left navbar marked by the red arrow.

![](../../img/jupyterlab-git.jpg)

## The Key Skills

* Skill 1: Create a blank repo on GitHub
* Skill 2: Clone your **GitHub** repo onto the JupyterHub
* Skill 0: Open your repository in the JupyterLab.
* Skill 3: Make some changes and commit those local changes
* Skill 4: Push the changes to GitHub

* Skill 1b: Fork someone else's GitHub repository

## Let's see it done!

### Skill 1: Create a blank repo on GitHub

1. Click the + in the upper left from YOUR GitHub page.
2. Give your repo the name `Test` and make sure it is public.
3. Click new and check checkbox to add the Readme file and `.gitignore`
4. Copy the URL of your new repo. It's in the browser where you normally see a URL.

[Show me](https://youtu.be/1uV_7iGVu3o)

### Skill 2: Clone your repo to the JupyterHub

1. Copy the URL of your repo. `https://www.github.com/yourname/Test`
2. Click on the `jupyterlab-git` icon in the left navbar.
3. You'll see 3 boxes<sup>*</sub>, click on Clone Repository.
3. Paste the URL from  in the box that pops up and paste in the URL from Step #1.
4. Your repo now appears in the list of folders.

[Show me](https://youtu.be/7HDheHE05jc) -- [Show me with the shell](https://youtu.be/GpYycSpwYQk) -- [Show me with Visual Studio Code](https://youtu.be/aMPGKMRjl8A)

* I don't see those boxes. You are in a repository. Click on the little folder icon at top to get out of the current folder. See video (at the end).


### Skill 3: Make some changes and commit your changes

1. Make some changes to the README.md file in the Test repo.
2. Click the `jupyterlab-git` icon, and stage the change(s) by rolling over the modified file and clicking the +.
2. Open GitHub Desktop, click the little checkboxes next to the changes.
3. Add a commit comment, click commit.

[Show me](https://youtu.be/2stgvvKer-k) -- [Show me from the shell](https://youtu.be/jXxWvjPYgDI) -- [Show me with Visual Studio Code](https://youtu.be/jMWvLk9iuFw)

### Skill 4: Push changes to GitHub / Pull changes from GitHub

To push changes you committed in Skill #3

1. From jupyterlab-git, click on the little cloud with up arrow at the top (it's kind of small).

[Show me](https://youtu.be/-D_Kk3ia36c) -- [Show me in the shell](https://youtu.be/XFdvHn_Q-1o)

To pull changes on GitHub that are not on your local computer:

1. Make some changes directly on GitHub
1. From jupyterlab-git, click on the little cloud with down arrow at the top (it's kind of small).

[Show me](https://youtu.be/XjsuaDHAAZg)

* Note in the shell, the command is `git pull`.

### Pair-activity 1

In JupyterLab,

1. Make a copy of README.md
2. Rename it to <youname>.md
3. Add some text.
4. Stage and commit the added file.
5. Push to GitHub.

Do this from `jupyterlab-git`. You can also try from the shell if you watched the shell videos too.

Try before watching. [Show me](https://youtu.be/ejmkkjWJ_Es) -- [Show me in the shell](https://youtu.be/tvmX41b5pTU)

### Pair-activity 2

All of this activity is in JupyterLab.

1. Clone this repo: https://github.com/snowex-hackweek/git-basics
2. Navigate to the repo, copy `Copyme.md` and rename to `<yourname>.md`
3. Stage and then commit that new file.
4. Push to GitHub.
5. Make some more changes and push to GitHub.
6. Pull in your partner's (and everyone elses) changes

[Show me](https://youtu.be/w0ub1hBZh70)

### Skill 1b: Fork a repo on GitHub

You can copy other people's repos but maintain a connection to the original (upstream) repo. In the hackweek, you will use this to get the tutorials and update them each morning.

1. In a browser, go to the GitHub repository you want to fork.
2. Click the little fork icon in the upper right corner.
3. Use Skill #1 to clone the forked repo to your computer.

Fetch changes from the original (upstream) using `jupyterlab-git`

1. From GitHub, click "Fetch upstream"
2. From JupyterLab, click on the `jupyterlab-git` icon and click the cloud with down arrow, to pull in the changes to JupyterLab.

Fetch changes from the original (upstream) using the shell

See instructions [here](jupyter)


### Skill 1c: Copy a repo on GitHub

You can copy your own or other people's repos^[This is different from forking. There is no connection to the original repository.].

1. In a browser, go to the GitHub repository you want to copy.
2. Copy its url.
3. Navigate to your GitHub page: click your icon in the upper right and then 'your repositories'
4. Click the `+` in top right and click `import repository`. Paste in the url and give your repo a name.
5. Use Skill #1 to clone your new repo to your computer

### Pair-activity 2

1. Fork https://github.com/snowex-hackweek/website2022 (GitHub)
2. Clone to JupyterHub (Skill #2)



