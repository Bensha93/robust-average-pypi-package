# Publishing Guide

This document explains how to publish new versions of the `robust-average` package to PyPI.

## Prerequisites

1. **PyPI Account**: Create an account at https://pypi.org/account/register/
2. **API Token**: Generate an API token at https://pypi.org/manage/account/token/
3. **Build Tools**: Install required tools:
   ```bash
   pip install build twine
   ```

## Publishing Steps

### 1. Update Version
Edit `pyproject.toml` and increment the version number:
```toml
version = "0.1.5"  # Change this
```

### 2. Build Package
```bash
python -m build
```

### 3. Check Package
```bash
twine check dist/*
```

### 4. Upload to PyPI
```bash
# Set your API token as environment variable
$env:TWINE_USERNAME="__token__"
$env:TWINE_PASSWORD="your-api-token-here"
twine upload dist/*
```

## Security Notes

- **Never commit API tokens** to version control
- **Use environment variables** for authentication
- **Test on TestPyPI first** if needed:
  ```bash
  twine upload --repository testpypi dist/*
  ```

## Alternative: Trusted Publishers

For automated publishing, consider using PyPI's Trusted Publishers:
1. Go to your package page on PyPI
2. Click "Manage" → "Publishing"
3. Set up GitHub Actions or other CI/CD

## Package Structure

```
robust-average-public/
├── robust_average/
│   ├── __init__.py
│   ├── robust_average.py
│   └── README.md
├── pyproject.toml
├── setup.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── example.py
└── test_robust_average.py
```

## Verification

After publishing, verify the package works:
```bash
pip install robust-average
python -c "from robust_average import robust_average; print(robust_average([1,2,3,4,5]))"
``` 