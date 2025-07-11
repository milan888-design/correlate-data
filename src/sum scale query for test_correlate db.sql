--product_type	state	county_state	year sales_in_thousand
--='sales_by_county_state_year'
--state	county_state	year gdp_in_thousand
--'gdp_by_county_state_year'

--example test_correlate database
WITH temp2 as
 (select state,year,sum(cast(sales_in_thousand as numeric(10,1))) as sales_in_thousand
 from 
 sales_by_county_state_year
	group by state,year
	),
temp2_minmaxrange as
(
SELECT cast(min(sales_in_thousand) as numeric(10,1)) as min
	,cast(max(sales_in_thousand) as numeric(10,1)) as max
	,cast(max(sales_in_thousand)-min(sales_in_thousand) as numeric(10,1)) as range
	FROM temp2
	) 
select 
	temp2.state,temp2.year,temp2.sales_in_thousand
     ,cast((temp2.sales_in_thousand-temp2_minmaxrange.min)*100/temp2_minmaxrange.range as numeric(10,1))  as rank
	,temp2_minmaxrange.min,temp2_minmaxrange.max,temp2_minmaxrange.range  
 from 
	temp2_minmaxrange, temp2

--example test_correlate database
WITH temp2 as
 (select state,year,sum(cast(gdp_in_thousand as numeric(20,1))) as gdp_in_thousand
 from 
 gdp_by_county_state_year
	group by state,year
	),
temp2_minmaxrange as
(
SELECT cast(min(gdp_in_thousand) as numeric(20,1)) as min
	,cast(max(gdp_in_thousand) as numeric(20,1)) as max
	,cast(max(gdp_in_thousand)-min(gdp_in_thousand) as numeric(20,1)) as range
	FROM temp2
	) 
select 
	temp2.state,temp2.year,temp2.gdp_in_thousand
--cast((temp2.gdpsum-temp2_minmaxrange.min)*100/temp2_minmaxrange.range as numeric(10,1))  as rank
	,temp2_minmaxrange.min,temp2_minmaxrange.max,temp2_minmaxrange.range  
 from 
	temp2_minmaxrange, temp2

--sales table
SELECT 
 salessum.state
 ,salessum.year
 ,salessum.sales_in_thousand
  ,salessum.sales_in_thousand_scaled
  FROM sales_by_county_state_year_summary salessum

--gdp table
SELECT 
 gdpsum.state
 ,gdpsum.year
 ,gdpsum.gdp_in_thousand
  ,gdpsum.gdp_in_thousand_scaled
  FROM gdp_by_county_state_year_summary gdpsum

--join sales and gdp tables
SELECT 
 salessum.state
 ,salessum.year
 ,salessum.sales_in_thousand
  ,salessum.sales_in_thousand_scaled
   ,gdpsum.gdp_in_thousand
  ,gdpsum.gdp_in_thousand_scaled
  FROM sales_by_county_state_year_summary salessum
  ,gdp_by_county_state_year_summary gdpsum
   WHERE 
   salessum.state=gdpsum.state
    and salessum.year=gdpsum.year
