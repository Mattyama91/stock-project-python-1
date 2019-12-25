import pandas as pd
import numpy as np
import os

name_abbreviation_mWIG40_dict = {
    'mWIG40': 'mWIG40',
    '11_bit_studios': '11B',
    'Asseco_Poland': 'ACP',
    'Amica': 'AMC',
    'Grupa_Azoty': 'ATT',
    'Budimex': 'BDX',
    'Benefit_Systems': 'BFT',
    'Bank_Handlowy_w_Warszawie': 'BHW',
    'BNP_Paribas_Bank_Polska': 'BNP',
    'Boryszew': 'BRS',
    'Inter_Cars': 'CAR',
    'Ciech': 'CIE',
    'CI_Games': 'CIG',
    'Celon_Pharma': 'CLN',
    'Comarch': 'CMR',
    'Develia': 'DVL',
    'AmRest_Holdings': 'EAT',
    'Echo_Investment': 'ECH',
    'Enea': 'ENA',
    'Energa': 'ENG',
    'Eurocash': 'EUR',
    'Fabryka_Maszyn_Famur': 'FMF',
    'Fabryki_Mebli_Forte': 'FTE',
    'Giełda_Papierów_Wartościowych_w_Warszawie': 'GPW',
    'Globe_Trade_Centre': 'GTC',
    'Getin_Holding': 'GTN',
    'ING_Bank_Śląski': 'ING',
    'Kernel_Holding': 'KER',
    'Kruk': 'KRU',
    'Grupa_Kęty': 'KTY',
    'LiveChat_Software': 'LVC',
    'Lubelski_Węgiel_Bogdanka': 'LWB',
    'Mabion': 'MAB',
    'Bank_Millennium': 'MIL',
    'Orbis': 'ORB',
    'PKP_Cargo': 'PKP',
    'PlayWay': 'PLW',
    'Stalprodukt': 'STP',
    'Ten_Square_Games': 'TEN',
    'VRG': 'VRG',
    'Wirtualna_Polska_Holding': 'WPL'
}

path = '/Users/michalozieblo/Desktop/stock-project-python/csv-files'

class Parameters:

    def __init__(self, abbreviations_of_companies):
        self.abbreviations_of_companies = abbreviations_of_companies
        self.list_source_df = []

        if len(self.abbreviations_of_companies) > 0:
            for i in self.abbreviations_of_companies:
                self.source_df = pd.read_csv(os.path.join(path,r'%s_d.csv' % i), delimiter=',', index_col=[0]) # , index_col=[0]
                self.source_df.index = pd.to_datetime(self.source_df.index) #TEST #ZDANY
                self.list_source_df.append(self.source_df)


        else:
            self.source_df = pd.read_csv(os.path.join(path,r'%s_d.csv' % abbreviations_of_companies), delimiter=',', index_col=[0]) # , index_col=[0]
            self.source_df.index = pd.to_datetime(self.source_df.index) #TEST # ZDANY
            self.list_source_df.append(self.source_df)

    def describe_company_df(self):
        print(self.source_df.describe(include='all'))

    def high_price(self):
        high_price = self.source_df['Najwyzszy']
        return high_price

    def low_price(self):
        low_price = self.source_df['Najnizszy']
        return low_price

    def open_price(self):

        list_open_price = []
        column_headlines = []

        for i in self.list_source_df:
            open_price = i['Otwarcie']
            list_open_price.append(open_price)

        for i in self.abbreviations_of_companies:
            column_headlines.append('Open_price_%s' % i)

        df_open_price = pd.concat(list_open_price, axis=1)
        df_open_price.columns = column_headlines

        return df_open_price

    def close_price(self):

        list_close_price = []
        column_headlines = []

        for i in self.list_source_df:
            close_price = i['Zamkniecie']
            list_close_price.append(close_price)

        for i in self.abbreviations_of_companies:
            column_headlines.append('Close_price_%s' % i)

        df_close_price = pd.concat(list_close_price, axis=1)
        df_close_price.columns = column_headlines

        return df_close_price

    def volume_stock(self):

        list_volume_stock = []
        column_headlines = []

        for i in self.list_source_df:
            volume_stock = i['Wolumen']
            list_volume_stock.append(volume_stock)

        for i in self.abbreviations_of_companies:
            column_headlines.append('Wolumen_%s' % i)

        # df_volume_stock = pd.concat(list_volume_stock, axis=1)
        # df_volume_stock.columns = column_headlines

        return list_volume_stock

    def daily_movement(self):

        database = pd.read_csv(os.path.join(path,r'database.csv'), delimiter=',', index_col=[0]) # , index_col=[0] BARDZO WAZNE # , delimiter=','

        list_open_close_price = []
        column_headlines = []

        for i in self.abbreviations_of_companies:
            open_price = database['Open_price_%s' % i]
            close_price = database['Close_price_%s' % i]
            open_price_subtract = open_price.sub(close_price)
            list_open_close_price.append(open_price_subtract)
            column_headlines.append('Daily_movement_%s' % i)

        daily_movement = pd.concat(list_open_close_price, axis=1)
        daily_movement.columns = column_headlines

        return daily_movement

    def sum_of_movements(self):

        database = pd.read_csv(os.path.join(path,r'database.csv'))

        for i in self.abbreviations_of_companies:
            open_price = database['Open_price_%s' % i]
            close_price = pd.Series(database['Close_price_%s' % i])
            open_price_subtract = open_price.sub(close_price)
            price_subtract_sum = np.sum(open_price_subtract)
            x = 'price_subtract_sum for %s: ' % i, price_subtract_sum
            print(x) ###### !!!

            result = []
            result.append(str(x)) #SPRAWDZ

        return result

    if __init__ == "__main__":
        print("Parameters run directly")
    else:
        print("Parameters imported into another module")