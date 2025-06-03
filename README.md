# Learning Python

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

A collection of Python examples and exercises covering various programming concepts.

## Contents

### Asyncio
Advanced asyncio examples demonstrating asynchronous programming.

```python
import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

asyncio.run(main())
```
### Concurrency
Examples of concurrent programming patterns.

### Context Managers
Implementation using class-based and generator approaches.

### Data Analysis
Pandas and NumPy exercises for data manipulation.

### Dataclasses
Modern Python dataclass examples.

### Hash Tables
Implementation and usage examples.

### Regular Expressions
Pattern matching with ```re``` module.

### Requests
HTTP requests using ```requests``` library.

## Getting Started
```bash
git clone https://github.com/Noka993/learning-python.git
cd learning-python/<topic-folder>
python example.py
```
## Requirements
- Python 3.8+
- Jupyter Notebook (for notebooks)
- Packages listed in each topic's directory

## License

This project is licensed under the [MIT License](LICENSE).
