# Install
For install turkish-name-gen package use:

```shell
$ pip install turkish-name-generator
```

Note: add `--user` if you get user error

# Usage
0. Import Module

```python
import trnamegen
```

1. Generate Random Names
```python
import trnamegen as trn

# randomName() function returns name with surname.

randomName = trn.randomName() # If you won't send any arguments there will no gender selection. Default is 0.
print("Random Name:", randomName)
randomWomanName = trn.randomName(2)
print("Random Woman Name:", randomWomanName)
randomManName = trn.randomName(1)
print("Random Man Name:", randomManName)
```

* Example Response
```shell
Random Name: Emir Yağcı
Random Woman Name: Melekşah Sucak
Random Man Name: Nejla Sertkayaoğlu
```

2. Generate Random First Names
```python
import trnamegen as trn

# firstName() function returns just name.

randomFirstName = trn.firstName() # If you won't send any arguments there will no gender selection. Default is 0.
print("Random Firstname:", randomFirstName)
randomWomanFirstName = trn.firstName(2)
print("Random Woman Firstname:", randomWomanFirstName)
randomManFirstName = trn.firstName(1)
print("Random Man Firstname:", randomManFirstName)
```

* Example Response
```shell
Random Firstname: Nazlı
Random Woman Firstname: Çağrınur
Random Man Firstname: Yağızalp
```

3. Generate Random Last Names
```python
import trnamegen as trn

# lastName() function returns just surname.

randomLastName = trn.lastName() # There is no gender selection here.
print("Random Lastname:", randomLastName)
```

* Example Response
```shell
Random Lastname: Yıldız
```