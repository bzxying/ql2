"""

time：2023.8.8
cron: 28 11,12,13,14,15 * * *
new Env('美团抢神券测试);

本脚本包括神券：
11点半，12点半，13点半，14点半，15点半的奶茶券20无门槛

抓包 ：微信打开 http://dpurl.cn/De93jW6z
抓https://promotion.waimai.meituan.com/lottery/limitcouponcomponent/info
里面的完整cookie

ck环境变量 bd_mtck 多账号新建变量或者 & 分割

卡密环境变量 bd_mtkm
发卡网：fk.bedee.top
算法接口环境变量 bd_mtsf  未填写将调用内置接口


"""

# 抢券次数
q_nums = 40

# 抢券延迟
q_yc = 0.1

try:
    import marshal, lzma, gzip, bz2, binascii, zlib;

    exec(marshal.loads(lzma.decompress(
        b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\xe0\x154\x14\\]\x001\x802\xa0hC"m;\xa5S\x08\\\xd8\xf7\x17\xa0\x87@\x96\xe0\xf8\xe5/9\xf0\xa2\x10\xfd\xbeM\xf9\x12\xa5\xc3\xaf\xd6\x9b\xa7\x98\x82\xb06\xb0^\xa38\xcfHe\xbc\xd5O\x1a\xc6->\xd7L\x9e\xe4\x97\xfd%z\xca\xa2{k\xc88I\x10\xc9!\x1f\xa1C$\x1fb#DI[\x89\x90\x95\xe5C\xa4\xa1\xb7\xda\'\xcc\xfe\x86\xdd\x03I\x05\x84\xa0(\xd3\xd0\x95\xbb#\xfe4[\xac\x17\x92\x86\x1d\xe4\xab!\x1a\xc6e:\xa0o\xee{\xcf\x11\x01#\n_c\x1efM\x88"\xbc\xb6\xce\xd8\xf0CW&\xe2\x9b\xff_\x01\xdd\x9c\xf7\xcdu\xa1\xac\x1c\xa2\xd6-\x08\xa3\x84\xf0h\x07K\xca\xc1\x1ab\xc5\xd8]b\x85<\xf1p\xb98B\xdeT\x9d\xa9\xedwO\x9e&\xa2\x9b\x95+\xbe\x0b\xf0\xa5\xc6\xd9\x16,\x11?\x06\xf6z\x1a\x99\x97\x8fj.\xa5\xce\xb3\xb3\x0f\x13\xe6}g\x0f\xbd]<\xde\x11\xb9\x8b\xf5\nj)\xa4(0\xda\xc5G\x99P\xfb\x0bm\xe6\xe9\xdfx\xedL \xebGB\xe3WN\xb2o\x80w\x0b\xe0wG\xdb\x05Y?\xb2\xc8V\xfb\xf8i{\x904\xac8\xfd\x17\x95\xc2\x0c\xe2a\xf3\x89\xc2O\xf2U\xcc\xf2\xe1B\x8d/\xcc)\xee~\xc44\xc9\xff\x15\x7f\x82\x97i\xdd\xe6w\x1f|\x18g_\xc7(\xde;p\x18\xbe\xbd\xe4\xe8\xe6\x98V\x9f\xc2\xe6\xa3p\x8f\x08B\xc1\xb6\xb9\xe09\xa9\xd6V\'\x1d\xf9_\x8a\x8a\xdc\x8f\xb5\xa1\x03\xdb\xc2R\x99\n\xed\xc0\xd0\xd0\xc8\xac\xf8X\xde\xbf\tx\xcb.n\xcb\x8e\xab3`\xd6\xca\xbb\xc2\xd8\tV\xbb\xe0bm\t\xf5\xa5$\xe9\xads\xcb\xf2\x18Mk\xc0I\xc3@\x93\xdd\x92\xe7K\xee\xe0J\x06\xdb"\xa7\xcb\xa6\xc5\x9fI[\xa6\xd6@\x05\x9a\xad\xe7_\xe3\x19\x0f\xbf\xfc\xc0\x90\xb5W\xeb\xa4\xe4\x06"\xbc\xb1W\x96\xf2\x1e\xb1\x1cHU\x08\xb6\xe8\xad\x13\x99\xc5\x83\x97M\xf7H=:\xf7_\x824\xbc}\xab(`\xa0\xb2\xd1\x1e\xe2\xe0l\xaa\xec\x93\x9f\x9eF\x82]\x97\xafrS\xbc\x122eC\xcbEU\x12\x06 \x1c\xb1\xd6k\x1f\xbf7\x12h\xe4\x01\x00\xc7\xb5\xa2r\xc3s,<a\xd9k\xdf\x13\xef5FA\x9c\x19\x9dt\x85>\xff\x98\xd4\x19ob\xe5\xec\xa3\xfa\xe2\xb2,\xfa\x96TNj\x98M=\xa3M\xa8l\x89\x0e\x81j6r\x9f\x98\xb2-p\xf1\xe2\x8by\xef\x8c\xf4\xab\xf0\xb4\'\'\xd8\xfd\xab\x06\x90Q\x1a\x14\x16\x8f3\x83C#\x831\xc0eT\x9bE\xa0\xc2\xd61\x8d\xb8vtf\xcb-\xf9~~w\x91\xf5\xbb\x04\xc6\xb0Q\xd7\xf2\xae\xd3\x13?\x16\x83\xed\xff\xb6\xaf\x05G\xf7e\x1d\xfa\xddu\x91m\xfb\xb4PU>!l\x05\xdb:\xe7\xea\xd6\xe0\x02\x10C\x89\xac\xdc\xee\x03\x92xU\xbd\x15\xe5v\xe5x\x0e\x0e\x8c\xf9\xed\x80\xe4\xaa\x07N\x9b\x11\x0b\x03\xf7\x91\x99k\xcdh){V\x82D4P\xbf\xa7\xf5\x06\xb4\xe5Q\xf2{%j\xb9M@/tv\xa2\xcf\x08 !Y\xb5\x05\x88f\xbb/\xa0I\xdf\xe9\xfah=y\x97|\x96\xfa\xffh\xafm\xb1,\xe5M\xca\xb6\x99\xd5\xda\xd7Ee\xa5\x81\x8bB/Ci\x1b\xf8Ix\x93\xb4\xf7;s\x10\xfc\x1cZ\xde\xfb\xaf\xed\x121\x1f\x1b\x01\xb8\xd3\xf23\xe8\x8e\x19j\xf2\x0c8L\xdf\\\xfb5Ii\xca\x1f@\xb08\x9bb[\xc2\xe6\x0f\x81Sc9 FvM\xe2\x82\x99\x99/OK\x10v\x8c\xdfV\x9f\x81o*\x81\xf06N\xf5\xcf"jOi\xb2\xf1\xd1\xea\x0f\xdb\x1dio\xc4\xd6\x91\xee\x8f!\xfe\xcb`\xa7\x04<\x04QZ\x9ej\xbb\x13\x00h\x0fI\xbd\xcb\x8efu\xa3\xd4J\x07I`L\x08\xb4\x96%\xf0\xc7\xf4\xa7?\xb3\x80\xe1\xc0\xbb]\xcd\x0f\n^\x1eKmD\xeet\xf9\xad%\x17\xfaC\xb4x\x0fvP+T\x1e\xeet\xd9\xac[\x0c\x1c\x7f\xa5\xc6\xd9\xcf\xe2d\xa1 \xd5{\x1b\xfe\xc8\xd8\x93=\xff\xfc\x9dK\xfc\x85\xc1\xa9\x9e\xdc\xf0\xf8p\xb2\xc7\xb9J\x16E\xb8\xaa\x91I\xb0py"\x8a\xdf\x94I\x05\x98\xc9\x1b\x07g.\'\xe2yUR\xae\x1d\xda\x82~\xcd\xcf6\x0e\x83\xb5\xeb\x8e\xdag\x13\xd9Z\xc1\xe9&f\xb9\xa1#\x12\xd8\x0f^\x1f\rd\xf5@\x92\ny\\\xd4\t\xd6\xd2\xa3\x9b\xb4\x8a\x01\xf0\xfe\xe3\xd0\x9a\x05\xf4\xb9\x17\x99\xcfI8\x07\x9c\x0b%\xa0>\xce,\xa4\xac\xd8)`\xac*\xd9`|-\xc6\n\x8a\xaf\xe0Q\xcc\t\x80H\xb4\xb7`\x12\xda\xc0Ap\xf8E\xb4\x94\xdd\x0ce\xd9\xae-8\x80k\xab\x94v\x9e\xa6\xd7\xe2\xe3T\x96\x0c\x19>\x8b\xd5\x13(U\xc6\xa2\'\x10\xf0R\x9e[\x94y)\xa1v\x9fn2\xb3\xab%~\x1e\xdc\x05\xba\xbd\xf4]\x0b\x06\xc8\x06\xd9\xc8XRu}$\t\x83\xcf;R-\x9f\xb4\xd2\x95\x9a\'Q\x02\xdeX\xe2\xbat\x916\x8eu\xba\xcc\xf3\xad V\xefC\xc1\xc9\xca\x1d(<\xbdY\xdb \xf5\x1f\x94\x85\xce\xdf\xadr\xd9\xa4|\xbcR\x92Gn&\xbf\xb2\x8aJ\t\x86z\x94`\xed\xcf\xfb\xafy2\x9f\x15K}\xd6\x15\xffIA\xe59r\xfe\xcd-\xa7\x06rSw\xb7\x025\xbc~4\xca04\xa3\x82\xa3\xf8@\x17\xa5\'\xc1\x16\xc2\xdab\xdd\xc7\x9c\xda~\xf6\x9b\xba\x93\xdc\x8aF\xe7\xfe\xc1\xd8\xd6\x837\xba\xcf\xda\xc4\xbe\xedx@cB\xfat\xdcZ\xdb\xdfI\x9b(\xef\xb7i\x04\xed/\x8b\x8drI\xd0\xf7\xa8\x98\xe6qg\xe0$\xbf\xbfJ\x94-r\xc3\x83\x1b\xebY\x8d\xb2n\x80\xab\xeclx\x04\xa1C\xac\xb97N0\x07\x8b\xc38\x8b\xf5\xdb\xdf"$z\x15\x8dT\xc77\xde\xef"\xd76\xd9\xd7\xb9}\xa9\xbe\x92\xe0(\x1a2\xb57k\xe33\xa7\'Tl\x8e\xd9\xc8\x9c\xfd\xd9\xe2B+1\nS^\x86+\xf3\x18\x11!\xc0\xedx\xa4\xc0\x8a\x0e\xfd/\xa7\xd8\x00<-\x82\xe5<&\x14\n\x86\'\xb7\x18m\xa0\x13\xc7\x15\xafO\x9fx\xbaM\xf8gb\xf4\xd2\x02\xc5\x14R\xa8\x9ca\x14\xc6\xb9+K>\x80\xdc\xd6\x14\x1fz*{\xd4\xfe#\x9d\x94w\x03#\xa3\xde\xd3\x16\xdc\xa6\xcf\x1b\xcd\xbb\xe4,\xd5`\xb9t,C\x9a\x7f|\xc8\x17\x19\x9bs\xb62\xea\xc7\xd0c\x82\'x\xfd\x94[\x8cm\xa9\x0f:\x8a`\x8b\x82\xe25\x7fq\xd2\x8d\xb1~h\xf0Cz\xd7\xd8y\xdbl\xb5g\xf6\x1e\x9f.\xc2\x17\xc5\xd8\x1e7b\xae\xbd&9\xeb\x92d.\x9c\xb4\xfd\x88\xe6\xbc<\xe6"Y\xed72\x9ch\xa6\xda\xd3W\x94\x7f\xf0f\x89\xb3\'\x0e\x18(?\xd0\xaa\x1a[\xda\xfclB\x90\xbea\x8c?>?*\x8d\x15\xa6\x1eZ\xb0\xb1\xf3\xd9\x9c\x00\xa1\x9b\x0f\xc7\xde\xfdR\xf3\xab9\x12\x9f\x02\xfa\xc4J\xee&\x8e\x0c\xe9\xadbe`6\xba\xbf%t\xeb\xbcp\xdbX\xd1\x0c\xdc\xe1%\xe3\xef\x16\xd0<\x0c\x9c\x1b\x94@\xc6f\x8eZY\xb2*a\x02\x84g\x8d\xe6@d\xf4<\xba\xe9\x8c\xb7\xad\xc3\x9eW\x81\x0c6\xb9\xca\xf8\x173\xc0\x92\xcd\xe4 \x10\xf3\xb1\x8e|r\xc2c\xf4\x8c\xc4\xa96\xd2\xf9\xd8b\x8b\xa8g\x92\x01\xa6\x06f\xcf=\xe4#\x1d9\x9f\xbb\x0e\xcd\xc9\xab\x93\xc20\x81\xd3\x91\x04\xda\x98\x16\xef\x8eB\xa8\xb5Ye\x052\xfcyf?\xf5\xfc\xcf\x1e(\xd7\x00\xf8\x8f\x1c\xca\xbcM\x99\xf7\xe1\xdf-\x19GI\x96\xa1Eo\xad\xee\x1dy\xff^\t\xe9`G\xd9K\x89\xe8;\xe7\r\xe2aq28u\xd5\xddJ\xc6g\x98\x84i\x9a\xc8\nE\xe2\xdf\xcde\xd5g\xbb(A\x83Y\x19\xe2\x9f\xe0\xb6\xef~"\xa3\xb10\xb5\xc9^\xae\xcd\xe6\xb9\xdam\x8d\xe2\xe6"\xb2\x9b\x9e\xc1\x14\xa5\xd6\x952y\x97\xe3\xcbC\xf2\x93-\x19\x1d\'\xd5\xd0t\xe5\xb7\xe2\x8b\t\xf0\xde\xde\x8epM\xf2t@\xae\x9d\x1b:XJ\xa5Tt\xfb\xf51\xcb\xd5\xa5\x02\x8fv\xb1\xaa=;>\xd84\xd5};u6\x1e\x18\xdeqE\xc5if\xfe!Y08c\x0b\xbb\xd78|rR\xdb\x97p\x01a\xfeQ\xee\x98M\xad]\xb4q\xc6\xc8\x82\xec\xc0HuR\\YE~\xa7\x8e\n\x92t\xcc\xbf\xaa\x9cS\xa0\xcd\xeb\x8bC$`\xf6\x90\x80\x08\xb6\xb7\x84\xf8\rpQ$\xc7\xb9\x183\xacjsK\xccT\x9c\xa1\xcb\xe2\x91\xb2&\x11\xceT~\x9b\xef\xf4\xc1\x0b%\xf2\xf1\x05/\xd1\x9f\xe7"(Y\xf7r@\xa0v\xc3t4\xb5L4\xa4\xe5\xd0\x00\xdd\x13\x94\x9fU\xc2\x0c\xbcL5?\xc9\xfa\x99\x82\x82\xc7\xce\xf6\x92\xaf\xec\xea\xcf\xcf\xe0\xda +\xd7\xae|\x85\x15\x84$F{\xf7D\xdd\xb2\xca\xb5\xd4\x88)\x83#3Z\xf6\xf8\xb9K5\xc3\xa0\xa9\xb7\xa4\x12\xba\xd8:\x1c8\x19$\xc5\xf3/\x92\x9b$~2\x96\xa1\x15\xf2b\xaa\xe4\xab\xaeP\xc7\xb5\x83\xe2y5\xcf\x97\xe9:\xbc\x83f\xadXH\xe4z>\x1d7\xc3\xa5\xce\x1f8\xe1\xf9*\xf5$\x82\xdeY\xf3U\x82d\xfcRN\x1c\x8bMu\xef\xe5\xf7\xd1\x8d\xdf\x86\xda\x00\xb7\xfeTK\xde\x03z_\x15\x9d\x1c[\xeenl\xd5&5\x81\xff)l\xbcK\x88,\x8a\x0em\xb2r\x11\x0c\xda\xffo\x96,\xa4N1\xc8\xad\x80\r8\xdfuH\\i\xa7\x7fzUh\xdf\xeb\xb6t\xa0A\xc3\xd3\xe7\xb4~\xb5\x8d\xe4\x9b\x9a\xb3{~l%\xc8\x0b\xe8\xcb\xf3\xe0\xa7uI\x80\x8ae\xd1\x1d\xf2\x98\x81.\xfd\xe1\t\x08H3\x9b\x164\xd5#\x84\x96\xba)\xe7\xc8d\xf7\xb3R\x8b\x7fP\n*\x18n\xb0NR\x0eS\xaa\xcb\x06\xa5\xaa\xa6F\xcb\xec\xecnO\xfc\xa4o\xd6\xe8T{\xe9\x1d\xb0\xb8\x9d\x08\x16\xd9\xbc\xb0\xd6\n+\x82o\x87\x8b$\xaf\x07S\xa8\x81"\x01$\xd7>WD\xf2D\x1c\xf7\xe2\xa9\xea\xfb\x1c#\xee\x89\xefe\'E\x7fr\'\xcf\x8f\x8f\x91E\x00)(\xe0\xe7\xcb>\x1a\xcc?\xbfms)\xdd\xd6\x16\x97\xb9\xf0*\xb0\xbb\xf8\x9e\x8c\xb3\xe7\tvq\xc8}\xc82\x9a\xe6K\xac\xb8K\x10Y\xa0\xed.\xbem\xb7\x9c\xdc\xb8\x0b\'\x15\xces\x83\xe0\xab\xe6\x99\xaa\xddu\x95\xe3\xfa\xcb\xd1\x99ei\xba\xaa:\xd8\x97\x9d\xf7\xf2\xc8\x0e\x1b\xa4\xa7`\xf4\x14\x0c}"W\x7f\xd2\xa3\x01"&\x15\x18!\x15\xad\xe4}\xb3\xcf\xf3\x02\xe4},;\xad\xfe\x16fQ\xef\xe7\x0b\ra:\xb5\x8c\xcaN\xc1\xf2;\x8e\xfd\n\xcd\x1e\x02\xff\xa1/\xe3\xd8\x13t\xbe\x82\x8e|\x8fL\xc2\xabr\xb9\xa3\x0b\x90\x89\x9d\xc0\xa0\xcd6 \x17g\x83I\n5\rV\x0c\xf6\x95\xf0\xf41qq\xc8\x9b\xd9\x9b\xedq}@\xfa\xb5H\x024\xa8\xef\x9b\x9b\x9c\xbe\\\xfe\xe7%/Xhr7Q\xc7\xd9\x01\x96\xa2\xf2\xc0r\x16\xbd\xc0\xb3\xa1\x14*\xf2r\x81\xfe\x99\xe81Y&P9\xfa\xabB\xdb/\xffuzs\'\xf0\x02\xbbn\x83O\x90\x9c\xc9Jt\xf0\x92F\xf9\xb2>\xc8rdt\x82~\xf4<\xb8\xc8Z\xd6}\xbcu\xa2\x9b\xe5\xaf\x9c\x85o-\xa1\xe1\xc7\x02\x98\xf9\x9dz\xe8w\xe0Y\x89\x14Ir\x9d\xfe\x01\xe5\x8a\xe6c\x96\x02\xe8\x99\x11\xf0I\x9e;lh\x89\xea\x86\x01\x87!\xb6E\xa8F\x1f,\xb9\xed6xq\xf4\xbd\x8d\xb2\xd4\x9cK\xd3-\xac\xfc\x97\xf5\xbd\x82p\x9fVn\x08\x9e\xb6\xd1A\x10\x07\x88\xee\xbd|\x95W\x7fo\xa4#=.N\x00\xf5R\xf0T\x12o}\xe6\xb3\xaf\xbb6\xfdF\xb90\xb2&N\xe6\x1b^Hz;\xb09\xe0\x99S\xbc\xb4\xa4\xb9\x1d\xa0\x809\x95\x0ei\x9f\xe3\xedf\x8fh\xf1\xc8a;\x1f\x1b\x1f\x8d\xc9f\xa2\xd8\xa2`=L\xa7\xd3\xa4\x19\xd8\x83\xc9\xe2\x83\xe7\xc4o\xd5\xa4\x1f[v\xa7\x87u\x06\xfa\x01\xb4\x1c\xab\x08\xba\x98\x85|\xc4\x90\xf3\x1b\x02\xf8iB\xbf(\xc2\xc8To\xef\xf1\xa5\xf4\xa0\xc6l\x081\x0b\xcc\xe6]/\xabex\x08#\xc8t\xee\xaa\xd246}H#\xfe\x14Z\x04\xcd\x15]D\xe3\xf6\xaf\x9f\x07\xe9O-\xa0gMdt\x07\x9dL\x1b8\xee|\xfa[\xce\x8c\x93\x92!\x99\x93\xc9L\x88]\x10\xaa\xcd\xf7\x8e \xea(\xe1U)D\xfb\n\xb3\xce\xaa\x0e\xab1t\xe4\xda\x1d}w\x08<\x8b^Ryd\xcf\xb0sM~\x92E\xc0\xe3zA,\x83?\\@\x17ME\xd7\xce\xd5\x05n\x05\xf5[j\xb7.5\xee\xb7\xb88(\xb3\xee[\x87\xc1\xfc\x8f\x8c\xb4_\xe9r`)\xb2\xc1#\x15\xf6u\x92gE\xca\x8a\xd9<\xcf\xfbp\xa4%9ul\x03S;\xc0z\xc8\xa3\xa8\x08\xf0\xc3\xac\xbd$\x9cs=N\x11G\x93FK\xef\x17\x80\x8c\x96r\x9f\xf7\xcf\x001B\x90pH[\x15\xea\xceU_\xbb\x15\x0b\xcd\x07\xf4:?~\xd5\x80{\xc17x]^%\x8e\x90n!\xb2v\r\x06\x11\xad\xa9\xa4IC`\xd6L\x9cx\xe7\x9a\x83\xf3kb\x8d\x89\x80\xcbP\x8eL\x9b8H\x0c6b\xfa\x13\xa5\x90\xf9\xfe\xe6\xcf1\\\x9d,i.\xef\x1cE\x99\x1c\x8b\x01 \x9b\xc6\x91M2N\x15\xb5B\xa0\xf2J\xcc\xb03aI\xea\x0b\x00\r_\xc4\xd3\xa45?Vw~p\xab\x8e\xeb\xa5d\xd5\xaa?\x07\xcdi\xe3\xa8\x9e|yY\xcbm\xe4\xdb4f\x86\xce\x00L\xcb?\xb7\xe3T\xc8\x88\xa5\xc3E\x928\x15g|\x96\x82y\x05l\xfaq=\r\xe8\xb4\xe4A\xae\xec\x193\xe6\xc8!\xa2d\x93\x8e\xd1\xcc\x96H]n\xb0:\xc2\x96pSB2\x94^$n\x15p\xdc\xc9Nk0J\x04\xbe\'\x95\xabE\xdbl\x1b\xa8\xc3Kb\xe0\x123.\x933\xc5\x9f\x96\xbe\x15\xfc\xb6S\xf0\xd2!\x88\x1b\x16\x1b\x1f\xe6w\r/\xc7\xa8\xaf\x9a\xfc\x88s\xf7h\x92\x8bY\xa7\xb3\x18\x01g4\x9bs`\xfa\xe0R\xf0\n\xe4\xa1[u1\xb8e\xc1~\x1e\xcav^M\x97\x0eg\xbbS\x9b\x15An\xa3\x14\x11\x87X\t\\W6\x05\x97\x14\xfc\xe0\xcc \x1aJ\xed#\xa1\x8cf\x03"h\xd7\xc3\'\xdfa\x1c\x8b\x8f\xf5\x9f8\xb8K,,u[$Z\x11=\x18T(\xe4\xa6\xedc\xea\x9d\x86\r\xa63\x01_\xd5t@\xc2\xd4\xb3m\xcb\xc5\xdeS\xb2\x9c\xb0\xd4|4s\x9a\xef\xb7\tGM\x02^{B/\x0e\xcb\xb2A\xc6\xa5\xc87\xb5\x92\xe7p\xddd\xbfH+)\x84<\x91\xb3\t\xed\x96\xbf\xbe\xdd\x99Q\xeb\x14|:j\xf6Q\xfc\x16\xee\xb8\x02\xa89\xbb\xb8To\xca1\xe9x\x7f\x88\xe5p\r\r\x82\xf7\x0bT=1\x84\xe7\xa5K\xab{!q\xce"{\x0c\xb2\x9c\xd8\xb8~@%SY\xa8$\x9c\xc5K}\x8e\x7fP|\xb6\xd5\x9d\xa5\x92\x8f\x8f\xf1\xab\x92\x02WT\x85x=\xc9ZB"\xa6l\x8e\xf1B\xe9\x9bn\x89\r\xd2\xa9[[}\x9e\x83)\x8a\xbb\x12\xee;\xa9\x03\x8a\xe9\x90Nn\xe2\x13WU\xf5\xab\xd8n\xa8\x166\x1d\xecX\xa7F6\x7fQ\xaf\xdcr\xa6\x1f\xf4\xc7\x07\x83j\xa7\xab\x94\x8c}\xc1\x15\x82\x86\xde\xad\x85\x07\x12\'\xf0<v\x03\xd4\xb2\nz\xf7\xc9\xd3\x0bw\x7f\xf6(\xcec\'\x94\x13vJA\xd3\nF\xb6\xa5\xf1\xae\x84A^\xf2\xfbK\x1fW8\xb1[b\xa1\x9a\x93\xab\xab\xe1\xb9b\xe6\xc8\xbe\xec\xd9n\xbd:\x85\xa6\x12\xc0\x17\x08\x01\x0enS\x06\xe9\xcd\xcdT\x84\x85\r\x1c\xe4\xcb\xa1\x18\x1c\x00WtO(n\xb7\x1d\x9eFY\xbbJ\xf3\x1cG\x91\xb0\xe3\x1fu\xef\xac_W\xd0\xa6\xa9\xb7v\xfb\x87\x97\x00\x9fr\xd6!\xdah\xf0\x94\xf2AF\x8b,4\x04n\n0\xect8-\xdb\x16\xa4\xf5c|K0\xbc\xbcsW&\x02{n#\x0b^\xd1\xf7>\xa2\xc9\\_\xd05\xac\x88}H\x11 9\xfa3:[8Mv\x9a\xa3Q\xb8\xe9er\x8a\x89+I\x9d\tV^3U>\xe2l\xd1\x8b}\xefx@\xe5\x81^\xf5P)m\x14/\x97\xbb>\x9d\x03\xd5\x07\xdfb\x0e\xa7\xb7\xb4\xfa\xf4\x07\x9aT\xf3\x9b\xb5/\xfbo\x915s\xea\xf6&o\x13\xbaG)\x97\x86\xa1\x1a\xdbM\xf8p\xf8\xbc\xe3\xd8buF\xb3MW\xa8P)\xb0\x8f\\\x90\rZ\x0b}I\x08\x11\xe7xa\x0c&\x93\xa5\x03\x93d\xcd\x19qMr\xde\xc25\xa4\x80|\xa5-\xbe\xde\xb6P\x86@\xa9\xae \x9a\x98\x80\x0ex\xc1Y\x97\xa8\xc9\xa4\xdbfNt\x00\xfa\x01\x9ff\xb7/\x88\xf8\xe6\x8f\x8a+q<q\x8b\xe8B\xc7&\xb8\xf6\'\xa9\x1c\xc6\x89+bm\x9b\xcb\x88\xc05..\x93e=\x1f\x03\xaa\xb0\xbd\xee\x84\xf1\xd8\x9fb\xa1nb;m\x88\xb2\x0e\xf4C\x86\x8d{Z\x01szIa\x8b\x0f5M\x8aq\xf8\x9b@\x06\xe9\xa3P\x9e\x9c\rs\xc197\xcb~p\t\x18\xc3\x9a\xb1\x98\xc2|>$\xf1\x13\x1f\xbb\x15[\xd3\x14z3\xd3YK\xbb:\xe9t\n\xf2\x94Z#t\x1774QRd\xdbw\xad\'\x0e\xfe\x7f\xf6\xea\xa0\x0cw3\xc5Yr\x18\xbf=\xdb8\xdf\xa0m\xf0\xa8\xd8\xdc\xdb\x005j\xbd\x1cz\xf4%p\xf7\xe2\xc3\xf6\x95\xb5\xbd^\x8f_\x87y\xb2\xf4\xa4i5\x19N\x05\x90\xd1a\xed\x14\x0b\xe61\x1c\x06\x96xmipf\x8d\xfb\x9aP\xee\xcb\xe2\xd1Ttt\xad\xbfr\xc8\xb1\xad\xf2\\\xd0\x95\x06A\x19\x05\xc2r \x86\xfc\x8d\x88(\x91\xff\xca\xbd\xd3\x81\xbeJ\x9e\xc0\xe0_k)\x01UU\xf3d\xa5\x1a\xdc\x8cE\xabe\xf8l\x90\x89\xc5T\xcc\xf5HWa\x08\xd0|\xf9\x8b\x9d\xb1\xb9\xf4 \xab\x9e\xda\xc7\x8d>\xc8\xc6e\xe9E\x15\x9f\xd35\x8e\xc9]\xc6\xf4&I\xd0;\x8a\x96\r\xcaYz,\x15R\x8d\x83R\xfc\xf1V\xfc\x9e_\xc3\x95\x99\x8c\x1a\x10\x94\x11\x99\xfa6\x9c\x8d\xad\xe9\xcf\xeaOR\xbfA\xfb\xf3q\x06;\x8cm\xc5\xaf\xf4\xdd\xc20\xe8\x852\xccI\x1aC\x94\xae{q\x12O\x19\xafmB\xa1G:\x10\x9b\xbb@f*\x193\x8cg1\x12\xe3\xcc\xdd\x80\r\xe7u\x9dK)\xb8\xb9E4c\xcc\xaf}\\Ge\xa5\x9eE\xd4\xf6\xa4C\x0f\x16\xb1B5\xfb\xe7bB\xa6\xdc\xeb\xea\xccYlO\xff\x94*\xb2\x18-\xa1\xfd\x11\\\xf5\xc5\xe0\x07\xb2\x9f\xea\x85\\\xb5:[5w.\xec]Y\x84_sCDH\xc4\x88\x91\xec\x07\x19{\x9d\xef5)\r\x1d[\x85\x15\xa2\x95\n\xbd<\xf4\xc4\xbd\xfaxE\xacm\x94Z\xa2\xc1\x89V\x04\xdd\xf5\xe9KJ\xb3~\x948J$\xcfK\xb4wd\xbary\xc1\x91\xab!=\xaf\xc2\x11\xda\xcdA,\xa2\xf8\xcd\xb0\x93\xa5\x13\x80\xdb\xc00\xb3\xd1\x96\xce"G\xd5-\xc8\x14\xe1\x96Nm\xf0g\xe0\xe0\x1b\xde\x03\xe0\x06\xf4k(\xe4\x06\xfe\x8f\xbfw1\xa7\xad\x00\xbf\xfc\x925>\xfe/X\xf9X\xaf \x98\xfb\xcf\xfd\xb1f\xb8x\x81q\xd9\x1f\x9b\xc3\x9f\xe3\x82\xa41H\xe9C\xb0%\xca\x00n\x83%\xe9\xd7bdZe\xa6\xe5\x81\x9bL\x1ef\xd3\xcb\xdd\x86\xed5\xdbY\x19\xf6\xe8w\xd7\x19u\xcd\x1c|\xa4\xb7\xd5\x90\x8fYB\x04Z\x18\x02\x8d\xe8f\xc4\xb2\x08(\xe7r\xabP\x86>L\x10\xcc\xff4Q[R\xbb#\xea\x8bc\xe2\xf8(!4\x1cv\xf7\xe1\xf2\xdb\xe4\xc7\x96\x1eOH/a\x7f\xa6q\x89\x01\xd8J\x08N\xaa\xc1=cB\xa9\\\x84\xb3\x1c\x91\x1bt\xc5\x87\x05\x8d\xc8\xc9z<\xf6\xb7\xcb3\xe2\xe0s\xc5\xb3\x0bna\x06\xd6\xb2x\xfeD\x87\xbcaz\x0e\xaa\x1c\x08\x82R\xe3\x1e \xa1%\xf9\xb7\xde#\x91u\xd1\x99j7\xbb\xccaJ\x1d\xcd\xebr\xe4\xc5\x8fX4\xd3o\xfb\x8em\xe8\x97F\x1d\x03\x1a\xe8\xa3\xf2\xf9\xf4\x15\xc3\xd3\xc2\x11\xd7\xefo\x06L\x94\x8b\xd8\xc7C\x0c\xb1\xf4:\x08\x8a\xa9\x07zv\xc1.eUh\xa1I\x9f\x1b\xae;\x08<!s6\xac!u\x87\xfd\r\xc3\xdf4\x0fy\x9cR\xabm\xa8\x96]L\xbeb_\xbb\xf1\xd8\xdd\xf1\x0c\xf7\x12[\xdcn\x8b\xe4\xd6\xb2\xdcAd\xe5\xf7\xad\t\x1bB\xf9=\xd3\xd9d\xcb-(Y\xd0;r\x14\x88\xe0\xb2q\xcb\xddK\xc6P\xa45\xd0\x8dx\xb9m\xfa7\x82\xb9\xfd\nW\x9f&\x12\xc4*\xd4\xbd\xbc\xcc\xd8mFv\x90\x1c\x85\x06\xd5\xec(\xb5\xaf\x81l\x9d\x12\xcb!\x83\xa6}\xcfL)1\xba\xde\xfd\xe7\x97\xcbw\xa4\x93\x19\xdbT\x96=Y\x89\xae\xe0G\x85\xdbd\x88\xf5z\xb7\xa3w\xe2\x16\xb5\xc4\xc6RV\xa1(\\\x8c\x06>\x80\xe8\xa7\x81\xddt"\x0b\xcb\x86H\xde42\x83(\xfe"\xf6#)\xf6q~4\xa8\xc8\x92\xebv(\x92\x8f\xe8\xd4\xce9\xb4T\xe0\xfd\x9b\xc3\xcd\'1\xa0\xf8\xa1\xe0\x02\xc70A\xd9zcP\x03\x14\x07i\xa3\x1b\xac\xdf\x1fu\xac\x10p\t.\x18\x15Q)w\xd1\xb9\xea\xa4\xddO\xd6\x99\xe4\x12\x9f\xb0e\xe3\x9d\x82(\x98\'\x0f#\xe1\xabN%\t\x85\x81\xfd\xc2i\xd7\xed\xc8\xbe\xd46\xfc+\xd6\xb2I\x18^\xca\xfe\xe8\xfe\x18p8m\xdd\xef\x8b\x18*Ka\xa1\x10\xe4dk\xce\xa9K\x14\xa1\xcf\xfa\xc0\x00i\xf8u\xbe\xf7&\xa8\xfb\x00\x01\xf8(\xb5*\x00\x00\xf2VS\xd4\xb1\xc4g\xfb\x02\x00\x00\x00\x00\x04YZ')))
except KeyboardInterrupt:
    exit()
