# Contributing to POEI-Python-Rss

👍🎉 First off, thanks for taking the time to contribute! 🎉👍

## Table of Contents

- [Setting Up the project locally](#setting-up-the-project-locally)
- [Submitting a Pull Request](#submitting-a-pull-request)

## Setting Up the project locally

To run the project you need to have `python` and therefore `pip` already installed.

1. [Fork](https://help.github.com/articles/fork-a-repo/) the project, clone
    your fork:

    ```sh
    # Clone your fork
    git clone https://github.com/<your-username>/POEI-Python-Rss.git

    # Navigate to the newly cloned directory
    cd POEI-Python-Rss
    ```
    
2. Download all the python packages required.<br>You can do it from the requirements.txt file with `pip`:
    ```sh
    pip install -r requirements.txt --use-pep517 --user
    ```
    The --use-pep517 is required by sgmllib (a dependency of feedparser) and the --user is required by flask<br><br>

3. You are ready to Contribute to the project. <br>Folow `README.md` instructions on how to use it.

> Tip: Keep your `master` branch pointing at the original repository and make pull requests from branches on your fork. To do this, run:
>
> ```sh
> git remote add upstream https://github.com/Zenika/POEI-Python-Rss.git
> git fetch upstream
> git branch --set-upstream-to=upstream/master master
> ```
>
> This will add the original repository as a "remote" called "upstream," then fetch the git information from that remote, then set your local `master` branch to use the upstream master branch whenever you run `git pull`.<br>
> Then you can make all of your pull request branches based on this `master` branch.<br>
> Whenever you want to update your version of `master`, do a regular `git pull`.

## Submitting a Pull Request

Please go through existing issues and pull requests to check if somebody else is already working on it.

Also, make sure to run and test the code before you commit your changes.<br>
(joke on me, the project doesn't have any test for the moment)
