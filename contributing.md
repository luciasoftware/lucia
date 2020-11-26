# Contributing

Thanks for your interest in improving lucia.
In the attempt to maintain code clarity and format, each pull request is evaluated before being merged.
To make sure your changes are able to be used and valued by everyone, we ask that you read and abide by the following. Pull requests/issues that don't adhere to these specifications will receive a lower priority overall.

## I have a question

This repository is strictly for development. questions are best answered by [our audiogames.net topic](https://forum.audiogames.net/topic/31079/lucia-opensource-audiogame-engine-written-in-python/)

## something should be added/changed/modified/improved

All contributions start out as issues.
File one [right here](https://github.com/luciasoftware/lucia/issues)

If there's enough community interest, let us know you've taken it on and
feel free to begin writing code.

Make a pull request, siting the specific issue you intend to address.
All Pull Requests that don't have associated issues will subsequently be ignored.

### Contributing to documentation

One of the simplest ways to get started contributing to a project is through improving documentation. 
Lucia is constantly evolving, this means that sometimes our documentation has gaps. You can help by
adding missing sections, editing the existing content so it is more accessible or creating new content (tutorials, FAQs, etc).

Issues pertaining to the documentation are usually marked with the [Documentation](https://github.com/LuciaSoftware/lucia/labels/Documentation) label.


## Contributing code.

You will first need to clone the repository using `git` and place yourself in its directory:

```bash
$ git clone git@github.com:LuciaSoftware/lucia.git
$ cd lucia
```

> **Note:** We recommend that you use a personal [fork](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo) for this step. If you are new to GitHub collaboration,
> you can refer to the [Forking Projects Guide](https://guides.github.com/activities/forking/).

Now you need to install the dependencies for Lucia and make sure the tests pass on your machine:

```bash
$ poetry install
$ poetry run pytest
```

Lucia uses several tools including linters and code formatters to insure coding style and consistency through the codebase.
To insure that you don't accidentally commit code that does not conform to the coding style used, you can install a pre-commit hook that will check that everything is in order:

```bash
$ poetry run pre-commit install
```

You can also run it anytime using:

```bash
$ poetry run pre-commit run --all-files
```

Finally, to start coding, you can do the following to open the project in Visual Studio Code.

```bash
$ poetry shell
$ code .
```

Your code must be accompanied by corresponding tests where necessary, if tests are not present your code
will not be merged.
If your code adds new features to lucia, those features most be documented through docstrings.


## Something broke

In order to help us help you, try and provide as much information as possible so we can get to the bottom of the issue.
Along with including your error, the following is a list of questions that should be addressed in each issue labeled as a bugfix. Exclude as applicable.

* What were you trying to do?
* what happened?
* What did you expect to happen?
* Are you using the most up-to-date version of Lucia?
* Under what platform do you receive the issue?
* What version of said platform are you running?
* Do you have any idea what may be causing the problem and/or how it might be fixed?
* Anything else you think may assist us in addressing/solving the problem


### Thanks to:

* All our contributors.
* The guys over at [poetry](https://github.com/python-poetry/poetry) for inspiration for this contributing file.
