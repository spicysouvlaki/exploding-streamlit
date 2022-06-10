
import streamlit as st

st.code("""
def genprimes(limit): 
    # just generate some heavy load function
    D = {}            
    q = 2

    while q <= limit:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def non_cache_wrap(limit):
    return sum(list(genprimes(limit)))
import random

non_cache_wrap(random.randint(100000, 1000000))

# select the spend sub type
sel1 = st.selectbox('Selection 1 - Change this to make sure you see the break', ['A', 'B'])

st.markdown('---')
_ = st.multiselect('Selection 2 - quickly select stuff in here', list('ABCDEFGHIJKLMNOPRST12342567i7oABCDEFGHIJKLMNOPRST12342567i7o') * 3)
    """)

def genprimes(limit): 
    # just generate some heavy load function
    D = {}            
    q = 2

    while q <= limit:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def non_cache_wrap(limit):
    return sum(list(genprimes(limit)))
import random

non_cache_wrap(random.randint(100000, 1000000))

# select the spend sub type
sel1 = st.selectbox('Selection 1 - Change this to make sure you see the break', ['A', 'B'])

st.markdown('---')
_ = st.multiselect('Selection 2 - quickly select stuff in here', list('ABCDEFGHIJKLMNOPRST12342567i7oABCDEFGHIJKLMNOPRST12342567i7o') * 3)
