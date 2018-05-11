# coding:utf-8
import requests
import re
import json
import xlwt
import time
urls = []
first_url = "https://s.taobao.com/search?q=%E8%BF%9E%E8%A1%A3%E8%A3%99&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180511&ie=utf8"
urls.append(first_url)
for p in range(1,50):
    uf = 'https://s.taobao.com/search?q=%E8%BF%9E%E8%A1%A3%E8%A3%99&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180511&ie=utf8&bcoffset=3&ntoffset=0&p4ppushleft=1%2C48&data-key=s&data-value={}'.format(p*44)
    urls.append(uf)

wb = xlwt.Workbook()
ws =wb.add_sheet('连衣裙',cell_overwrite_ok=True)
ws.write(0,0,'id')
ws.write(0,1,'标题')
ws.write(0,2,'主图地址')
ws.write(0,3,'详情地址')
ws.write(0,4,'售价')
ws.write(0,5,'邮费')
ws.write(0,6,'地址')
ws.write(0,7,'付款人数')
ws.write(0,8,'是否天猫')
ws.write(0,9,'店铺地址')
ws.write(0,10,'店铺名称')
ws.write(0,11,'类型ID')
headers = {
    'authority': 's.taobao.com',
    'method': 'GET',
    'path': '/search?q=selenium%E6%95%99%E7%A8%8B&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=-32&p4ppushleft=1%2C48&ntoffset=-32&s=616',
    'scheme': 'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'thw=cn; t=aaf1f066a52008e9fe325b78d7bae520; cna=5ylXE5QotzcCAXM8PHlFlgPy; hng=CN%7Czh-CN%7CCNY%7C156; UM_distinctid=162c2a7f1fddf-024d02a118f732-4446062d-1fa400-162c2a7f1fe1af; _cc_=WqG3DMC9EA%3D%3D; tg=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; enc=ZYwUbUbN1B6XLr1NH9rqq4A4T1212IddMVy0%2BUOGvZ0D33I5s916DZWl1U4sYSDY3iCY3e%2Fo9GwghVN%2BSNwpSw%3D%3D; cookie2=36b4198d455bfbe3cb7db682727b8cee; _tb_token_=5d67f6675ee51; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; swfstore=176415; mt=ci=0_0; v=0; JSESSIONID=3EB172DEA16AA3CF2C2E4E2A305D7E23; isg=BBwcqr-xqtq3MF4jmi1OczMh7ToOPcI87ZQz-vYdL4fqQbzLHqWQT5LTpam5SfgX',
    'upgrade-insecure-requests': '1',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
item = []
m = 0
for url in urls:
    # time.sleep(2)
    m += 1
    try:
        print(url)
        response = requests.get(url,headers=headers)
        html = response.text
        time.sleep(1)
        goods_info = re.findall('g_page_config = (\{.*?\}\});.*g_srp_loadCss', html, re.S)
        time.sleep(1)

        goods_json = goods_info[0]
        goods_dict = json.loads(goods_json)

        data = goods_dict['mods']['itemlist']['data']['auctions']
        print(data)
        item.append(data)
    except Exception as e:
        print(e)
        urls.append(url)
        continue

t = 0
for m in range(0,len(item)):
    for i in range(0, len(data)):
        # for item in goods_dict['mods']['itemlist']['data']['auctions']:
        t += 1
        ws.write(t, 0, data[i]['nid'])
        ws.write(t, 1, data[i]['title'])
        ws.write(t, 2, data[i]['pic_url'])
        ws.write(t, 3, data[i]['detail_url'])
        ws.write(t, 4, data[i]['view_price'])
        # if float(data[i]['view_fee']) == 0.00:
        #     ws.write(i + 1, 5, '包邮')
        # else:
        ws.write(t, 5, data[i]['view_fee'])
        ws.write(t, 6, data[i]['item_loc'])
        ws.write(t, 7, data[i]['view_sales'])
        ws.write(t, 8, data[i]['shopcard']['isTmall'])
        ws.write(t, 9, data[i]['shopLink'])
        ws.write(t, 10, data[i]['nick'])
        ws.write(t, 11, data[i]['category'])

wb.save('selenium教程.xls')
