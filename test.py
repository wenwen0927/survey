#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import csv
from datetime import datetime


# In[2]:


#pip install streamlit


# In[4]:


import streamlit as st
import csv
from datetime import datetime

st.set_page_config(page_title="你的外在氣場是什麼風格？", layout="centered")

st.title("🎭 你的外在氣場是什麼風格？")
st.write("從穿衣的小細節，看出你的社交能量！快來測測看～")

with st.form("style_quiz"):
    # 原本問題
    q1 = st.radio("Q1：你穿衣服時，會怎麼選擇衣長？", 
                  ["A. 落在骨盆上最順眼", 
                   "B. 喜歡遮屁股一點", 
                   "C. 越長越好", 
                   "D. 沒特別注意"])
  

    q2 = st.radio("Q4：以下哪種描述最符合你的身形？", 
                  ["A. 肩膀窄、骨架小", 
                   "B. 整體比例平均", 
                   "C. 上半身稍寬", 
                   "D. 身高比較高 / 四肢修長"])
    
    q3 = st.radio("Q5：你最常穿的衣服版型是？", 
                  ["A. 合身剪裁", 
                   "B. 微寬鬆", 
                   "C. 完全寬鬆", 
                   "D. 看心情"])

    q4 = st.radio("Q6：你穿 T-shirt 或上衣最在意什麼？", 
                  ["A. 領口不能太高或太低", 
                   "B. 袖長要剛剛好", 
                   "C. 衣長要能遮部位", 
                   "D. 材質舒服就好"])
    q5 = st.radio("Q2：你平常穿衣服的尺寸是？", 
                  ["A. XS / S", 
                   "B. M", 
                   "C. L", 
                   "D. XL / 以上"])
    
    q6 = st.radio("Q3：如果讓你自己量一下肩膀的寬度，你猜大概是？",
                  ["A. 小於 38cm（肩膀比較窄）",
                   "B. 38～39.5cm（中等）",
                   "C. 39.5～41cm（偏寬）",
                   "D. 超過 41cm（寬肩代表）"])
        

    submitted = st.form_submit_button("點這裡看結果")

if submitted:
    # 只看 Q1、Q4～Q6 來推論「風格類型」
    answers_for_result = [q1[0], q4[0], q5[0], q6[0]]
    result_letter = max(set(answers_for_result), key=answers_for_result.count)

    # 儲存完整資料
    with open("responses.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().isoformat(),
            q1[0], q2[0], q3[0], q4[0], q5[0], q6[0],
            result_letter
        ])

    # 顯示風格類型
    if result_letter == "A":
        st.subheader("💎 優雅理性型")
        st.write("你講話有條理，穿衣風格偏清爽、乾淨，是朋友中的「大腦擔當」。")
    elif result_letter == "B":
        st.subheader("🌿 自在親和型")
        st.write("你給人一種自然舒服的感覺，穿衣風格簡單實穿，讓人想親近你。")
    elif result_letter == "C":
        st.subheader("🔥 個性強烈型")
        st.write("你擁有鮮明的存在感，衣著風格大膽有型，是朋友圈中的靈魂人物。")
    elif result_letter == "D":
        st.subheader("🌈 變化萬千型")
        st.write("你不喜歡被定義，是天生的風格創造者，風格天天變！")

    st.markdown("---")
    st.caption("🔐 測驗結果僅供參考，資料不會公開喔 😉")


# In[ ]:




