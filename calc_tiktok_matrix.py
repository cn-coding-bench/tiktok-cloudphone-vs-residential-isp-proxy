#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TikTok Shop 跨境直播与矩阵养号网络/硬件成本测算脚本
零第三方依赖，对比 DuoPlus 云端真机云手机与指纹浏览器+双ISP代理在不同规模下的真实成本与风控特性。
"""

import argparse
import sys

def format_row(cols, widths, aligns):
    parts = []
    for val, w, align in zip(cols, widths, aligns):
        s = str(val)
        actual_len = sum(2 if ord(c) > 127 else 1 for c in s)
        padding = max(0, w - actual_len)
        if align == '<':
            parts.append(s + ' ' * padding)
        elif align == '>':
            parts.append(' ' * padding + s)
        else:
            left = padding // 2
            right = padding - left
            parts.append(' ' * left + s + ' ' * right)
    return " | ".join(parts)

def run_calc(phones=10, stream=False):
    print("=" * 76)
    print("  TikTok Shop 跨境直播与矩阵养号硬件/网络成本测算 (设备数: {})".format(phones))
    print("=" * 76)

    # 1. DuoPlus 云端真机云手机
    duo_device_monthly = phones * 65.0
    bwh_stream_monthly = 181.2 if stream else 0.0  # 若带直播推流，需配搬瓦工CN2 GIA专线中转
    duo_total_monthly = duo_device_monthly + bwh_stream_monthly
    duo_annual = duo_total_monthly * 12

    # 2. 指纹浏览器 + 静态住宅代理 (PC模拟)
    browser_monthly = 50.0 if phones <= 50 else 100.0
    lisa_vps = 68.0
    proxy_ip = phones * 45.0  # 独享双ISP住宅IP
    browser_total_monthly = browser_monthly + lisa_vps + proxy_ip
    browser_annual = browser_total_monthly * 12

    headers = ["方案配置", "硬件/环境月费", "网络/VPS月费", "稳态月均支出", "风控通过率评估"]
    widths = [26, 16, 16, 16, 20]
    aligns = ['<', '>', '>', '>', '<']

    print(format_row(headers, widths, aligns))
    print("-" * 76)
    print(format_row(["DuoPlus ARM真机云手机", f"¥{duo_device_monthly:.1f}", f"¥{bwh_stream_monthly:.1f}", f"¥{duo_total_monthly:.1f}", "99% (原生芯片与真机传感器)"], widths, aligns))
    print(format_row(["比特浏览器+双ISP静态代理", f"¥{browser_monthly:.1f}", f"¥{lisa_vps+proxy_ip:.1f}", f"¥{browser_total_monthly:.1f}", "85% (适合PC端，移动端易被验)"], widths, aligns))
    print("-" * 76)

    print("\n💡 TikTok 风控防封核心实战认知:")
    print("  • 【0 播放致命原因】: TikTok App 会深度读取设备陀螺仪、电池电量、OpenGL ES 驱动与真实基带信息。普通指纹浏览器在 PC 上模拟移动端极易被判定为模拟器导致 0 播放！")
    print("  • 【真机云手机破局】: DuoPlus 采用底层物理 ARM 架构云手机，运行真实 Android 系统，每台设备拥有独一无二的硬件 IMEI 与传感器特征，从根源规避矩阵连坐。")
    print("  • 【网络底层要求】: 必须搭配原生双 ISP 住宅 IP（如丽萨主机双 ISP）或优质专线（搬瓦工 CN2 GIA），严禁使用机房广播 IP。\n")

    print("🔗 推荐官方合作通道:")
    print("  • DuoPlus 跨境真机云手机: https://cbcost.mybskm.top/go/duoplus")
    print("  • 丽萨主机美区双 ISP 原生住宅 VPS: https://cbcost.mybskm.top/go/lisahost")
    print("  • 搬瓦工 CN2 GIA 高清直播专线: https://cbcost.mybskm.top/go/bwh")
    print("  • 比特浏览器 (PC端环境隔离): https://cbcost.mybskm.top/go/bitbrowser")
    print("  • TikTok 云手机 vs 住宅代理专题页: https://cbcost.mybskm.top/tiktok-cloudphone-vs-fingerprint-isp-proxy.html\n")

def main():
    parser = argparse.ArgumentParser(description="TikTok Shop 跨境直播与矩阵养号硬件与网络成本测算")
    parser.add_argument("--phones", type=int, default=10, help="运营云手机/设备数量 (默认: 10)")
    parser.add_argument("--stream", action="store_true", help="是否包含跨境高清直播推流场景")
    args = parser.parse_args()
    run_calc(args.phones, args.stream)

if __name__ == '__main__':
    main()
