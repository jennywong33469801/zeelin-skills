# -*- coding: utf-8 -*-
"""
日期工具模块 - VOL编号推算
用法:
  python date_utils.py vol 2026-04-21
  python date_utils.py today
  python date_utils.py check_vol 111
"""

import sys
import argparse
from datetime import datetime, timedelta

# ─── 配置区（按项目修改）───────────────────────
START_DATE = "2024-03-10"  # VOL.1 发行日期
# ─────────────────────────────────────────────

WEEKDAY_CN = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]


def date_to_vol(date_str: str, fmt: str = "%Y-%m-%d") -> int:
    """根据日期推算VOL编号"""
    dt = datetime.strptime(date_str, fmt)
    start = datetime.strptime(START_DATE, "%Y-%m-%d")
    return (dt - start).days + 1


def vol_to_date(vol: int) -> str:
    """根据VOL编号推算日期"""
    start = datetime.strptime(START_DATE, "%Y-%m-%d")
    return (start + timedelta(days=vol - 1)).strftime("%Y-%m-%d")


def get_weekday_cn(date_str: str, fmt: str = "%Y-%m-%d") -> str:
    """返回中文星期"""
    dt = datetime.strptime(date_str, fmt)
    return WEEKDAY_CN[dt.weekday()]


def get_today_vol() -> int:
    """返回今天对应的VOL编号"""
    return date_to_vol(datetime.now().strftime("%Y-%m-%d"))


def format_daily_header(date_str: str, vol: int = None) -> str:
    """格式化日报头部信息"""
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    formatted = dt.strftime("%Y年%m月%d日")
    weekday = WEEKDAY_CN[dt.weekday()]
    mmdd = dt.strftime("%m%d")
    if vol is None:
        vol = date_to_vol(date_str)
    return {
        "date_full": formatted,
        "weekday": weekday,
        "mmdd": mmdd,
        "vol": vol,
        "vol_label": f"VOL.{vol}",
        "date_label": f"{formatted} · {weekday}",
        "footer_label": f"AI日报 VOL.{vol} · {dt.strftime('%Y.%m.%d')}"
    }


def validate_vol_date(vol: int, expected_date: str = None) -> dict:
    """验证VOL编号与日期是否匹配"""
    calc_date = vol_to_date(vol)
    if expected_date:
        match = calc_date == expected_date
        return {"vol": vol, "calc_date": calc_date, "expected": expected_date, "match": match}
    return {"vol": vol, "calc_date": calc_date}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VOL编号推算工具")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("today", help="输出今天对应的VOL编号")
    sub.add_parser("weekday", help="输出今天的中文星期")
    sub.add_parser("info", help="输出今天日报完整头部信息")

    sub.add_parser("vol", help="根据日期查VOL").add_argument("date", help="日期 2026-04-21")
    sub.add_parser("date", help="根据VOL查日期").add_argument("vol", type=int)
    sub.add_parser("check_vol", help="验证VOL编号").add_argument("vol", type=int)

    args = parser.parse_args()

    if args.cmd == "today":
        vol = get_today_vol()
        today = datetime.now().strftime("%Y-%m-%d")
        print(f"{today} → VOL.{vol}")

    elif args.cmd == "weekday":
        print(get_weekday_cn(datetime.now().strftime("%Y-%m-%d")))

    elif args.cmd == "info":
        today = datetime.now().strftime("%Y-%m-%d")
        info = format_daily_header(today)
        print(f"VOL.{info['vol']} | {info['date_full']} · {info['weekday']}")
        print(f"MMDD: {info['mmdd']}")

    elif args.cmd == "vol":
        v = date_to_vol(args.date)
        print(f"{args.date} → VOL.{v}")

    elif args.cmd == "date":
        d = vol_to_date(args.vol)
        w = get_weekday_cn(d)
        print(f"VOL.{args.vol} → {d} ({w})")

    elif args.cmd == "check_vol":
        r = validate_vol_date(args.vol)
        print(f"VOL.{r['vol']} = {r['calc_date']}")

    else:
        parser.print_help()
