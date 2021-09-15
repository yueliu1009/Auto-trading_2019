
import okex.futures_api as future

import json

if __name__ == '__main__':
    api_key = ''
    seceret_key = ''
    passphrase = ''

     futureAPI = future.FutureAPI(api_key, seceret_key, passphrase, True)

    orders = []
    order1 = {"client_oid": "f379a96206fa4b778e1554c6dc969687", "type": "2", "price": "1800.0", "size": "1",
              "match_price": "0"}
    order2 = {"client_oid": "f379a96206fa4b778e1554c6dc969687", "type": "2", "price": "1800.0", "size": "1",
              "match_price": "0"}
    orders.append(order1)
    orders.append(order2)
    orders_data = json.dumps(orders)
    print(orders_data)
    result = futureAPI.take_orders('BCH-USD-181019', orders_data=orders_data, leverage=10)


    print(json.dumps(result))
