from pytrends.request import TrendReq
import matplotlib.pyplot as plt

import pandas as pd


class GoogleTrend:
    def __init__(self):
        pass

    def get_trend(self, keywords):
        pytrends = TrendReq(hl='ja-JP', tz=540)
        pytrends.build_payload(
            keywords, timeframe='2021-07-01 2022-12-30', geo='JP'
            )
        df = pytrends.interest_over_time()
        return df

    def run(self):
        keywords1 = ['ビットコイン', 'BTC', 'ETH', '仮想通貨', 'リップル']
        keywords2 = ['Bitcoin', 'イーサリアム', 'コインチェック', '暗号通貨', 'ビットフライヤー']
        legend = [
            "Bitcoin(Ja)", 'BTC', 'ETH', 'CryptoCurrency(Ja)', 'Ripple(Ja)',
            'Bitcoin', 'Ethereum(Ja)', 'Coincheck(Ja)', 'CryptoCurrency(Ja)',
            'BitFlyer'
            ]
        df1 = self.get_trend(keywords1)
        df2 = self.get_trend(keywords2)
        data = pd.concat([df1, df2], axis=1)
        for _ in data.columns.values:
            if not _ == 'isPartial':
                plt.plot(data.index.values, list(data[_]))
        plt.xticks(rotation=90, fontsize=6)
        plt.ylabel('Search volume')
        plt.title('Google trend')
        plt.legend(legend, fontsize=8)
        plt.savefig('GoogleTrend.jpg', dpi=300)
