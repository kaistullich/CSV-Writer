# Excel .CSV writer

import csv

# Sample list of lists to be converted
export = [
    # Brand                 Name         Price      Shipping    Rating       Category       Year         availability           image                                                                                                                                              Links to Product      
    ['Apple',           'Macbook Pro',    1300,       True,       4.5,      'Laptops',      2016,           True,        "http://zdnet1.cbsistatic.com/hub/i/2016/11/07/f2fafebf-2442-4cf1-9d48-d71fcc48a4ae/6b69e3ef899dd4feef43c63b2f9e195b/macbook-pro-13-header2.jpg",      "https://goo.gl/fI5207"],
    ['Acer',            'Aspire',         579,        False,      4.0,      'Laptops',      2014,           False,       "https://images-na.ssl-images-amazon.com/images/I/71tiAIUkggL._SL1322_.jpg",                                                                           "https://goo.gl/eXNa51"],
    ['Gigabyte',        'Gigabyte',       1699,       True,       5.0,      'Laptops',      2016,           True,        "http://images10.newegg.com/ProductImageCompressAll300/34-233-175-07.jpg",                                                                             "https://goo.gl/obhC29"],
    ['Dell',            'Inspiron',       799,        True,       3.4,      'Laptops',      2016,           True,        "http://3.bp.blogspot.com/-IuMXastfEeg/UYOUsLQfzjI/AAAAAAAAAzA/g4MrZRhmVgo/s1600/Dell+Inspiron+3521.jpg",                                              "https://goo.gl/4ktz0M"],  
    ['Apple',           'Macbook Air',    899,        True,       4.7,      'Laptops',      2016,           True,        "http://www.notebookcheck.net/uploads/tx_nbc2/design_unibody2_20101020_01.png",                                                                        "https://goo.gl/KKlPpx"],
    ['Canon',           'EOS Rebel',      599,        False,      4.7,      'Cameras',      2016,           False,       "https://shop.usa.canon.com/wcsstore/ExtendedSitesCatalogAssetStore/34688_1_xl.jpg",                                                                   "https://goo.gl/K0pUuT"],
    ['Nikon',           'D5500',          699,        True,       4.8,      'Cameras',      2015,           True,        "http://cdn-4.nikon-cdn.com/e/Q5NM96RZZo-YRYNeYvAi9beHK4x3L-8joW7yUnybX4TCMkFk-mOrm-nraMSB68suimClsSfnK7sEK7urtYpz1Q==/Views/1544_D5500_left.png",     "https://goo.gl/4Q6Sfj"],
    ['Canon',           'EOS 80D',        1599,       True,       4.9,      'Cameras',      2016,           True,        "http://www.newsshooter.com/wp-content/uploads/2016/02/EOS-80D-EF-S-18-55mm-IS-STM-LCD-Open-FSL.jpg",                                                  "https://goo.gl/MlSXkW"],
    ['Sony',            'Alpha a77 II',   2099,       True,       4.9,      'Cameras',      2016,           False,       "https://phillipreeve.net/blog/wp-content/uploads/2015/06/sony_alpha-7r-ii-_05.jpg",                                                                   "https://goo.gl/IR8y9O"],
    ['Canon',           'EOS 6D',         1899,       True,       4.9,      'Cameras',      2016,           True,        "http://www.kenrockwell.com/canon/6d/D3S_9085-left-1200.jpg",                                                                                          "https://goo.gl/q5eRHo"],
    ['Xbox',            'Xbox One S',     299,        False,      5.0,      'Gaming',       2016,           True,        "https://i.ytimg.com/vi/XuTwtOo88r8/maxresdefault.jpg",                                                                                                "https://goo.gl/ubtLdb"],
    ['Sony',            'Playstation 4',  399,        False,      3.7,      'Gaming',       2014,           False,       "http://media.psu.com/media/articles/image/playstation4_image.jpg",                                                                                    "https://goo.gl/c1iMbU"],
    ['Nintendo',        'Wii U',          299,        False,      2.5,      'Gaming',       2012,           True,        "http://www.cheatsheet.com/wp-content/uploads/2016/05/wii-u.jpg",                                                                                      "https://goo.gl/zaWk4N"],
    ['Sega',            'Dreamcast',      99,         True,       3.0,      'Gaming',       1998,           True,        "https://upload.wikimedia.org/wikipedia/commons/a/a0/Sega-dreamcast-set.png",                                                                          "https://goo.gl/oyUrMv"],
    ['Nintendo',        '3DS',            199,        False,      4.4,      'Gaming',       2013,           True,        "http://www.nintendo.com/images/social/fb-3ds-400x400.jpg",                                                                                            "https://goo.gl/QgQjX9"],
    ['Netgear',         'N600',           109,        False,      4.4,      'Networking',   2014,           False,       "http://www.netgear.com/images/Products/Networking/WirelessRouters/WNDR3700v5/WNDR3700v5_3D_ENbox_Transparent_c.png",                                  "https://goo.gl/iLQsCd"],
    ['Xfinity',         'Arris Touchstone',199,       False,      4.3,      'Networking',   2016,           True,        "http://pisces.bbystatic.com/image2/BestBuy_US/images/products/9082/9082028_rd.jpg;canvasHeight=550;canvasWidth=642",                                  "https://goo.gl/2EnGP4"],
    ['Zoom',            'N300',            66,        False,      4.2,      'Networking',   2015,           True,        "http://pisces.bbystatic.com/image2/BestBuy_US/images/products/4277/4277014_rd.jpg;maxHeight=550;maxWidth=642",                                        "https://goo.gl/MsKH2a"],
    ['Asus',            'RT-AC1200',       49,        False,      3.3,      'Networking',   2015,           False,       "http://gloimg.gearbest.com/gb/pdm-product-pic/Electronic/2015/12/30/goods-img/1475007642748193383.JPG",                                               "https://goo.gl/devBsb"],
    ['Netgear',         'NighHawk X10',    499,       True,       4.5,      'Networking',   2016,           True,        "http://www.geeky-gadgets.com/wp-content/uploads/2016/10/Netgear-Nighthawk-X10-Router.jpg",                                                            "https://goo.gl/aZUgUG"],
    ['General Tools',   'Screwdriver',     20,        False,      1.0,      'Tools',        2010,           False,       "https://images-na.ssl-images-amazon.com/images/I/51KkvLH-9JL._SL1200_.jpg",                                                                           "https://goo.gl/aTQy3I"],
    ['Bosch',           'Power Box',       199,       True,       3.7,      'Tools',        2013,           True,        "https://www.boschtools.com/ca/en/ocsmedia/optimized/full/PB360C_Hero.png",                                                                            "https://goo.gl/hUDJ1n"],
    ['PK',              'Solar Tool Kit',  158,       False,      3.1,      'Tools',        2014,           False,       "https://www.comtradestore.com/product_images/b/709/PK-2061__62077_zoom.jpg",                                                                          "https://goo.gl/nDDZrc"],
    ['Sun Force',       'Power Inverter',  319,       False,      2.2,      'Tools',        2015,           True,        "https://images-na.ssl-images-amazon.com/images/I/61jq4wNHzOL._SY355_.jpg",                                                                            "https://goo.gl/12ag9c"],
    ['GT',              'Infrared Reader', 139,       False,      4.4,      'Tools',        2013,           False,       "https://ae01.alicdn.com/kf/HTB1ugMzHVXXXXbOXpXXq6xXFXXXo/Victor-VC-305B-infrared-thermometer-Mini-Handheld-font-b-IR-b-font-Infrared-font-b-Gun.jpg", "https://goo.gl/oe42du"],
    ['Bose',            'True Sound',      299,       True,       5.0,      'Headphones',   2015,           True,        "https://www.google.com",                                                                                                                              "https://goo.gle/oetff"]
]

  
""""                          * IMPORTANT *

The program will OVERRIDE any changes that were made after the 1st write, IF
the file name is the same. If the file name changes, it will just create a new 
file with the new list.
"""

# Replace 'sample.csv' with the name the .csv file should be called (if needed)
try:
    with open("sample.csv","w") as f:
        writer = csv.writer(f)
        # Replace 'export' with whatever the variable assigned to the list is (if changed)
        writer.writerows(export)
        print ('** .CSV file SUCCESSFULLY created! **')

except Exception as e:
    print ('The following error occured: ',str(e))
