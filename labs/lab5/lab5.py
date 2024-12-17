import streamlit as st


class Povtory(str):
    def povtory_sliv(self, s):
        
        words = s.lower().split()
        symv3 = []
        
        
        for i in words:
            if len(i) > 3:
                symv3.append(i) 
        
        
        for word in symv3:
            if symv3.count(word) > 1:
                return True
        return False
       


    def palindrome(self):
        ryadok = self.replace(" ", "").lower()
        return ryadok == ryadok[::-1]


def lab5():

    s = st.text_input("Введіть рядок: ")

    s = Povtory(s)

    povtory = s.povtory_sliv(s)
    palindrome = s.palindrome()

    if not s:
        st.warning("Будь ласка, введіть текст")
    else:
        if povtory:
            st.success("Повтори > 3 символів знайдені")  
        else: 
            st.error("Повторів > 3 символів немає")
        if palindrome:
            st.success("Паліндром знайдено")
        else:
            st.error("Паліндром не знайдено")