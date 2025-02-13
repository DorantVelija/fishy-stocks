# 🎣 Fishy Stocks – Because Your Goldfish is Smarter Than You  

Ever wondered if your pet goldfish has a knack for the stock market? Well, wonder no more! **Fishy Stocks** lets your fish pick stocks based on which side of the tank they prefer. Because why trust Wall Street when you have *Mr. Bubbles*? Inspo Michael Reeves 

## 🐠 How it Works  

1. The program fetches two random stocks from the **S&P 500**.  
2. The fish swims. The camera tracks its movement.  
3. Whichever side the fish spends more time on? BOOM. That's the stock it "buys."  
4. The transaction is logged in a CSV file for future *fish-ancial* analysis.  

## 📂 What's in the Box?  

- `logic.py` – Handles the stock selection logic (seriously, it’s random).  
- `stock_api.py` – Talks to Yahoo Finance so your fish can trade like a pro.  
- `save_bought_stocks.py` – Logs stock picks because *data science*.  
- `video.py` – Tracks your fish with **OpenCV**.  
- `snp500.json` – List of stocks in the S&P500.  
- `stocks_bought.csv` – A record of your fish’s legendary (or tragic) investments.  
- `requirements.txt` – So you don’t rage over missing dependencies.  

## 🛠 Setup  

1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
    ```    
2.	Make sure your camera of choice is working (your fish is the trader, not you).
3.	Run the script and let the magic happen:

### 📊 Sample CSV Output  

Every time the fish makes a trade, the data is logged in `stocks_bought.csv` like this:

| Symbol | Short Name     | Price Bought | Industry   | Date       | Stock Owned |
|--------|--------------|--------------|------------|------------|--------------|
| AAPL   | Apple Inc.    | 184.32       | Technology | 2025-02-13 | 0.0542       |
| GOOGL  | Alphabet Inc. | 151.76       | Technology | 2025-02-13 | 0.0659       |
| MSFT   | Microsoft Corp. | 398.45    | Technology | 2025-02-14 | 0.0251       |

## 🚨 A few important notes:
- This project is adjusted to track GOLDFISH movements, in order to track any other colour of fish, the bounds will need to be changed.
- I will post the results of my fishy stocks and their detailed performance in the future. 
- Not fish-ancial advice.

## 📊 Live Demo  

Check out the madness in action:  
[![Fishy Stocks Demo](https://img.youtube.com/vi/GMwkam-gtKg/0.jpg)](https://youtu.be/GMwkam-gtKg?si=MbKtkWoet21IuI1d)  



## 🔮 Can a Goldfish Predict the Market?  

Probably not, but it’s got about the same success rate as some hedge funds. Try it out and see if your fish is the next Warren Buffett!  

🐟💸 **Happy Trading!**
 