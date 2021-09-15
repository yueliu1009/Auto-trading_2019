import okex.account_api as account
import okex.futures_api as future
import json
from twilio.rest import Client

if __name__ == '__main__':

    api_key = 'd187d845-92ed-4711-9bdd-03d1aa5849cb'
    seceret_key = '41CAF0030493BE13423DF449CE2348D2'
    passphrase = 'adou1009'
    
    # future api test
    futureAPI = future.FutureAPI(api_key, seceret_key, passphrase, True)
    #result = futureAPI.get_position()
    #result2 = futureAPI.get_coin_account('ETC')
    result3 = futureAPI.get_coin_account("EOS")
    #result4 = futureAPI.get_accounts()
    #result5 = futureAPI.get_specific_ticker("EOS-USD-190329")
    result6 = futureAPI.get_holds_amount("EOS-USD-190329")
    result7 = futureAPI.get_trades("EOS-USD-190329",0,5,5)
    result8 = futureAPI.get_specific_ticker("EOS-USD-190329")


    #result = futureAPI.get_ledger('btc')
    #result = futureAPI.get_products()
    #result = futureAPI.get_depth('EOS-USD-190329', 1)
    #result = futureAPI.get_ticker()
    #result = futureAPI.get_specific_ticker('ETC-USD-181026')
    #result = futureAPI.get_specific_ticker('ETC-USD-181026')
    #result = futureAPI.get_trades('ETC-USD-181026', 1, 3, 10)
    #result6 = futureAPI.get_kline('EOS-USD-190329','2018-10-14T03:48:04.081Z', '2018-12-20T03:48:04.081Z')
    #result = futureAPI.get_index('EOS-USD-181019')
    #result = futureAPI.get_products()
    #result = futureAPI.take_order("ccbce5bb7f7344288f32585cd3adf357", 'BCH-USD-181019','2','10000.1','1','0','10')
    #result = futureAPI.take_order("ccbce5bb7f7344288f32585cd3adf351",'BCH-USD-181019',2,10000.1,1,0,10)
    #result = futureAPI.get_trades('BCH-USD-181019')
    #result = futureAPI.get_rate()
    #result = futureAPI.get_estimated_price('BTC-USD-181019')
    #result = futureAPI.get_holds('BTC-USD-181019')
    #result = futureAPI.get_limit('BTC-USD-181019')
    #result = futureAPI.get_liquidation('BTC-USD-181019', 0)
    #result = futureAPI.get_holds_amount('BCH-USD-181019')
    #result = futureAPI.get_currencies()



    #print('result' + "==" + json.dumps(result))
    #print(json.dumps(result2))
    print(json.dumps(result3))
    #print(json.dumps(result4))
    #print(json.dumps(result#5))
    print('result6' + "==" + json.dumps(result6))
    print('result7' + "==" + json.dumps(result7))
    print('result8' + "==" + json.dumps(result8))

    #account_sid = 'AC3a900abcdbe035b7f1d0757fae1ad7eb'
    #auth_token = '5c79b7972434d0a2f1e6814438318c59'
    #client = Client(account_sid, auth_token)
    #message = client.messages.create(body=json.dumps(result8), from_='+61488856275', to='+61412986090')
    #print(message.sid)
