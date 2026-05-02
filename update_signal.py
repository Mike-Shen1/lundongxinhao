

从 日期时间 导入 日期时间

# 读取数据
df = pd.read_csv('data.csv', encoding='utf-8-sig')
最新行 = df.iloc[1]

# 策略参数
['市盈率百分位']
市盈率低 = 30
市盈率_高 = 70

# 风控1：财报季休眠
is_quarterly_month = latest_row['is_quarterly_month']

如果是季度月:
    should_rebalance = False
    reason = "财报季休眠（1/4/7/10月不调仓）"
    权重 = 无
否则:
    # 计算仓位
    如果 每股收益百分位 < PE_LOW:
        权重 = {"515300"0.60"518880"0.40}
    elif pe_percentile > PE_HIGH:
        权重 = {"511010": 0.50, "511880": 0.50}
    否则:
        权重 = {"515300": 0.35, "511010": 0.20, "518880": 0.35, "511880": 0.10}
    
    # 风控2：仅月度首个交易日调仓
    should_rebalance = latest_row['is_first_trading_day']
    reason = "正常交易日" if should_rebalance else "非月度首个交易日"

# 组装结果
结果 = {
    "日期"['日期']
    "更新时间"：当前（）。格式化日期时间（'Y-m-d H:M:S'），
    "市盈率百分位": 四舍五入(市盈率百分位, 2),
    "应该重新平衡": should_rebalance
    "信号原因": 原因,
    "目标权重": 权重,
    "etf_prices": {
        "515300": 浮点数(最新行['515300_收盘价']),
"511010": 浮点数(最新行['511010_收盘价']),
"518880": 浮点数(最新行['518880_收盘价']),
        "511880": 浮点数(最新行['511880_收盘价'])
    }
    "免责声明" "本策略仅为量化模型输出，不构成投资建议，投资有风险，入市需谨慎"
}

# 保存信号文件
打开('signal.json', 'w', 编码='utf-8') 作为 f:
    json.dump(result, f, ensure_ascii=False, indent=2)

("信号生成成功！")
打印(json.dumps(结果, 确保_ascii=False, 缩进=2))
