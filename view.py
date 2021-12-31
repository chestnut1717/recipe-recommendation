from os import name
from recipe_recom import *
import show_expiration
import streamlit as st




# streamlit을 이용해 화면을 보여준다.
def show_page():
    # default page setting
    st.set_page_config(page_title="리사야 냉장고를 부탁해", page_icon="🍎", layout="wide")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    # data load
    df = load_data()
    
    # row1.config
    row1_spacer1, row1_2, row1_spacer2 = st.columns(
        (2,3,2)
        )

    # row2.config
    row2_spacer1, row2_1, row2_spacer2, row2_2, row2_spacer3,row2_3 = st.columns(
        (.2, 1.3, .1, 1.3, .1, .2)
        )

    # row3.config
    row3_spacer1, row3_1, row2_spacer2, row3_2, row3_spacer3,row3_3 = st.columns(
        (.2, 1.3, .1, 1.3, .1, .2)
        )
    
    # 상세설정
    with row1_2:
        st.write("""# 👩‍🍳리사야 냉장고를 부탁해""")
        st.write(' ')
        st.write(' ')
        input_ingredient = st.text_input('재료를 입력해 주세요           🦐🥕🌽🧅🦀')
        output_df = get_recommendations(input_ingredient, '메뉴',df)
        output_df = output_df.reset_index()
        output_df = output_df.drop(['index'],axis = 1)
        output_df = output_df[:3]
    ingredients = df['재료'].apply(lambda x : x.split(','))

    # set row2
    with row2_1:
        menu = [menu for menu in output_df['이름']]
        st.header('🧾Recipe')
        for i in range(3):
            for index, j in zip(['요리 이름', '재료', '겹치는 재료'], range(0, 3)):
                if j == 2:
                    j = -2
                if index == '요리 이름':
                    st.write(f'#### {i+1}.  ',output_df.iloc[i,j])
                else:
                    st.write(f"{index}  :  ", output_df.iloc[i, j])
        # st.dataframe(output_df[['이름', '재료','겹치는 재료']])
        
    with row2_2:
        st.header('🗸 Recipe Choice')
        name = st.selectbox('',menu)
        image_url = output_df[output_df['이름'] == name].iloc[0, -4]
        st.image(image_url, width=250,use_column_width = 'auto')
        recipe_url = output_df[output_df['이름'] == name].iloc[0, -3]
        st.write("조리법 주소")
        st.write(recipe_url)
    
    with row3_2:
        ## 웹 페이지에 영수증 등록
        new_exp = show_expiration.upload_credit()
        new_exp

        ## 유통기한 경고 문구 출력
        show_exp = show_expiration.button2()
        show_exp

        ##기본 버튼
        back_button = show_expiration.button3()
        back_button



if __name__ == "__main__":
    show_page()


