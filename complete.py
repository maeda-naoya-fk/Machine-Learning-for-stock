import pandas as pd
import sys

class Complete:

    def __init__(self, dfs, stock_numbers):

        self.dfs = dfs
        self.sns = stock_numbers

    def com(self):

        for i in range(len(self.dfs)):

            df = self.dfs[i][['日付', '終値']]
            num = self.sns[i]
            df = df.rename(columns = {'日付':'Date', '終値':num})

            df[num + '_Diff'] = df[num]/df[num].shift()-1

            if i == 0:
                complete_df = df

            else:
                complete_df = pd.merge(complete_df, df, on = 'Date')


        columns = self.sns.copy()
        columns.insert(0, 'Date')
        complete_isna = complete_df[columns]
        if complete_isna.isna().sum().sum() == 0:
            return complete_df

        else:
            print('Error : There are missing value > Please choose other target_number or prepare_number')
            self.isna(complete_isna)

    def isna(self, complete_isna):
        sys.exit()
        pass
