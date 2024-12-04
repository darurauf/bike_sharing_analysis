import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
st.title("Proyek Analisis Data")
st.subheader("Bike Sharing Dataset")
data = pd.read_csv("C:/Users/Dar/Downloads/hour.csv")
st.write(data)
st.markdown(
    """
    Dari data tersebut, bisa didapatkan 2 pertanyaan bisnis :
    1. Bagaimana kondisi cuaca seperti *temperature*, *humidity*, dan *wind speed* dapat mempengaruhi total jumlah dari rental sepeda?
    2. Bagaimana pola penyewaan sepeda pada waktu-waktu yang berbeda dalam satu hari serta perbedaannya antara pengguna biasa dan pengguna terdaftar?
    """
)
st.subheader("Data Visualization")
st.markdown(
    """
    Setelah melakukan Data Cleaning dan EDA, kita dapat visualisasikan data yang berhubungan dengan pertanyaan bisnis sebelumnya.
    """
)

# Visualisasi data
col1, col2= st.columns([1, 1])
with col1:
    weather_features = ['temp', 'atemp', 'hum', 'windspeed', 'cnt']
    corr_matrix = data[weather_features].corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Matrix: Kondisi Cuaca dengan Jumlah Rental')
    st.pyplot(plt)

with col2:
    hourly_data = data.groupby('hr')[['casual', 'registered', 'cnt']].mean().reset_index()

    # Persiapkan data untuk line chart
    chart_data = hourly_data[['hr', 'casual', 'registered']].set_index('hr')

    # Tampilkan line chart menggunakan Streamlit
    st.line_chart(chart_data)

# Conclusion
st.subheader("Conclusion")
st.markdown(
    """
    Dari hasil kedua data visualisasi sebelumnya dapat dipahami bahwa:
    
    **Conclusion pertanyaan 1**
    
    Suhu memainkan peran penting dalam mempengaruhi penyewaan sepeda, suhu yang lebih tinggi umumnya menyebabkan lebih banyak penyewaan sedangkan kelembaban dan kecepatan angin memiliki efek yang kecil atau dapat diabaikan pada total penyewaan.
    
    **Conclusion pertanyaan 2**:
    
    Pengguna casual lebih suka menyewa sepeda pada jam-jam senggang, terutama pada siang hari. Pengguna registered menunjukkan pola komuter, menyewa sepeda di pagi dan sore hari.
    """
)