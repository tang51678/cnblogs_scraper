# cnblogs_scraper 项目

### 1. 创建项目和安装依赖

首先，创建一个新的Scrapy项目：

```
scrapy startproject cnblogs_scraper

项目结构如下：
cnblogs_scraper/
│
├── cnblogs_scraper/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       └── cnblogs_pick.py
├── data_analysis.py
└── requirements.txt
└── scrapy.cfg
![image](https://github.com/tang51678/cnblogs_scraper/assets/80816552/b3d76865-c04f-4a58-bc0c-78d56074aada)

```

在项目根目录下的`requirements.txt`文件中添加所需依赖：

```
scrapy
pandas
jieba
```

安装依赖：

```
pip install -r requirements.txt
```



### 2.运行爬虫和数据分析

1. **运行爬虫**：

```
scrapy crawl cnblogs_pick
```

1. **运行数据分析脚本**：

```
python data_analysis.py
![image](https://github.com/tang51678/cnblogs_scraper/assets/80816552/50b6ddc1-49d2-455e-9c5c-4b72089c1e86)

```

### 3.关键修改点：

1. **XPath选择器**：
   - 使用XPath选择器定位文章标题、链接、作者、日期、评论数、阅读数和推荐数。
2. **分页处理**：
   - 使用CSS选择器选择分页链接，然后通过`response.follow`方法跟随链接进行下一页的爬取。

请确保在你的项目中创建了正确的items.py文件，并且CnblogsScraperItem类定义正确，以便接收从爬虫中提取的数据。此外，还要确认settings.py中的相关设置是否正确，如User-Agent等。

