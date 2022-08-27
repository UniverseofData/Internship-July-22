# Here I have uploaded the jypiter notbook where data cleaning processed on raw data before application deployment.
> **Step-1**
    Necessary liabaries for data preprocessing imported namely
    Pandas liabary for **data wrangling**
    Numpy libary for **mathametical operaions**
    
> **Step-2**
    imported the raw datafile using pd.read_csv('open_pubs') command as data stored in comma seperated values format.
    
> **Step-3**
    Data shape checked using df.shape
    Here we having 9 no. of features and 51330 records(rows).

> **Step-4**
    Checked the null values if any available in our raw dataset
    almost **767** no. of fields data was missing for **two features** namely '**latitude**' and '**longitude**'
    using the **drop.na**command we drop both the features which are not playing vital role in our dataset, and if we       tried to filled these blank details using mode command it may hamper our model acuracy , so its better to drop         these features. 
    
> **Step-5**
    Here after cleaning the data we once again check the datashape to know the revised / updated data size after data       cleaning.
    Now we having 9 mo. of features and 50,563 no. of records.
    
> **Step-6**
    Here we will save the clean data in csv file as clean_open_pub_data.
