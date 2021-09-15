#  coding:utf-8
import time

advertsing = '''
    **************************************
    *         合约自动交易程序            *
    *         Tel：15353378609           *                     
    *         -----------------          *               
    *                                    *   
    **************************************
'''
from Func import CountDown, N_time, Lisp, Median, Cycle_data,Initialize
import okex.futures_api as future


class AutoTrade():

    def __init__(self,api_key, seceret_key, passphrase,symbol,Min,Max,n):
        self.api_key = api_key
        self.seceret_key = seceret_key
        self.passphrase = passphrase
        self.symobl = symbol
        self.Lisp = Lisp(Min,Max,n)
        self.Median = Median(self.Lisp)
        self.Median1,self.Median2 = self.Median[0],self.Median[1]
        self.KD,self.PK,self.PD,self.KK = Median(self.Median1)[0],Median(self.Median1)[1],Median(self.Median2)[0],Median(self.Median2)[1]
        self.KDcyc,self.PKcyc,self.PDcyc,self.KKcyc = Cycle_data(self.KD[::-1]),Cycle_data(self.PK[::-1]),Cycle_data(self.PD),Cycle_data(self.KK)

    def KD(self, size, leverage):
        futureApi = future.FutureAPI(self.api_key, self.seceret_key, self.passphrase, True)
        ticker = futureApi.get_specific_ticker(instrument_id=self.symobl)
        ticker_last = float(ticker['last'])
        my_info = futureApi.get_specific_position(instrument_id=self.symobl)
        long_qty = int(my_info['holding'][0]['long_qty'])
        long_avg_cost = my_info['holding'][0]['long_avg_cost']
        long_avail_qty = int(my_info['holding'][0]['long_avail_qty'])
        short_qty = int(my_info['holding'][0]['short_qty'])
        short_avg_cost = my_info['holding'][0]['short_avg_cost']
        short_avail_qty = int(my_info['holding'][0]['short_avail_qty'])
        print('***** LocalTime : {}***** '.format(N_time()))
        print('***** high_24h price : {}-----low_24h price : {}*****'.format(ticker['high_24h'], ticker['low_24h']))
        print('***** New Price : {} *****'.format(ticker['last']))
        print('***** 24h_Trading Volume : {}*****'.format(ticker['volume_24h']))
        print('{}Hold current,long_qty{}, long_avail_qty{} , long_avg_cost{}'
              .format(N_time(), long_qty, long_avail_qty, long_avg_cost))
        print('{}Hold current,short_qty{},short_avail_qty{} ,short_avg_cost{}'
              .format(N_time(), short_qty,
                      short_avail_qty, short_avg_cost))
        CountDown()
        for i in self.KDcyc:
            if i[0] < ticker_last < i[1] and i[3] == 0:
                Gprice = (float(i[0])+float(i[1]))/2
                i[3] = 1
                order = futureApi.take_order(client_oid=111111, instrument_id=self.symobl, otype=1, price=Gprice,
                                             size=(i[2]*size),
                                             match_price=0, leverage=leverage)
                print('----- {}Successful create KD_order ID:{}-----'.format(N_time(), order['order_id']))
            time.sleep(0.5)

    def PK(self,size, leverage):
        futureApi = future.FutureAPI(self.api_key, self.seceret_key, self.passphrase, True)
        ticker = futureApi.get_specific_ticker(instrument_id=self.symobl)
        ticker_last = float(ticker['last'])
        my_info = futureApi.get_specific_position(instrument_id=self.symobl)
        long_qty = int(my_info['holding'][0]['long_qty'])
        long_avg_cost = my_info['holding'][0]['long_avg_cost']
        long_avail_qty = int(my_info['holding'][0]['long_avail_qty'])
        short_qty = int(my_info['holding'][0]['short_qty'])
        short_avg_cost = my_info['holding'][0]['short_avg_cost']
        short_avail_qty = int(my_info['holding'][0]['short_avail_qty'])
        print('***** LocalTime : {}***** '.format(N_time()))
        print('***** high_24h price : {}-----low_24h price : {}*****'.format(ticker['high_24h'], ticker['low_24h']))
        print('***** New Price : {} *****'.format(ticker['last']))
        print('***** 24h_Trading Volume : {}*****'.format(ticker['volume_24h']))
        print('{}Hold current,long_qty{}, long_avail_qty{} , long_avg_cost{}'
              .format(N_time(), long_qty, long_avail_qty, long_avg_cost))
        print('{}Hold current,short_qty{},short_avail_qty{} ,short_avg_cost{}'
              .format(N_time(), short_qty,
                      short_avail_qty, short_avg_cost))
        CountDown()
        for i in self.PKcyc:
            if i[0] < ticker_last < i[1] and i[3] == 0 and short_qty > 0:
                Gprice = (float(i[0])+float(i[1]))/2
                order = futureApi.take_order(client_oid=111111, instrument_id=self.symobl, otype=4, price=Gprice,
                                             size=(i[2]*size),
                                             match_price=0, leverage=leverage)
                print('----- {}Successful create PK_order ID:{}-----'.format(N_time(), order['order_id']))
                self.KKcyc = Initialize(self.KKcyc)
            time.sleep(0.5)

    def PD(self,size, leverage):
        futureApi = future.FutureAPI(self.api_key, self.seceret_key, self.passphrase, True)
        ticker = futureApi.get_specific_ticker(instrument_id=self.symobl)
        ticker_last = float(ticker['last'])
        my_info = futureApi.get_specific_position(instrument_id=self.symobl)
        long_qty = int(my_info['holding'][0]['long_qty'])
        long_avg_cost = my_info['holding'][0]['long_avg_cost']
        long_avail_qty = int(my_info['holding'][0]['long_avail_qty'])
        short_qty = int(my_info['holding'][0]['short_qty'])
        short_avg_cost = my_info['holding'][0]['short_avg_cost']
        short_avail_qty = int(my_info['holding'][0]['short_avail_qty'])
        print('***** LocalTime : {}***** '.format(N_time()))
        print('***** high_24h price : {}-----low_24h price : {}*****'.format(ticker['high_24h'], ticker['low_24h']))
        print('***** New Price : {} *****'.format(ticker['last']))
        print('***** 24h_Trading Volume : {}*****'.format(ticker['volume_24h']))
        print('{}Hold current,long_qty{}, long_avail_qty{} , long_avg_cost{}'
              .format(N_time(), long_qty, long_avail_qty, long_avg_cost))
        print('{}Hold current,short_qty{},short_avail_qty{} ,short_avg_cost{}'
              .format(N_time(), short_qty,
                      short_avail_qty, short_avg_cost))
        CountDown()
        for i in self.PDcyc:
            if i[0] < ticker_last < i[1] and i[3] == 0 and short_qty > 0:
                Gprice = (float(i[0]) + float(i[1])) / 2
                order = futureApi.take_order(client_oid=111111, instrument_id=self.symobl, otype=3, price=Gprice,
                                             size=(i[2] * size),
                                             match_price=0, leverage=leverage)
                print('----- {}Successful create PD_order ID:{}-----'.format(N_time(), order['order_id']))
                self.KDcyc = Initialize(self.KDcyc)
            time.sleep(0.5)

    def KK(self,size, leverage):
        futureApi = future.FutureAPI(self.api_key, self.seceret_key, self.passphrase, True)
        ticker = futureApi.get_specific_ticker(instrument_id=self.symobl)
        ticker_last = float(ticker['last'])
        my_info = futureApi.get_specific_position(instrument_id=self.symobl)
        long_qty = int(my_info['holding'][0]['long_qty'])
        long_avg_cost = my_info['holding'][0]['long_avg_cost']
        long_avail_qty = int(my_info['holding'][0]['long_avail_qty'])
        short_qty = int(my_info['holding'][0]['short_qty'])
        short_avg_cost = my_info['holding'][0]['short_avg_cost']
        short_avail_qty = int(my_info['holding'][0]['short_avail_qty'])
        print('***** LocalTime : {}***** '.format(N_time()))
        print('***** high_24h price : {}-----low_24h price : {}*****'.format(ticker['high_24h'], ticker['low_24h']))
        print('***** New Price : {} *****'.format(ticker['last']))
        print('***** 24h_Trading Volume : {}*****'.format(ticker['volume_24h']))
        print('{}Hold current,long_qty{}, long_avail_qty{} , long_avg_cost{}'
              .format(N_time(), long_qty, long_avail_qty, long_avg_cost))
        print('{}Hold current,short_qty{},short_avail_qty{} ,short_avg_cost{}'
              .format(N_time(), short_qty,
                      short_avail_qty, short_avg_cost))
        CountDown()
        for i in self.KKcyc:
            if i[0] < ticker_last < i[1] and i[3] == 0 and short_qty > 0:
                Gprice = (float(i[0]) + float(i[1])) / 2
                i[3] = 1
                order = futureApi.take_order(client_oid=111111, instrument_id=self.symobl, otype=2, price=Gprice,
                                             size=(i[2] * size),
                                             match_price=0, leverage=leverage)
                print('----- {}Successful create KK_order ID:{}-----'.format(N_time(), order['order_id']))
            time.sleep(0.5)
