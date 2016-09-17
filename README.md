#### Done:
1. Used wget to get local page of https://en.wikipedia.org/wiki/Atlantic_hurricane_season
2. Parsed html file and wrote data into SQLite database 
 

#### Queries about the scraped data: 


```python
import sqlite3 as lite
conn = lite.connect('hurricanes.db')
cur = conn.cursor()
```

What year had the most tropical storms?


```python
cur.execute("SELECT year, MAX(tropical_storms) FROM atlantic_hurricanes ")
print cur.fetchone()
```

    (2005, 28)


What year had the most major hurricanes?


```python
cur.execute("SELECT year, MAX(major_hurricanes) FROM atlantic_hurricanes ")
print cur.fetchone()
```

    (1961, 7)


What year had the most deaths?


```python
cur.execute("SELECT year, MAX(deaths) FROM atlantic_hurricanes ")
print cur.fetchone()
```

    (1998, 12000)


What year had the most damage (not inflation adjusted)?


```python
cur.execute("SELECT year, MAX(damage)  FROM atlantic_hurricanes WHERE damage != 'N.A' ")
print cur.fetchone()
```

    (2005, 159000000000.0)


What year had the highest proportion of tropical storms turn into major hurricanes?


```python
cur.execute("SELECT year, MAX(major_hurricanes/tropical_storms) FROM atlantic_hurricanes WHERE tropical_storms != 0 ")
print cur.fetchone()
```

    (1860, 1)


#### Notes about data :


Defined the data type for these two columns as integers, making them comparable for the queries. 

Note about the value of "deaths": I noticed that non-numerical characters such as "+", "," and "~" in the values of deaths column, I decided to delete these characters, for example "200+" becomes "200", as "+" and "~" indicate an approximate estimate, so deleting them has a trivial effect on the later exploratory analysis of data. As to the "None", "Numerous", "Not Known" and "Unknown" values in this column, I converted them to integer zero so the data type for the deaths column will be integers.

Note about the value of "Damage": I converted the string values in the damage column to float numbers and delete the dollar sign, for example $410 million becomes 410000000.0. As to the missing data prior to 1900s, I added N.As to this column indicating that the data about damage is not available for these years. When doing the query, the data other than N.A are selected to come up with the year that has maximum value of damages. As to the "Unknown" value, I converted it to zero. Also I deleted the ">" sign for the same reason I provided for handling data of "deaths".

Note about the combination of "strongest storm", "Retired names" and "Notes" into a single column: I added the string data in the "strongest storm" and "Retired names" to the Notes column and seperated them with a comma.

