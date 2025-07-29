# document-scanner-cli
Document Scanning Command Line for Windows, macOS and Linux.

## Windows

1. Use TWAIN.

   ```bash
   python twain_scan.py -L #list scanners
   python twain_scan.py -d "scanner name" -o put.png #scan with a scanner
   ```

2. Use WIA.

   ```bash
   python wia_scan.py -L #list scanners
   python wia_scan.py -d "scanner name" -o put.png #scan with a scanner
   ```


## Linux

Use SANE:

```bash
scanimage -L  #list scanners
scanimage -d "scanner name" -o put.png #scan with a scanner
```


