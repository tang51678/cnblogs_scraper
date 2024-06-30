import pandas as pd
import jieba
import jieba.analyse
from datetime import datetime

def load_data(file_path):
    # 读取CSV数据
    df = pd.read_csv(file_path)
    if df.empty:
        raise ValueError("数据文件为空，请确保爬虫已经成功爬取数据。")
    return df

def preprocess_data(df):
    # 处理空值
    df = df.dropna()

    # 将views和comments列转换为整数类型
    df['views'] = df['views'].astype(int)
    df['comments'] = df['comments'].astype(int)

    # 将date列转换为日期类型
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    return df

def extract_keywords(title):
    # 使用jieba分词提取关键词
    keywords = jieba.analyse.extract_tags(title, topK=5)
    return keywords

def get_top_author(df):
    # 统计发贴量最大的作者
    top_author = df['author'].value_counts().idxmax()
    return top_author

def get_latest_article(df, author):
    # 找出该作者的最新一篇文章
    latest_article = df[df['author'] == author].sort_values(by='date', ascending=False).iloc[0]
    return latest_article

def main(file_path):
    df = load_data(file_path)
    df = preprocess_data(df)

    if df.empty:
        print("数据文件为空或数据处理后为空，请确保爬虫已经成功爬取数据并写入文件。")
        return

    # 找出阅读量最大的一篇文章
    if df['views'].empty:
        print("数据中没有views列或views列为空，请检查数据。")
        return

    max_views_article = df.loc[df['views'].idxmax()]
    keywords = extract_keywords(max_views_article['title'])

    print("阅读量最大文章的标题关键字：", keywords)

    top_author = get_top_author(df)
    latest_article = get_latest_article(df, top_author)

    print("发贴量最大的作者：", top_author)
    print("他的最新一篇文章：", latest_article)

if __name__ == "__main__":
    main('cnblogs.csv')
