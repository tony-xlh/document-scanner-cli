# document-scanner-cli
Document Scanning Command Line for Windows, macOS and Linux.

## Windows (using WIA with Python)

```bash
python wia_scan.py -L #list scanners
python wia_scan.py -d "scanner name" -o put.png #scan with a scanner
```



## Linux (using SANE)

```bash
scanimage -L  #list scanners
scanimage -d "scanner name" -o put.png #scan with a scanner
```


