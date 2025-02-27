import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def run_simulation(n_sims, probabilities):
    fruits = ['apple', 'banana', 'orange', 'grape', 'mango']
    results = np.random.choice(fruits, size=n_sims, p=probabilities)
    return results

def main():
    st.title('🎲 Fruit Monte Carlo Simulator')
    
    # Sidebar controls
    st.sidebar.header('Simulation Parameters')
    n_sims = st.sidebar.slider('Number of simulations', 100, 10000, 1000)
    
    # Probability inputs
    st.sidebar.subheader('Fruit Probabilities')
    apple_prob = st.sidebar.slider('Apple probability', 0.0, 1.0, 0.3)
    banana_prob = st.sidebar.slider('Banana probability', 0.0, 1.0, 0.25)
    orange_prob = st.sidebar.slider('Orange probability', 0.0, 1.0, 0.2)
    grape_prob = st.sidebar.slider('Grape probability', 0.0, 1.0, 0.15)
    mango_prob = st.sidebar.slider('Mango probability', 0.0, 1.0, 0.1)
    
    probabilities = [apple_prob, banana_prob, orange_prob, grape_prob, mango_prob]
    
    # Normalize probabilities
    prob_sum = sum(probabilities)
    probabilities = [p/prob_sum for p in probabilities]
    
    if st.button('Run Simulation'):
        results = run_simulation(n_sims, probabilities)
        df_results = pd.DataFrame(results, columns=['fruit'])
        
        # Display results
        st.subheader('Simulation Results')
        frequencies = df_results['fruit'].value_counts()
        relative_frequencies = df_results['fruit'].value_counts(normalize=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("Actual frequencies:")
            st.write(frequencies)
        
        with col2:
            st.write("Relative frequencies:")
            st.write(relative_frequencies)
        
        # Plot
        fig, ax = plt.subplots()
        ax.bar(frequencies.index, frequencies.values)
        ax.set_title('Monte Carlo Simulation Results')
        ax.set_xlabel('Fruit')
        ax.set_ylabel('Frequency')
        st.pyplot(fig)

if __name__ == '__main__':
    main() 