import streamlit as st

def main():
    # 1. 設定網頁標題
    st.title('BMI 健康計算機')
    st.markdown("請輸入您的身高與體重，我們將為您計算 BMI 指數。")

    # 使用分隔線讓版面更清楚
    st.divider()

    # 2. 輸入介面：使用 columns 讓身高體重並排顯示，比較美觀
    col1, col2 = st.columns(2)

    with col1:
        # 設定 min_value 防止輸入負數
        height = st.number_input('身高 (cm)', min_value=1.0, value=170.0, step=1.0)
    
    with col2:
        weight = st.number_input('體重 (kg)', min_value=1.0, value=65.0, step=0.1)

    # 3. 按鈕與邏輯
    if st.button('開始計算'):
        # 防呆機制：確保身高不為 0
        if height > 0:
            # 單位換算：公分 -> 公尺
            height_m = height / 100
            
            # 計算 BMI
            bmi = weight / (height_m ** 2)
            
            # 顯示 BMI 數值 (保留一位小數)
            st.markdown(f"### 您的 BMI 指數為：**{bmi:.1f}**")

            # 4. 判斷邏輯與 5. 加分題 (顏色顯示)
            # 判斷標準參考：
            # 過輕：BMI < 18.5
            # 正常：18.5 <= BMI < 24
            # 肥胖 (含過重)：BMI >= 24
            
            if 18.5 <= bmi < 24:
                result_text = "正常"
                # 顯示綠色文字
                st.markdown(f"### 判定結果：:green[{result_text}]")
                st.success("恭喜！您的體重在正常範圍內，請繼續保持。")
            
            else:
                if bmi < 18.5:
                    result_text = "過輕"
                else:
                    result_text = "肥胖" # 廣義包含過重
                
                # 顯示紅色文字
                st.markdown(f"### 判定結果：:red[{result_text}]")
                st.error("注意！您的體重不在理想範圍，建議調整飲食或運動。")
        else:
            st.warning("身高數值必須大於 0")

if __name__ == '__main__':
    main()