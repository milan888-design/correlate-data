--sum scale query on testgraphquery db
WITH temp2 as
(
select order_type,sum(cast(quantity as numeric(10,1))) as ordertypesum
 from 
 sales_order
	group by order_type
	),
temp2_minmaxrange as
(
SELECT cast(min(ordertypesum) as numeric(10,1)) as min
	,cast(max(ordertypesum) as numeric(10,1)) as max
	,cast(max(ordertypesum)-min(ordertypesum) as numeric(10,1)) as range
	FROM temp2
	) 
select 
	temp2.order_type,temp2.ordertypesum
--,cast((temp2.ordertypesum-temp2_minmaxrange.min)*100/temp2_minmaxrange.range as numeric(10,1))  as rank
	,temp2_minmaxrange.min,temp2_minmaxrange.max,temp2_minmaxrange.range  
 from 
	temp2_minmaxrange, temp2