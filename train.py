from sklearn.tree import DecisionTreeClassifier
import sklearn.model_selection
import pandas as pd

class Tree_updown:

    def __init__(self, complete_df, stock_numbers, test_size, max_depth):

        self.c_df = complete_df
        self.sns = stock_numbers
        self.ts = test_size
        self.m = max_depth

        self.diffs = [sn + '_Diff' for sn in self.sns]


    def prepare(self):

        y = self.c_df[self.sns[0]].shift(-1) - self.c_df[self.sns[0]]
        y.loc[y >= 0] = 1
        y.loc[y < 0] = -1
        y = y[1:-1]

        X = self.c_df[self.diffs].iloc[1:-1]

        return X, y

    def predict(self, X, y):

        X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = self.ts, train_size = 1 - self.ts, random_state = 0)

        model = DecisionTreeClassifier(random_state = 0, max_depth = self.m)
        model.fit(X_train, y_train)

        next_day_diff = self.c_df[self.diffs].iloc[-1]
        next_day_predict = model.predict([next_day_diff])

        print('predict next day : UP') if next_day_predict == 1 else print('predict next day : CONSTANT') if next_day_predict == 0 else print('predict next day : DOWN')

        print('')
        print('テスト用正解率:{}'.format(model.score(X_test, y_test)))
        print('学習用正解率:{}'.format(model.score(X_train, y_train)))

        importance = pd.DataFrame({'feature_names':self.sns, 'coefficient':model.feature_importances_})
        print('')
        print(importance)

        print('')
        print('データ数:{}'.format(len(y)))


class Tree_updown_k(Tree_updown):

    def __init__(self, complete_df, stock_numbers, test_size, max_depth, k):
        super().__init__(complete_df, stock_numbers, test_size, max_depth)
        self.k = k

    def prepare_k(self):

        y = self.c_df[self.sns[0]].shift(-1)/self.c_df[self.sns[0]] - 1
        y.loc[y*100 >= self.k] = 1
        y.loc[y*100 <= -self.k] = -1
        y.loc[(-self.k < y*100) & (y*100 < self.k)] = 0
        y = y[1:-1]

        X = self.c_df[self.diffs].iloc[1:-1]

        return X, y

class Verify(Tree_updown_k):

    def __init__(self, complete_df, stock_numbers, verify_df, test_size, max_depth, k):
        super().__init__(complete_df, stock_numbers, test_size, max_depth, k)
        self.verify_df = verify_df

    def verify(self, X, y):

        X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = self.ts, train_size = 1 - self.ts, random_state = 0)

        model = DecisionTreeClassifier(random_state = 0, max_depth = self.m)
        model.fit(X_train, y_train)

        y_test = self.verify_df[self.sns[0]].shift(-1)/self.verify_df[self.sns[0]] - 1
        y_test.loc[y_test*100 >= self.k] = 1
        y_test.loc[y_test*100 <= -self.k] = -1
        y_test.loc[(-self.k < y_test*100) & (y_test*100 < self.k)] = 0
        y_test = y_test[1:-1]
        X_test = self.verify_df[self.diffs][1:-1]

        next_day_predict = model.predict(X_test)
        print(next_day_predict)
        print(y_test)

        print(next_day_predict == y_test)
