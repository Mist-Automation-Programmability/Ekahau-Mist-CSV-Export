# Ekahau-Mist-CSV-Export
Ekahau to Mist CSV export

### Objective:
This script is designed to take a predicted/simulated Ekahau file and output the CSV with the AP names needed to populate the Mist Ekahau import.  You will still need to populate the MAC Address, but this gives you the CSV structure and the names of the APs defined in Ekahau.

### Requirements:

#### Python 3:
For a multitude of reason, I have opted to make this Python3 only.  A lot has to do with the cross-platform behavior with csv.Dictwriter and how windows handles line termination in Python2.

#### Ekahau:
This is only tested in Ekahau Pro 10.2+.
You should also only have predicted/simulated APs in this file.

### Usage:
```
usage:
python ekahau_mist_csv.py -i INPUTFILE -o OUTPUTFILE

example:
python ./ekahau_mist_csv.py -i TestEkahauFile.esx -o TestEkahauFile.csv

Results:
Vendor AP Name,AP MAC Address
AP-01,
AP-02,
AP-03,
...
```





