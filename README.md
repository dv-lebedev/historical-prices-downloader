# quote-downloader
Little script to download historical prices from Google Finance.


Change 'main()' vars as you need and run script.

```python
def main():

    destination_path = os.getcwd() #directory for downloded files

    start_date = datetime(2012, 5, 1)
    end_date = datetime(2012, 6, 1)

    symbols = [
        'GOOG',
        'IBM',
        'JPM'
    ]

    download_all(symbols, start_date, end_date, destination_path)
```
