#商品を購入して、消費税を加えた計算結果を返す関数を記述してください。
#第1引数に商品の金額、第2引数に消費税（10%）を設定できるようにしてください。

def purchase_item(price,tax_price) ->int:
    total_price=price*(1 + (tax_price/100))
    print(f"商品金額は{total_price}円です。")

purchase_item(500,10)
