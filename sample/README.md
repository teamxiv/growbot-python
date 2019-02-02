# growbot-py sample

How to use:

- Make sure you have [pipenv](https://pipenv.readthedocs.io/en/latest/) (it's like pip and virtualenv combined. it's also the new standard.)
- `cd sample`
- `pipenv install` to install stuff from `sample/Pipfile` to a virtualenv
- Update the uuid and host in the sample if necessary
- `pipenv run python main.py` to run the sample
- Trigger the move somehow (manually send a POST request?)
- Observe the message being caught
