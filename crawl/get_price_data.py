import requests
import asyncio
from time import time
import json
import concurrent.futures
from bs4 import BeautifulSoup
import pandas as pd
import asyncio

loop = asyncio.get_event_loop()
list_code = pd.read_excel("code_stock.xlxs")


def get_data(code="VIC", page=1):
    print("code, page", code, page)
    df = pd.DataFrame(columns=["ticker", "time", "close", "open", "high", "low", "volume"])
    URL = f"https://s.cafef.vn/Lich-su-giao-dich-{code}-1.chn"
    hdr = {
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Sec-Fetch-Dest": "empty",
        "X-MicrosoftAjax": "Delta=true",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "*/*",
        "Origin": "https://s.cafef.vn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Referer": "https://s.cafef.vn/Lich-su-giao-dich-VNINDEX-1.chn",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8",
        "Cookie": "_ga=GA1.2.1063637455.1585215340; favorite_stocks_state=1; _uidcms=1585215340247638741; _gid=GA1.2.1677237587.1586756506; \
        cafef.IsMobile=IsMobile=NO; ASP.NET_SessionId=wqjhet2gh2fwaqr11xugxear; _ga=GA1.3.1063637455.1585215340; _gid=GA1.3.1677237587.1586756506",
    }

    # body = f"ctl00%24ContentPlaceHolder1%24scriptmanager=ctl00%24ContentPlaceHolder1%24ctl03%24panelAjax%7Cctl00%24ContentPlaceHolder1%24ctl03%24pager2&ctl00%24ContentPlaceHolder1%24ctl03%24txtKeyword={code}&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate1%24txtDatePicker=&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate2%24txtDatePicker=&ctl00%24UcFooter2%24hdIP=&__EVENTTARGET=ctl00%24ContentPlaceHolder1%24ctl03%24pager2&__EVENTARGUMENT={page}&__VIEWSTATE=%2FwEPDwUKMTU2NzY0ODUyMGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFKGN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RsMDMkYnRTZWFyY2jJnyPYjjwDsOatyCQBZar0ZSQygQ%3D%3D&__VIEWSTATEGENERATOR=2E2252AF&__ASYNCPOST=true&"
    body = f"ctl00%24ContentPlaceHolder1%24scriptmanager=ctl00%24ContentPlaceHolder1%24ctl03%24panelAjax%7Cctl00%24ContentPlaceHolder1%24ctl03%24pager2&ctl00%24ContentPlaceHolder1%24ctl03%24txtKeyword={code}&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate1%24txtDatePicker=&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate2%24txtDatePicker=&__VIEWSTATE=4%2BnBJTKHSUwIoNFlzUKX6w7rCOiKF900WRU%2FkrQW%2Fo7xC8bedavSHwvHgO2F3vS31brOLL5roYLt7N%2FgaPXsFX3t3T6DpznT39TqoHeIKg8pZugbv6k4Xfk6EC2ny2vbkTLVHAJKIhudHXLc4mV20kMOfmvx%2Bz%2BeuVo%2FVjM0uyNSBRTvVC4YDkQgXhpuprAvq%2FQQixW8UvmnWGVZqkZ%2Bw8XWHJovkc1MR7vwMCe5fJqwzrh2oB2enc5OqUkSPjUkHPaxU73dzusDSn28t%2FyXuuaF7Z3ZgvIFY4qih6XsH7q3qXrOo4x2TrMN05PtPotBT1dqdcJA%2FQeMtKEUitXDKBvu%2FvJnOxVry9S%2BiIGi5RAtH1wjDaP6GDA%2F78nFDGGa4sKFM1ulXUdgxKclftODrL0Of1%2BW8A%2BsOsECbgokymorZ2yLcmMBmVF7l7uYln8GpngKedBK77Igki5M2ED6aloqQdASM4E3Zy84C7SDeZf3uMCKynFgQ4d9EzJWa7qDQ6JiRQECajO4EfStfGYLlBShGo1s66P6pV9QoS2%2BcM%2B1p9EvSFQt5NIfuKirdAxWW0M%2BGXUfWWd6jqNA0bV41dvehRQTg%2B56TmH%2Fj%2BFiDNrdZk0KUHtrtulM6NAq47y6OpddM6MZvWlWjpO71maq53gvhvyfPNBNfsFJ%2FqvyD96%2FPH2O7bBV1IgU0Lc1eo2QzZ5VaxxHHU127x5k%2FKvAZduZYlSpEVb%2B98Db%2BLbZXCnHUtVIKWLzL%2B%2BjISDnxh6Rpae2mUkbU4nASNnh9JzpiLZwLvKeeOskcsixZV5X84f9chONil95qiYy%2F01ACaExHQ0uGdOalGWxZDXkmsk1O5DBmTdh8iO68HmI%2BKxk4J3zQpI2GjdxNPrACFa0lk%2F%2FrKMOoW4AvdLWfjzommfj0OJe4JiWF2skwEb2iXMnBsE%2B0CLl2ANYgdLEXJxMGiYSq5yp7GCmORN%2FP0G14V1pEcF%2BBR9BJoDOU1uXoWdeGXXXDinKfts4ouZjSc7%2FGkUtNh2OXcdzHFHziA0QvSiKWTckG4p%2B43xBRRrBFnYTk8wJbFnupRWhABlMAHLJjfj3ayVYY62O3286y8Y4eZi2Bl2x%2FZnK64ymWuDxhGpJo3uUVubjbvPM4w37QFe15IDazf9%2BeS%2B%2BTrPLksV9FYTjRMtZbKmHSnl%2BiWHhD01yxYGY16z4w6%2F8hA31Nt45LGhl%2Fa5xQdQHOGoXbPSekPVZkMguz7Z84qAoGHkmFgKeZLOnsXI86X1ZNXFqWBPcs5smBUi0NKfGFg%2BF8rURErvsYx7ihZVQp%2BDRFBRbOe6q8pGt0OyczJoZaB50fS2FajW2wuu410kbOkFgaK4F6r3iWbKTWPGLgaBUpfQ5jibY%2BbG%2BIWj%2BgQk7Kpb1pVNZhJ%2B54Zb0FZmMpNgZa0%2FTc6%2BguAp6MWm7p3ufruFvl%2FSi%2BTZ%2BqEMAzhnROuQGRE15i%2BQk6bqhKn8OZBQOtJXSd2UiJxHX8Aw6ANSGJL9YTTg7DPL%2F5eDvHV1627fWBcY5HH%2BpSEtQ7UyUXKd0r5EG%2FgBRNeGHvRXSfACBt090l9D21ZUlZ06phm4mrJ%2FLrlM0MObOkkB2ms9zUXNjhZW5goMKOzAZc25GH0TMDHdk9cV6HJeswA3x%2BBq0%2BmK4rGYWrWMuak9daLnWXB1Hf9Ri05hyRndQcDvEbWdNkivFbOAyEkGW0oLV7JE%2B6hGCn4U%2Ff9NunPKowavCPyNGxzKC98N7W2m5pG9AM4n%2BYmO2wbV%2BaDWBfvwe3kGNHELetLpNLgwqWUPlT28WSpW2eiWl8Atdgrk1nkyza9lX7IzF8%2FjD05qemdE%2BG3KyBNKQ5EVpVPKOuFXgMTtncn6GZJ6jLN2Nyg134m6Ng040VIkfWszk75ZM6sgKxn0zXWlPnjVRtb1zwr%2BmYzD8lWSYVQK7EUt7mA19LVuR2Y3SFvK%2FOqunxJKxL%2B26IFqBugPvktOVHFMUFcMkq632IY5IWghmz7E0cV%2BqldZInTyCl8z%2FmGE2aYHP7JJ0SR49aewAmVzsip4ldrWYF%2FAtJQ4VUPcl6CUjs%2Fgo8IKHE7KkxpH9m7BYLD4jMc5djcNt1uKWKRAsgJsexLoHxyX%2BZ8jqbE6eCwALeczl7X3QUNY59o7oiCGmuHgf0dOJnfkrvvlNnjrCrnVnM5W1B%2Fs%2Bx3wEQIRnXe%2BWFbmX1a%2BP%2B%2Bey40ZVCfTvI4gViMCoM9ELmi0qIWmKeWQmHzqRgnZ3NWJqUnEYfrvfGWRHApd7qWUHJPk4%2FlaVGkYekGx%2F3dHeHKw5gBbZByuz%2FbFpReGpCcvSpR%2BzfGZ04BtkvuzyDEPsu%2F3qsCGtIr%2FDJ4subUzBsudUAPcEH8klnTDOtgfBVYjBzV2MxO0y67QPHg6gEmAarmv8FuKBc3ek1hgEuh3nJd3UvpXvLcUYfnDrVvjqhQGhfFMW496Xwv7sPJnFme%2FzWF42fkhzbEh%2BSLmf8xESwt9WMCGP8QIjTcllGdz3gporzdyXdOMIgYJaCqJbi9euJsmIIgqpucyrFk3fnVU38I%2FkIIxS6r7NNB%2B3erNTX%2BiIOZUGUpSMRDafekHma90y8%2BL5gikWPY1z9W%2FdmKJ3wU%2FOQqHJPMsDDP8sv1w%2BGRmj69OEa%2FKvAeITCAAp5nHVxXeZwTiZtZhaiR6V%2B%2Bxac498J11e8xVMu%2BZBG%2FZZML%2FqMK0BRzolyPQ6g1QbZnIumAVVvRR33q4gq7wYG3XzRfC322%2F6sHq2L4etKwHxQcXwg9WCC%2Bn8zJ%2FzXP1DSUfm3GszEvTSuP6TyQQiTMXhGOPWW%2B0s3aN%2FMLlVclBw526WT9vVBir3qPYK8s1ZFXBCUxvkwB3QiuPmcgXhrNPc614uiYuqA4GT%2BHipLqmKLOHdbJRoYxlzktacB%2BRgPaJDY3CWEqTcntI%2BzqC0P3p1kRcbOQ7Mx1mhUSxhe2vC1EZ5bMtawygsUAkXXi9o0B9Akr33gLuV4UrPW14VlZLCpsMFC6g6Ybw%2F30IddJz5wR0lOJ%2F15mMsapjIkCGdkPWW8H76kahJEDcTKrbL0lNZRUuqMHlcdksQlTKNMOOjDwKVK4G98gNVgyhISa7dkvzkPY0J1304hfkPIVYwIaPy21ZkA1kRxjkVNYuXi2dLA1wpqDrAdoCLl9oVwYW%2FxE6G2D0lwRpjuJcTLAHDDjRNG6fzcj4awGt2sdqcxwu35wS8cZeVP7RkppcBSMVAGqPReyHS91hDNA%2F4kpgvuAaxIbRCVQwbpLnPvb1dUxrH4FhgoHKNio2%2Bf3p5h9Q3mA6PdrkrGzaS9Mxz1oiau1f%2B%2Fp5e%2BCTpnWOrE8%2FksUb3QlJwsGowL28IBDxotcXqfGsFCtYltIHkMUUs1hKWBdInHdxat6R5sXXCxVdqrRISbOnsqbE2XO6tV4mgG2f2vV2OabRhslhv4kgk7UvY0H7lnpj%2BLiCZxn1DLKmZyAOg40f6KzCKiNB1kU68GxNm1BAiUS%2BQ%2BiL8gRW9tgDcBy84t0da%2Bz75RGM22uCXU8TcUnotxOdSNlJJbjjSphYTaszaxRAEW9hE9FV%2FBQ2OcdKvsNuoi4dP3eDB8ld6HIAEnuYu7Vt%2BKPRlLUDL1jdzT3Rom2viji8r8y0oUaG7e4P%2Foqi0zTsqlpqPCImqYlCdL%2FCo%2F0jeUIOCJK28BA7cnGGy9ZEP6uuIgzscEY%2BAwXGI85Xj4mR%2Boxwg1x8vR14aa6HmakunNXDYeOVES%2B0tuRKScTPxbGieG7J9b9jSFO16K54uiuh%2F%2BrRRcU5zTNuG9cgrk%2FborEuii3M3lI%2BR3miP5jd%2FVV9ixl47WfIH8rQM%2BOa%2FfY6X0zYdwJ%2FrCG9WNqeXJiecehJnUYU6vczUXJhEBX5JMuaRX8NWNmCV7C28t%2FqO4yXb42ikVF1T462rEI84vKgOnbc0kEZxnR41eUQNmjW%2BubRUF98Rm3RyVTlxTDLPpAqcMuWauUcsVhrLngR9e9EjQfHOrQfrtFHAU6BQmHpgnGvJgyVyaDXH11J1mzMRdliCRzlzt%2BLdB3FMbVuKFIkp5rQpkk0a%2FeY75nf%2FeUPFtWS0CEL3BoyQua5QrWhoy%2BegjGuzJJJYkZBJpMgdTdtzCFg99v4C3NNgYN4Ulbic8RrrRdSMaA6MexGwjbg9tNEinSWM9ClhlKXO%2BRumn7cy9Pwz%2BfXpGhyIDL2OhUC074yLCOzn3iPJlE631uWKXjs0abOOhkgjYXan9d0aDStXURjmLH3WOxqohx%2BjS7Miz%2FS3BX1CsX%2FLhejUdl0B9s36mwbhDh4AC%2FTFtTCD7CaUz11NigyRnYzSDAU%2BEBRwu%2Bj11TLIWHeg%2BkzKfDyxYdsAHSPWWjk6%2Bv2CvO3Wl1jSjkkz4bSc0%2FpDXfqEcAEA2VaNTAIR%2F9OcWMWgWJhbZxjMd2hevrPlvsLlgg5BRNDtOenk6CLAhRPzCFgjtRrflUIQEont28WIjpfUAlWxN%2Br0MrepLZMOJOo2TiHcf8cERQSButcZ4%2FHwLl4S%2BpydWY1IB2VZSp98ux4WrE%2B54vSE92EcBY9UCBfg2VmtSA%2BgyfzGQWjAZzQJxB2qIGIb3Z%2FLncGBJ7n6hKK7SE38BWTWWWFKc27dwb%2FBVKwdFvUiCcOKqnbHhG5CF10xhInzXpBfiobifxNU%2FuofeB2k5VI%2BMKgN5p6SfJMUiqM3miJTD2BuKjpI1sfijdrJzqSNEJZsBxvC2lX82N5Xef6CYFORN9oKNfGUmevc661HkRCcMgHThpZI0ox4c78ngm1wqinChyZNk%2BRJLrmckh%2BT%2BK0EEZRwVlzNM8kSBQxm4n9IKHhdbgMTY5tAb0ANqgB3%2BKM28W2KvnxfIswXrGYh%2Be7NIk1FowUguwrowESCiva9pNe2Clr09WlqjUhr4mAN9ygP1tzmKBw77Qw2WRS8PN29GpGBlz6wUbJ6e1JOtdoqLDQwHFSg1yMaL53CKQKGFqFRXjTNpWObPKYAjRBdHMI1FSyosm%2FITW7N%2F2AOytZK0Qi8E6ZO44ZGxiTMziMT%2BC5CziAzR3cVTCHFBApQNfGpAwzfqX%2F%2FmThTRofi25U6zHzh5eECW3m2HKX52N%2BKKunKuf0EzRbUan7FswLxAi3nEemSuuXgrejwCNaixklQIAzgwREIBGRX8ip8EFeBxSf%2B%2F7Nmiusp18yw5B1P4bb6FaGLhJ04M9VpQatZQPF59V9ajFW%2B2SY3QNmo4xvP4FECzI5ytlSt&__VIEWSTATEGENERATOR=2E2252AF&__EVENTTARGET=ctl00%24ContentPlaceHolder1%24ctl03%24pager2&__EVENTARGUMENT={page}&__ASYNCPOST=true&"
    resps = requests.post(URL, headers=hdr, data=body)
    soup = BeautifulSoup(resps.content, 'html.parser')
    table = soup.find('table', id='GirdTable2').find_all('tr')[2:]

    def _str_to_float(string):
        string = string.encode(
            'utf-8').decode(
                'utf-8').replace(
                    '\xa0', '').replace(
                        ',', '').replace(
                            "(", "").replace(" %)", "")

        return float(string)

    for row in table:
        columns = row.find_all('td')
        df = pd.concat([df, pd.DataFrame.from_records([{
            "ticker": code,
            "time": columns[0].get_text(),
            "close": _str_to_float(columns[2].get_text()),
            "open": _str_to_float(columns[9].get_text()),
            "high": _str_to_float(columns[10].get_text()),
            "low": _str_to_float(columns[11].get_text()),
            "volume": _str_to_float(columns[5].get_text())
        }])])
        # df = df.append({
        #     "ticker": code,
        #     "time": columns[0].get_text(),
        #     "close": _str_to_float(columns[2].get_text()),
        #     "open": _str_to_float(columns[9].get_text()),
        #     "high": _str_to_float(columns[10].get_text()),
        #     "low": _str_to_float(columns[11].get_text()),
        #     "volume": _str_to_float(columns[5].get_text())
        # }, ignore_index=True)

    return df


def get_all_data(code="VIC"):
    available = True
    try:
        df = pd.read_csv(f'data-all/{code}.csv')
    except Exception as e:
        df = pd.DataFrame(columns=["ticker", "time", "close", "open", "high", "low", "volume"])

    for i in (range(1, 3)):
        df_resp = get_data(page=i, code=code)
        if df_resp.empty or available is False:
            break
        df = pd.concat([
            df, df_resp
        ], ignore_index=True).reset_index(drop=True)

    df = df.drop_duplicates(subset="time")
    # df1 = pd.read_csv(f'data-all/stock.csv')
    df.to_csv(f'data-all/{code}.csv', index=False)


if __name__ == "__main__":
    # codes = list_code[(list_code["Unnamed: 2"] == "HSX") & (
    #     list_code["Unnamed: 0"].str.len() == 3)]["Unnamed: 0"].tolist()
    codes = list_code[(list_code["Unnamed: 0"].str.len() == 3)]["Unnamed: 0"].tolist()

    with concurrent.futures.ThreadPoolExecutor(max_workers=600) as executor:
        executor.map(get_all_data, codes)
