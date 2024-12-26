# goit-core-hw-07 README

## Setup Instructions

### 1. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: .\venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Format Code

- **Run Black**:
  ```bash
  black .
  ```
- **Run isort**:
  ```bash
  isort .
  ```

### 4. Check Formatting

- **Black Check**:
  ```bash
  black --check .
  ```
- **isort Check**:
  ```bash
  isort --check-only .
  ```

### 5. Removing pycache

- **Run script**:
  ```
  find . -type d -name "__pycache__" -exec rm -r {} +
  ```
