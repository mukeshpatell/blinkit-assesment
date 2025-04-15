# blinkit-assesment : TASK--1
# SQL

### Prerequisites

- SQL Installed in system

### Installation

1. **Create Tables:**

   ```bash
   CREATE TABLE blinkit_categories (
    l1_category NVARCHAR(255),
    l1_category_id INT,
    l2_category NVARCHAR(255),
    l2_category_id INT
    );
    ```
    ```bash
    CREATE TABLE blinkit_city_map (
    store_id INT,
    city_name NVARCHAR(255)
    );
    ```

    ```bash
    CREATE TABLE all_blinkit_category_scraping_stream (
    created_at DATETIME,
    l1_category_id INT,
    l2_category_id INT,
    store_id INT,
    sku_id INT,
    sku_name NVARCHAR(255),
    selling_price FLOAT,
    mrp FLOAT,
    inventory INT,
    image_url NVARCHAR(500),
    brand_id INT,
    brand NVARCHAR(255),
    unit NVARCHAR(50)
    );
    ```

2. **Insert Records from csv into table:**
    ```bash
    LOAD DATA INFILE '/var/lib/mysql-files/blinkit_categories.csv' 
    INTO TABLE blinkit_categories 
    FIELDS TERMINATED BY ','  
    ENCLOSED BY '"'  
    LINES TERMINATED BY '\n' 
    IGNORE 1 ROWS;
    ```

    ```bash
    LOAD DATA INFILE '/var/lib/mysql-files/blinkit_city_map.csv'
    INTO TABLE blinkit_city_map
    FIELDS TERMINATED BY ',' 
    ENCLOSED BY '"' 
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;
    ```

    ```bash
    LOAD DATA INFILE '/var/lib/mysql-files/all_blinkit_category_scraping_stream.csv'
    INTO TABLE all_blinkit_category_scraping_stream
    FIELDS TERMINATED BY ',' 
    ENCLOSED BY '"' 
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;
    ```

3. **Perform Analysis and create blinkit_city_insights.csv**
    ```bash
    'Execute the query from sql_operations.txt'