# covidtr - Covid Turkey Api

Covid Turkey Api

https://covidtr.herokuapp.com/


## Endpoints

- /

The endpoint returns the last result.

- /today

The endpoint returns the today's result. 

- /results

The endpoint returns all results.

## Rate Limits
- 1 request per 5 seconds
- 40 requests per 5 minutes

### Cache Timeout

The cache timeout is 5 minutes.



## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install covidtr.

```bash
pip install -r requirements.txt
```

## Usage

```python
gunicorn wsgi:app
```

## Testing
```bash
pip install -r tests/requirements.txt
pytest
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GPL v3](https://www.gnu.org/licenses/gpl-3.0.txt)