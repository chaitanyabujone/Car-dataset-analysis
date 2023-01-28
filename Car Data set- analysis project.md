```python
import pandas as pd
```


```python
car =pd.read_csv(r"C:\Users\Chaitanya\Downloads\Cars Data1.csv")
```


```python
#  Always Analyze data first
# .head() command shows first N rows of data (by default t shows 5) 
car.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Make</th>
      <th>Model</th>
      <th>Type</th>
      <th>Origin</th>
      <th>DriveTrain</th>
      <th>MSRP</th>
      <th>Invoice</th>
      <th>EngineSize</th>
      <th>Cylinders</th>
      <th>Horsepower</th>
      <th>MPG_City</th>
      <th>MPG_Highway</th>
      <th>Weight</th>
      <th>Wheelbase</th>
      <th>Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Acura</td>
      <td>MDX</td>
      <td>SUV</td>
      <td>Asia</td>
      <td>All</td>
      <td>$36,945</td>
      <td>$33,337</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>265</td>
      <td>17</td>
      <td>23</td>
      <td>4451</td>
      <td>106</td>
      <td>189</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Acura</td>
      <td>RSX Type S 2dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$23,820</td>
      <td>$21,761</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>200</td>
      <td>24</td>
      <td>31</td>
      <td>2778</td>
      <td>101</td>
      <td>172</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Acura</td>
      <td>TSX 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$26,990</td>
      <td>$24,647</td>
      <td>2.4</td>
      <td>4.0</td>
      <td>200</td>
      <td>22</td>
      <td>29</td>
      <td>3230</td>
      <td>105</td>
      <td>183</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Acura</td>
      <td>TL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$33,195</td>
      <td>$30,299</td>
      <td>3.2</td>
      <td>6.0</td>
      <td>270</td>
      <td>20</td>
      <td>28</td>
      <td>3575</td>
      <td>108</td>
      <td>186</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Acura</td>
      <td>3.5 RL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$43,755</td>
      <td>$39,014</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>225</td>
      <td>18</td>
      <td>24</td>
      <td>3880</td>
      <td>115</td>
      <td>197</td>
    </tr>
  </tbody>
</table>
</div>




```python
#shape - It shows the total no. of rows and no. of columns of the dataframe
car.shape
```




    (428, 15)




```python
#Now check if there are any Null values in dataset (If there is any null value in any column,then fill it with mean of that column.)
car.isnull().sum()
```




    Make           0
    Model          0
    Type           0
    Origin         0
    DriveTrain     0
    MSRP           0
    Invoice        0
    EngineSize     0
    Cylinders      2
    Horsepower     0
    MPG_City       0
    MPG_Highway    0
    Weight         0
    Wheelbase      0
    Length         0
    dtype: int64




```python
#fillna() - To fill the null values of a column with some particular value. For cylinders we will fill null valules wth mean
car['Cylinders'].fillna(car['Cylinders'].mean(), inplace=True)
```


```python
car.isnull().sum()
```




    Make           0
    Model          0
    Type           0
    Origin         0
    DriveTrain     0
    MSRP           0
    Invoice        0
    EngineSize     0
    Cylinders      0
    Horsepower     0
    MPG_City       0
    MPG_Highway    0
    Weight         0
    Wheelbase      0
    Length         0
    dtype: int64




```python
# Check what are the different types of Make are there in our dataset. And, what is the count of each Make in the data?
car['Make'].value_counts()
```




    Toyota           28
    Chevrolet        27
    Mercedes-Benz    26
    Ford             23
    BMW              20
    Audi             19
    Honda            17
    Nissan           17
    Volkswagen       15
    Chrysler         15
    Dodge            13
    Mitsubishi       13
    Volvo            12
    Jaguar           12
    Hyundai          12
    Subaru           11
    Pontiac          11
    Mazda            11
    Lexus            11
    Kia              11
    Buick             9
    Mercury           9
    Lincoln           9
    Saturn            8
    Cadillac          8
    Suzuki            8
    Infiniti          8
    GMC               8
    Acura             7
    Porsche           7
    Saab              7
    Land Rover        3
    Oldsmobile        3
    Jeep              3
    Scion             2
    Isuzu             2
    MINI              2
    Hummer            1
    Name: Make, dtype: int64




```python
#Show all the records where Origin is Asia or Europe.
car[car['Origin'].isin(['Asia','Europe'])]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Make</th>
      <th>Model</th>
      <th>Type</th>
      <th>Origin</th>
      <th>DriveTrain</th>
      <th>MSRP</th>
      <th>Invoice</th>
      <th>EngineSize</th>
      <th>Cylinders</th>
      <th>Horsepower</th>
      <th>MPG_City</th>
      <th>MPG_Highway</th>
      <th>Weight</th>
      <th>Wheelbase</th>
      <th>Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Acura</td>
      <td>MDX</td>
      <td>SUV</td>
      <td>Asia</td>
      <td>All</td>
      <td>$36,945</td>
      <td>$33,337</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>265</td>
      <td>17</td>
      <td>23</td>
      <td>4451</td>
      <td>106</td>
      <td>189</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Acura</td>
      <td>RSX Type S 2dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$23,820</td>
      <td>$21,761</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>200</td>
      <td>24</td>
      <td>31</td>
      <td>2778</td>
      <td>101</td>
      <td>172</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Acura</td>
      <td>TSX 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$26,990</td>
      <td>$24,647</td>
      <td>2.4</td>
      <td>4.0</td>
      <td>200</td>
      <td>22</td>
      <td>29</td>
      <td>3230</td>
      <td>105</td>
      <td>183</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Acura</td>
      <td>TL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$33,195</td>
      <td>$30,299</td>
      <td>3.2</td>
      <td>6.0</td>
      <td>270</td>
      <td>20</td>
      <td>28</td>
      <td>3575</td>
      <td>108</td>
      <td>186</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Acura</td>
      <td>3.5 RL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$43,755</td>
      <td>$39,014</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>225</td>
      <td>18</td>
      <td>24</td>
      <td>3880</td>
      <td>115</td>
      <td>197</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>423</th>
      <td>Volvo</td>
      <td>C70 LPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$40,565</td>
      <td>$38,203</td>
      <td>2.4</td>
      <td>5.0</td>
      <td>197</td>
      <td>21</td>
      <td>28</td>
      <td>3450</td>
      <td>105</td>
      <td>186</td>
    </tr>
    <tr>
      <th>424</th>
      <td>Volvo</td>
      <td>C70 HPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$42,565</td>
      <td>$40,083</td>
      <td>2.3</td>
      <td>5.0</td>
      <td>242</td>
      <td>20</td>
      <td>26</td>
      <td>3450</td>
      <td>105</td>
      <td>186</td>
    </tr>
    <tr>
      <th>425</th>
      <td>Volvo</td>
      <td>S80 T6 4dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$45,210</td>
      <td>$42,573</td>
      <td>2.9</td>
      <td>6.0</td>
      <td>268</td>
      <td>19</td>
      <td>26</td>
      <td>3653</td>
      <td>110</td>
      <td>190</td>
    </tr>
    <tr>
      <th>426</th>
      <td>Volvo</td>
      <td>V40</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$26,135</td>
      <td>$24,641</td>
      <td>1.9</td>
      <td>4.0</td>
      <td>170</td>
      <td>22</td>
      <td>29</td>
      <td>2822</td>
      <td>101</td>
      <td>180</td>
    </tr>
    <tr>
      <th>427</th>
      <td>Volvo</td>
      <td>XC70</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>All</td>
      <td>$35,145</td>
      <td>$33,112</td>
      <td>2.5</td>
      <td>5.0</td>
      <td>208</td>
      <td>20</td>
      <td>27</td>
      <td>3823</td>
      <td>109</td>
      <td>186</td>
    </tr>
  </tbody>
</table>
<p>281 rows × 15 columns</p>
</div>




```python
#Removing unwanted records - Remove all the records (rows) where Weight is above 4000.
car[~(car['Weight']> 4000)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Make</th>
      <th>Model</th>
      <th>Type</th>
      <th>Origin</th>
      <th>DriveTrain</th>
      <th>MSRP</th>
      <th>Invoice</th>
      <th>EngineSize</th>
      <th>Cylinders</th>
      <th>Horsepower</th>
      <th>MPG_City</th>
      <th>MPG_Highway</th>
      <th>Weight</th>
      <th>Wheelbase</th>
      <th>Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Acura</td>
      <td>RSX Type S 2dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$23,820</td>
      <td>$21,761</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>200</td>
      <td>24</td>
      <td>31</td>
      <td>2778</td>
      <td>101</td>
      <td>172</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Acura</td>
      <td>TSX 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$26,990</td>
      <td>$24,647</td>
      <td>2.4</td>
      <td>4.0</td>
      <td>200</td>
      <td>22</td>
      <td>29</td>
      <td>3230</td>
      <td>105</td>
      <td>183</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Acura</td>
      <td>TL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$33,195</td>
      <td>$30,299</td>
      <td>3.2</td>
      <td>6.0</td>
      <td>270</td>
      <td>20</td>
      <td>28</td>
      <td>3575</td>
      <td>108</td>
      <td>186</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Acura</td>
      <td>3.5 RL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$43,755</td>
      <td>$39,014</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>225</td>
      <td>18</td>
      <td>24</td>
      <td>3880</td>
      <td>115</td>
      <td>197</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Acura</td>
      <td>3.5 RL w/Navigation 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$46,100</td>
      <td>$41,100</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>225</td>
      <td>18</td>
      <td>24</td>
      <td>3893</td>
      <td>115</td>
      <td>197</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>423</th>
      <td>Volvo</td>
      <td>C70 LPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$40,565</td>
      <td>$38,203</td>
      <td>2.4</td>
      <td>5.0</td>
      <td>197</td>
      <td>21</td>
      <td>28</td>
      <td>3450</td>
      <td>105</td>
      <td>186</td>
    </tr>
    <tr>
      <th>424</th>
      <td>Volvo</td>
      <td>C70 HPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$42,565</td>
      <td>$40,083</td>
      <td>2.3</td>
      <td>5.0</td>
      <td>242</td>
      <td>20</td>
      <td>26</td>
      <td>3450</td>
      <td>105</td>
      <td>186</td>
    </tr>
    <tr>
      <th>425</th>
      <td>Volvo</td>
      <td>S80 T6 4dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$45,210</td>
      <td>$42,573</td>
      <td>2.9</td>
      <td>6.0</td>
      <td>268</td>
      <td>19</td>
      <td>26</td>
      <td>3653</td>
      <td>110</td>
      <td>190</td>
    </tr>
    <tr>
      <th>426</th>
      <td>Volvo</td>
      <td>V40</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$26,135</td>
      <td>$24,641</td>
      <td>1.9</td>
      <td>4.0</td>
      <td>170</td>
      <td>22</td>
      <td>29</td>
      <td>2822</td>
      <td>101</td>
      <td>180</td>
    </tr>
    <tr>
      <th>427</th>
      <td>Volvo</td>
      <td>XC70</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>All</td>
      <td>$35,145</td>
      <td>$33,112</td>
      <td>2.5</td>
      <td>5.0</td>
      <td>208</td>
      <td>20</td>
      <td>27</td>
      <td>3823</td>
      <td>109</td>
      <td>186</td>
    </tr>
  </tbody>
</table>
<p>325 rows × 15 columns</p>
</div>




```python
#Instruction ( Applying function on a column ) - Increase all the values of 'MPG_City' column by 3.
car['MPG_City']=car['MPG_City'].apply(lambda x:x+3)
```


```python
car
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Make</th>
      <th>Model</th>
      <th>Type</th>
      <th>Origin</th>
      <th>DriveTrain</th>
      <th>MSRP</th>
      <th>Invoice</th>
      <th>EngineSize</th>
      <th>Cylinders</th>
      <th>Horsepower</th>
      <th>MPG_City</th>
      <th>MPG_Highway</th>
      <th>Weight</th>
      <th>Wheelbase</th>
      <th>Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Acura</td>
      <td>MDX</td>
      <td>SUV</td>
      <td>Asia</td>
      <td>All</td>
      <td>$36,945</td>
      <td>$33,337</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>265</td>
      <td>20</td>
      <td>23</td>
      <td>4451</td>
      <td>106</td>
      <td>189</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Acura</td>
      <td>RSX Type S 2dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$23,820</td>
      <td>$21,761</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>200</td>
      <td>27</td>
      <td>31</td>
      <td>2778</td>
      <td>101</td>
      <td>172</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Acura</td>
      <td>TSX 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$26,990</td>
      <td>$24,647</td>
      <td>2.4</td>
      <td>4.0</td>
      <td>200</td>
      <td>25</td>
      <td>29</td>
      <td>3230</td>
      <td>105</td>
      <td>183</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Acura</td>
      <td>TL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$33,195</td>
      <td>$30,299</td>
      <td>3.2</td>
      <td>6.0</td>
      <td>270</td>
      <td>23</td>
      <td>28</td>
      <td>3575</td>
      <td>108</td>
      <td>186</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Acura</td>
      <td>3.5 RL 4dr</td>
      <td>Sedan</td>
      <td>Asia</td>
      <td>Front</td>
      <td>$43,755</td>
      <td>$39,014</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>225</td>
      <td>21</td>
      <td>24</td>
      <td>3880</td>
      <td>115</td>
      <td>197</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>423</th>
      <td>Volvo</td>
      <td>C70 LPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$40,565</td>
      <td>$38,203</td>
      <td>2.4</td>
      <td>5.0</td>
      <td>197</td>
      <td>24</td>
      <td>28</td>
      <td>3450</td>
      <td>105</td>
      <td>186</td>
    </tr>
    <tr>
      <th>424</th>
      <td>Volvo</td>
      <td>C70 HPT convertible 2dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$42,565</td>
      <td>$40,083</td>
      <td>2.3</td>
      <td>5.0</td>
      <td>242</td>
      <td>23</td>
      <td>26</td>
      <td>3450</td>
      <td>105</td>
      <td>186</td>
    </tr>
    <tr>
      <th>425</th>
      <td>Volvo</td>
      <td>S80 T6 4dr</td>
      <td>Sedan</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$45,210</td>
      <td>$42,573</td>
      <td>2.9</td>
      <td>6.0</td>
      <td>268</td>
      <td>22</td>
      <td>26</td>
      <td>3653</td>
      <td>110</td>
      <td>190</td>
    </tr>
    <tr>
      <th>426</th>
      <td>Volvo</td>
      <td>V40</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>Front</td>
      <td>$26,135</td>
      <td>$24,641</td>
      <td>1.9</td>
      <td>4.0</td>
      <td>170</td>
      <td>25</td>
      <td>29</td>
      <td>2822</td>
      <td>101</td>
      <td>180</td>
    </tr>
    <tr>
      <th>427</th>
      <td>Volvo</td>
      <td>XC70</td>
      <td>Wagon</td>
      <td>Europe</td>
      <td>All</td>
      <td>$35,145</td>
      <td>$33,112</td>
      <td>2.5</td>
      <td>5.0</td>
      <td>208</td>
      <td>23</td>
      <td>27</td>
      <td>3823</td>
      <td>109</td>
      <td>186</td>
    </tr>
  </tbody>
</table>
<p>428 rows × 15 columns</p>
</div>




```python

```
