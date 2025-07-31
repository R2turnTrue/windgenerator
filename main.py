import pandas as pd
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

fe = fm.FontEntry(
    fname='conconfont.ttf',
    name='Ownglyph corncorn')
fm.fontManager.ttflist.insert(0, fe)
plt.rcParams.update({'font.size': 12, 'font.family': 'Ownglyph corncorn'})

red = pd.read_csv('cds_result/res_00_RED_45deg.csv')
red = red[['time','A0 (RED)']]
red.rename(columns={'A0 (RED)': '45도'}, inplace=True)
red.rename(columns={'time': '시간'}, inplace=True)
red['45도'] -= red['45도'].iloc[0]

yellow = pd.read_csv('cds_result/res_01_YELLOW_30deg.csv')
yellow = yellow[['time','A2 (YELLOW)']]
yellow.rename(columns={'A2 (YELLOW)': '30도'}, inplace=True)
yellow.rename(columns={'time': '시간'}, inplace=True)
yellow['30도'] -= yellow['30도'].iloc[0]

purple = pd.read_csv('cds_result/res_02_PURPLE_0deg.csv')
purple = purple[['time','A1 (PURPLE)']]
purple.rename(columns={'A1 (PURPLE)': '0도'}, inplace=True)
purple.rename(columns={'time': '시간'}, inplace=True)
purple['0도'] -= purple['0도'].iloc[0]

res = pd.concat([red, yellow, purple])

res.plot(x='시간')

plt.title('발전기 프로펠러 날개별 LED 조도 변화')

plt.show()