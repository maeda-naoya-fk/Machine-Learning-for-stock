import configparser
from datetime import datetime
import json
from scraiping import *
from complete import *
from train import *
import sys

if __name__ == '__main__':


    print('Read config.ini')
    config = configparser.ConfigParser()
    config.read('config.ini')
    setup = config['setup']
    model = config['model']

    start = datetime.strptime(setup.get('start'), '%Y%m%d')
    finish = datetime.strptime(setup.get('finish'), '%Y%m%d')

    target_number = eval(setup.get('target_number'))
    prepare_number = eval(setup.get('prepare_number'))
    stock_numbers = prepare_number.copy()
    stock_numbers.insert(0, target_number)

    headers = {'User-Agent' : setup.get('User-Agent')}

    k = float(model.get('model_k'))
    max_depth = float(model.get('max_depth'))
    test_size = float(model.get('test_size'))
    print('Done')
    print('----------------------')



    print('Start scraiping')
    dfs = Scraiping(stock_numbers, start, finish, headers).main()
    print('All Done')
    print('----------------------')



    print('Make complete_df for train')
    complete_df = Complete(dfs, stock_numbers).com()
    print('Done')
    print('-----------------------')

    print('Start train')
    if k == 0:
        Tu = Tree_updown(complete_df, stock_numbers, test_size, max_depth)
        X, y = Tu.prepare()
        Tu.predict(X, y)
    elif k > 0:
        Tuk = Tree_updown_k(complete_df, stock_numbers, test_size, max_depth, k)
        X, y = Tuk.prepare_k()
        Tuk.predict(X, y)
    else:
        print('Error : you have to choose k > 0')
        sys.exit()
