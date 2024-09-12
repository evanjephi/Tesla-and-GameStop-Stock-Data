#If you're using anaconda locally, install this
#!pip install yfinance==0.2.38
#!pip install pandas==2.2.2
#!pip install nbformat


!pip install yfinance
!pip install bs4
!pip install nbformat

import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#filterwarnings function to filter or ignore specific warning messages or categories
import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#Defining graph function
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

#Extract Tesla Data
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max") #Extract history stock information
tesla_data.reset_index(inplace=True)  #reset first five rows of tesla and gme dataframe

#using web scraping to extract tesla revenue data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url)

soup = BeautifulSoup(html_data.content, 'html.parser')
tables = soup.find_all('table') # Step 1
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"]) #Step 3
for table in tables: #Step 2
    if "Tesla Quarterly Revenue" in table.text:
        rows = table.find_all('tr') #Step 4

        for row in rows: 
            cols = row.find_all('td')
            if len(cols) == 2:
                date = cols[0].text.strip()
                revenue = cols[1].text.strip()
                
                revenue = revenue.replace('$', '').replace(',', '') #Step 5
                new_row = pd.DataFrame({"Date": [date], "Revenue": [revenue]})
                tesla_revenue = pd.concat([tesla_revenue, new_row], ignore_index=True)

revenue = revenue.replace('$', '').replace(',', '')
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

#display first and last five rows
print(tesla_revenue.head())
print(tesla_revenue.tail())

#Extract GameStop Data
ticker = yf.Ticker("GME")
gme_data = ticker.history(period="max")
gme_data.reset_index(inplace=True)

#using web scraping to extract tesla revenue data
url_2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data_2 = requests.get(url_2).text

soup_2 = BeautifulSoup(html_data_2, 'html.parser')

tables = soup_2.find_all('table')
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for table in tables:
    if "GameStop Quarterly Revenue" in table.text:
        rows = table.find_all('tr')
        for row in rows[1:]: 
            cols = row.find_all('td')
            if len(cols) == 2:  
                date = cols[0].text.strip()
                revenue = cols[1].text.strip()

                revenue = revenue.replace('$', '').replace(',', '')

                new_row = pd.DataFrame({"Date": [date], "Revenue": [revenue]})
                gme_revenue = pd.concat([gme_revenue, new_row], ignore_index=True)

gme_revenue = gme_revenue[gme_revenue['Revenue'] != '']

#display first and last five rows
print(tesla_revenue.head())
print(tesla_revenue.tail())

# Plot Stock Graph

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing=.3)
    
    #Filter data
    stock_data_ = stock_data[stock_data['Date'] <= '2021-06-14']
    revenue_data_ = revenue_data[revenue_data['Date'] <= '2021-04-30']

    #add data
    fig.add_trace(go.Scatter(x=stock_data_['Date'], y=stock_data_['Close'].astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=revenue_data_['Date'], y=revenue_data_['Revenue'].astype("float"), name="Revenue"), row=2, col=1)

    #Update axis titles
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)

     # Update layout
    fig.update_layout(showlegend=False, height=900, title=stock, xaxis_rangeslider_visible=True)
    
    # Show the plot
    fig.show()



#Plot Tesla stock grarh
make_graph(tesla_data, tesla_revenue, 'Tesla')

#Plot GME stock graph
make_graph(gme_data, gme_revenue, 'GameStop')
