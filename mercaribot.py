from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def main():
    # chromeDriverの位置
    driver = webdriver.Chrome('C:/Code/chromeDriver')

    set_search_conditions(driver)
    get_item(driver)

    driver.close()

def set_search_conditions(driver):
    #driver.get('https://www.mercari.com/jp/search/?keyword=%E3%82%B9%E3%83%9E%E3%83%9B')
    driver.get('https://jp.mercari.com/user/profile/374459928?status=on_sale')
    driver.set_window_size(1024,768)  #(1920, 1080)

def get_item(driver):
    """
    検索結果を取得する
    """
    items = driver.find_elements_by_class_name('items-box')

    print('----------------------------------------------------------')
    try:
       print(items[0].find_element_by_class_name('item-sold-out-badge').text)
    except:
       items[0].find_element_by_tag_name('h3').click()	#ここに購入処理入れる
           
    else:
       # 商品リンク
       print(items[0].find_element_by_tag_name('a').get_attribute('href'))
       # 商品タイトル
       print(items[0].find_element_by_tag_name('h3').text)
       # 商品画像
       print(items[0].find_element_by_tag_name('img').get_attribute('data-src'))
       # 価格
       print(items[0].find_element_by_class_name('items-box-price').text)

if __name__ == '__main__':
    main()

