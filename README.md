## Como rodar?

```python
python main.py
```

## Como criar o binário

```python
pyinstaller --paths=src/ -F --add-data=data/entries.json:./data/entries.json src/main.py
```
