![image](https://github.com/user-attachments/assets/d368343f-b36d-4505-9b61-a175b746727e)# NIFTY-GOLD_Price_EDA
This project performs an exhaustive statistical analysis between NIFTY-50 and Gold Prices from FY-16 till FY-22

1. The initial aim for this project is to co-relate the price fluctuation between NIFTY-50 and gold.

First we do an inital co-relation between the NIFTY-day Close price and Gold Price daily.

![alt text](image.png)

- From the above diagram it is evident that gold is positively correlated with NIFTY-50 Index, that means if NIFTY increases then gold prices increases as well but not as much, but when NIFTY decreases gold prices do take the hit but stay relatively stable.

2. Then we try to plot the time series data plot for both the asset classes to see the trend between the data.

![image](https://github.com/user-attachments/assets/dbb2b453-3ceb-4645-b88e-6502c50cde77)

From the above image it is clear that when NIFTY is about to break-even with gold from a Bullish run then investing in gold might lead to substantial gains during a bearish market trend.

3. Next we try to observe the seasonality pattern for Gold vs NIFTY during FY16-FY22

- For this analysis we use a daily percentage_change to observe the daily returns and then calculate a 30-day rolling correlation between the returns of both the asset classes.

![image](https://github.com/user-attachments/assets/379f3324-668f-4644-88ed-46a8a4356413)

From the above analysis it shows that gold prices correct atleast 3 times a year, but if we see the daily percentage change gold is less volatile than NIFTY-50

![image](https://github.com/user-attachments/assets/8065ca75-3195-4ae2-a81d-e11ab89081b1)

4. Then we perform a Granger Causality Test on the two asset classes.

- The Granger causality test is a statistical method used to determine if one time series can be used to predict another, meaning that past values of one variable can help predict future values of another, but not vice versa. It's a way to assess potential causal relationships between variables in time series data.  
  - We assume a max_lag of 5
 
![image](https://github.com/user-attachments/assets/d8f14160-bd09-4363-871b-12032193417c)

Granger analysis shows us that the asset classes are not directly following a linked pattern among themselves; rather they are related to each other by certain market regime's like( Bearish, Bullish)

5. That's why we perform a Regime analysis to show how the asset classes behave in different market regime's

- In statistics, regime analysis, also known as regime switching or regime-switching models, examines time series data that may exhibit different behaviors or "regimes" over time, acknowledging that the statistical properties of the data can change.
- Broadly there is two market regime's
  - Bullish (When Equity markets like NIFTY are on the rise)
  - Bearish (When Equity markets like NIFTY are on the fall or as we call it market correction)
  - Finally we see a neutral regime when the market consolidates.

![image](https://github.com/user-attachments/assets/c711e537-ad67-4195-8575-06153b089a3b)
From the above analysis we can see that the volatility of gold is less, and gold almost never gives a negative return even during the worst NIFTY returns phase.

![image](https://github.com/user-attachments/assets/97ab7ae0-1450-49dc-a075-c28319307b0d)




