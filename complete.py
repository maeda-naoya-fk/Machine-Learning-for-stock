import pandas as pd
import sys

class Complete:

    def __init__(self, dfs, stock_numbers):

        self.dfs = dfs
        self.sns = stock_numbers
        
    # スクレイピングしてきたデータを繋ぎ合わせる。また説明変数となるものを作る
    def com(self):
        
        #　スクレイピングしてきた企業ごとに作業を繰り返す
        for i in range(len(self.dfs)):
            
            # 日付と終値しか使わない
            df = self.dfs[i][['日付', '終値']]
            num = self.sns[i]
            df = df.rename(columns = {'日付':'Date', '終値':num})
            
            #説明変数となるもの。（当日ー前日）/前日の終値
            df[num + '_Diff'] = df[num]/df[num].shift()-1
            
            #まずcomplete_dfをtargetのdfをもとにマージしていく
            if i == 0:
                complete_df = df
            # Dateが共通するものでマージしていく
            else:
                complete_df = pd.merge(complete_df, df, on = 'Date')

        #complete_dfでnanになっていたらそれを補完するような作業を行なっていく。まずは見つける
        columns = self.sns.copy()
        columns.insert(0, 'Date')
        complete_isna = complete_df[columns]
        # なかったらそのまま
        if complete_isna.isna().sum().sum() == 0:
            return complete_df
        # あったら補完していく作業をやるが私がやったプログラムでは見つからなかったため今回はパスしている
        else:
            print('Error : There are missing value > Please choose other target_number or prepare_number')
            self.isna(complete_isna)
    #補完作業を行う
    def isna(self, complete_isna):
        sys.exit()
        pass
