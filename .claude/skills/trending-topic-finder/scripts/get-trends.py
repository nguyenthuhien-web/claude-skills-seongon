#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script lấy dữ liệu trending từ Google Trends
Sử dụng thư viện pytrends để phân tích xu hướng tìm kiếm
"""

import argparse
import time
from datetime import datetime, timedelta
import pandas as pd
from pytrends.request import TrendReq


def get_arguments():
    """
    Xử lý arguments từ dòng lệnh

    Args:
        keyword: Từ khóa hoặc ngành cần tìm (bắt buộc)
        --country: Mã quốc gia (mặc định: VN)
        --days: Số ngày lấy dữ liệu (mặc định: 7)

    Returns:
        Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="Lấy dữ liệu trending từ Google Trends",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ sử dụng:
  python get-trends.py "điện máy" --country VN --days 7
  python get-trends.py "iPhone 16" --country VN --days 30
  python get-trends.py "AI" --country US --days 14
        """
    )

    parser.add_argument(
        "keyword",
        type=str,
        help="Từ khóa hoặc ngành cần tìm (bắt buộc)"
    )
    parser.add_argument(
        "--country",
        type=str,
        default="VN",
        help="Mã quốc gia (mặc định: VN)"
    )
    parser.add_argument(
        "--days",
        type=int,
        default=7,
        help="Số ngày lấy dữ liệu (mặc định: 7)"
    )

    return parser.parse_args()


def fetch_trends_data(keyword, country, days):
    """
    Lấy dữ liệu trending từ Google Trends

    Args:
        keyword: Từ khóa tìm kiếm
        country: Mã quốc gia (VN, US, v.v.)
        days: Số ngày lấy dữ liệu

    Returns:
        Dict chứa interest_over_time, related_topics, related_queries
    """
    try:
        # Khởi tạo TrendReq từ pytrends
        pytrends = TrendReq(hl='vi_VN', tz=420)

        # Tính toán khoảng thời gian
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        timeframe = f"{start_date.strftime('%Y-%m-%d')} {end_date.strftime('%Y-%m-%d')}"

        print(f"\n📊 Đang lấy dữ liệu trending...")
        print(f"   Từ khóa: {keyword}")
        print(f"   Quốc gia: {country}")
        print(f"   Khoảng thời gian: {timeframe}\n")

        # Xây dựng request cho Google Trends
        pytrends.build_payload(
            kw_list=[keyword],
            cat=0,  # Tất cả các thể loại
            timeframe=timeframe,
            geo=country,
            gprop=''  # Tất cả các thuộc tính
        )

        # Xử lý lỗi 429 Too Many Requests
        time.sleep(2)

        # Lấy interest_over_time: xu hướng tìm kiếm theo thời gian
        try:
            interest_over_time = pytrends.interest_over_time()
            print(f"✅ interest_over_time: {len(interest_over_time)} rows")
        except Exception as e:
            print(f"⚠️ interest_over_time error: {e}")
            interest_over_time = pd.DataFrame()

        time.sleep(2)

        # Lấy related_topics: chủ đề liên quan đang tăng
        try:
            related_topics = pytrends.related_topics()
            print(f"✅ related_topics: {len(related_topics)} items")
        except Exception as e:
            print(f"⚠️ related_topics error: {e}")
            related_topics = {}

        time.sleep(2)

        # Lấy related_queries: từ khóa liên quan đang tăng
        try:
            related_queries = pytrends.related_queries()
            print(f"✅ related_queries: {len(related_queries)} items")
        except Exception as e:
            print(f"⚠️ related_queries error: {e}")
            related_queries = {}

        return {
            'interest_over_time': interest_over_time,
            'related_topics': related_topics,
            'related_queries': related_queries,
            'timeframe': timeframe
        }

    except Exception as e:
        print(f"❌ Lỗi khi lấy dữ liệu: {str(e)}")
        import traceback
        traceback.print_exc()
        return None


def process_interest_over_time(data):
    """
    Xử lý dữ liệu interest_over_time
    Tính toán mức độ tăng trưởng và sắp xếp

    Args:
        data: DataFrame chứa interest_over_time

    Returns:
        Sorted DataFrame theo mức độ tăng trưởng
    """
    if data is None or data.empty or len(data) < 2:
        return None

    # Loại bỏ cột 'isPartial' nếu tồn tại
    if 'isPartial' in data.columns:
        data = data.drop(columns=['isPartial'])

    # Lấy cột dữ liệu đầu tiên
    col_name = data.columns[0]
    values = data[col_name].values

    # Tính toán mức độ tăng trưởng (% thay đổi từ đầu đến cuối)
    first_value = int(values[0])
    last_value = int(values[-1])

    if first_value > 0:
        growth = ((last_value - first_value) / first_value) * 100
    else:
        growth = 0

    # Tính giá trị trung bình
    average = data[col_name].mean()

    # Tính giá trị peak (cao nhất)
    peak = data[col_name].max()

    return {
        'data': data,
        'growth_percent': growth,
        'average': average,
        'peak': peak,
        'first_value': first_value,
        'last_value': last_value
    }


def process_related_topics(data):
    """
    Xử lý dữ liệu related_topics
    Sắp xếp theo mức độ tăng trưởng và lợi ích

    Args:
        data: Dict chứa 'rising' và 'top' topics

    Returns:
        Sorted DataFrame
    """
    if not data or len(data) == 0:
        return None

    topics_data = data.get('rising')  # Chủ đề đang tăng

    if topics_data is not None and not topics_data.empty:
        # Sắp xếp theo 'growth_percent' giảm dần
        topics_data = topics_data.sort_values('growth_percent', ascending=False)
        return topics_data

    return None


def process_related_queries(data):
    """
    Xử lý dữ liệu related_queries
    Sắp xếp theo mức độ tăng trưởng

    Args:
        data: Dict chứa 'rising' và 'top' queries

    Returns:
        Sorted DataFrame
    """
    if not data or len(data) == 0:
        return None

    queries_data = data.get('rising')  # Từ khóa đang tăng

    if queries_data is not None and not queries_data.empty:
        # Sắp xếp theo 'growth_percent' giảm dần
        queries_data = queries_data.sort_values('growth_percent', ascending=False)
        return queries_data

    return None


def print_results(keyword, country, trends_data):
    """
    In kết quả ra màn hình dạng có thể đọc được

    Args:
        keyword: Từ khóa tìm kiếm
        country: Mã quốc gia
        trends_data: Dict chứa dữ liệu từ Google Trends
    """
    print("\n" + "="*60)
    print("📈 TRENDING TOPIC REPORT")
    print("="*60)
    print(f"🔍 Từ khóa: {keyword}")
    print(f"🌍 Quốc gia: {country}")
    print(f"⏰ Khoảng thời gian: {trends_data['timeframe']}")
    print("="*60 + "\n")

    # ===== INTEREST OVER TIME =====
    print("📊 [INTEREST OVER TIME - Xu hướng theo thời gian]")
    print("-" * 60)

    interest_stats = process_interest_over_time(trends_data['interest_over_time'])

    if interest_stats:
        print(f"Giá trị đầu (ngày đầu tiên): {interest_stats['first_value']}")
        print(f"Giá trị cuối (ngày cuối cùng): {interest_stats['last_value']}")
        print(f"Mức độ tăng trưởng: {interest_stats['growth_percent']:.2f}%")
        print(f"Giá trị trung bình: {interest_stats['average']:.2f}")
        print(f"Giá trị peak (cao nhất): {interest_stats['peak']}")
        print("\nDữ liệu chi tiết (5 dòng đầu):")
        print(interest_stats['data'].head())
    else:
        print("Không có dữ liệu")

    # ===== RELATED TOPICS =====
    print("\n\n🔗 [RELATED TOPICS - Chủ đề liên quan đang tăng]")
    print("-" * 60)

    rising_topics = process_related_topics(trends_data['related_topics'])

    if rising_topics is not None and not rising_topics.empty:
        print(f"Tổng số chủ đề: {len(rising_topics)}\n")
        print("Top 5 chủ đề đang tăng:")
        print(rising_topics.head(5))
    else:
        print("Không có dữ liệu")

    # ===== RELATED QUERIES =====
    print("\n\n🔤 [RELATED QUERIES - Từ khóa liên quan đang tăng]")
    print("-" * 60)

    rising_queries = process_related_queries(trends_data['related_queries'])

    if rising_queries is not None and not rising_queries.empty:
        print(f"Tổng số từ khóa: {len(rising_queries)}\n")
        print("Top 5 từ khóa đang tăng:")
        print(rising_queries.head(5))
    else:
        print("Không có dữ liệu")

    print("\n" + "="*60)
    print("✅ Hoàn tất!")
    print("="*60 + "\n")


def main():
    """
    Hàm chính - điểm vào của script
    """
    # Lấy arguments
    args = get_arguments()

    # Lấy dữ liệu trending
    trends_data = fetch_trends_data(args.keyword, args.country, args.days)

    if trends_data is None:
        exit(1)

    # In kết quả
    print_results(args.keyword, args.country, trends_data)


if __name__ == "__main__":
    main()
