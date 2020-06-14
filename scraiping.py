import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

class Scraiping:

    def __init__(self, stock_numbers, start, finish, headers):

        self.sns = stock_numbers
        self.start = start
        self.finish = finish
        self.headers = headers

    def main(self):

        dfs = []
        for sn in self.sns:
            df = self.scra(sn)
            dfs.append(df)
            print('Done : ' + sn)

        return dfs

    def scra(self, sn):


        data = []
        for y in range(self.start.year, self.finish.year+1):

            url = 'https://kabuoji3.com/stock/{}/{}/'.format(int(sn), y)
            soup = BeautifulSoup(requests.get(url, headers = self.headers).content,'html.parser')
            tr = soup.find_all('tr')

            t = 1
            while True:

                try:
                    td_t = [t.text for t in tr[t].find_all('td')]
                    date = pd.to_datetime(td_t[0])
                    if (self.start <= date) and (date <= self.finish):
                        td_t[4] = int(td_t[4])
                        data.append(td_t)
                    elif (date > self.finish):
                        break
                except IndexError:
                    break

                t += 1

            time.sleep(1)



        df = pd.DataFrame(data, columns = ['日付', '始値', '高値', '安値', '終値', '出来高', '終値調整'])
        return df
