This is a small python cli app that calculates dollar-cost averaging investment strategy for crypto currencies.

DCA, is an investment strategy that reduces market risk by spreading out the purchase of a security over several smaller purchases.

It takes:
* Price information in CSV format
* Date range (begin and end)
* Amount to buy daily
* Amount to sell at

As a result it calculates the following outputs:
* How much money is invested (spent)
* Total coin bought (owned at end of period)
* How much money you would make if you sold at price
* How many times you've multiplied (or lost) your invested money

## Commands

You can run the script in the following way

`python3 src/main.py [command] [args]`

-----

To show all available coins use

`python3 src/main.py list`

-----

Example: To calculate DCA returns on Ether for a given range use

`python3 src/main.py dca Ethereum.csv 2018-10-01 2020-04-30 40 3000`
- This will tell you how much you would win (or lose) if you bought ether for 40\$ every day within the given date range and sold when 1 ether equals 3000\$

-----

To compare the exact same strategy as above but for Solana you would use:
`python3 src/main.py dca Solana.csv 2018-10-01 2020-04-30 40 220`
- Here you would buy for the exact same period and amount (\$40 a day) as the example above. And you would sell for the price of 220\$ a SOL.

## Data

It uses data downloaded from the internet, it's located under `top_coins_price_feed` folder.
The columns are: Date, Open, High, Low, Close, Volume, Currency

The feed starts when the coin has first started trading and ends on 2022-05-09

To use your own pricing feed you must support the same columns and 
drop the file in `top_coins_price_feed` folder. When running the `dca` command
just use your file name.

## Algorithm 

Coins bought for a day is calculated as ((H+L+C) / 3) / Amount_per_day
