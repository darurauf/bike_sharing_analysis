# Bike Sharing Analysis

Proyek ini menganalisis data penyewaan sepeda (*Bike Sharing Dataset*) untuk menjawab pertanyaan-pertanyaan bisnis terkait pola penyewaan sepeda berdasarkan kondisi cuaca dan waktu.

## **Tujuan Proyek**
1. **Pengaruh Cuaca:** Bagaimana kondisi cuaca seperti *temperature*, *humidity*, dan *wind speed* memengaruhi total jumlah penyewaan sepeda.
2. **Pola Penyewaan:** Bagaimana pola penyewaan sepeda berbeda dalam satu hari, serta perbedaannya antara pengguna biasa (*casual*) dan pengguna terdaftar (*registered*).

## **Tahapan Proyek**
1. **Import Packages/Library:** Menggunakan library Python seperti `pandas`, `numpy`, dan `matplotlib` untuk analisis dan visualisasi data.
2. **Data Wrangling:**
   - **Gathering Data:** Mengumpulkan informasi penting seperti tanggal, kondisi cuaca, dan jumlah penyewaan sepeda.
   - **Assessing Data:** Mengecek data untuk memastikan tidak ada nilai yang hilang atau anomali.
   - **Cleaning Data:** Memperbaiki data jika ditemukan inkonsistensi.
3. **Exploratory Data Analysis (EDA):**
   - Membuat visualisasi untuk menganalisis hubungan antara variabel cuaca dan jumlah penyewaan.
   - Mengidentifikasi pola waktu penyewaan sepeda berdasarkan jam dan kategori pengguna.

## **Insight yang Diperoleh**
- Tidak ada nilai yang hilang dalam dataset.
- Pola penyewaan sepeda menunjukkan perbedaan signifikan antara pengguna biasa dan pengguna terdaftar.
- Cuaca memengaruhi jumlah penyewaan sepeda dengan hubungan yang kuat pada variabel tertentu seperti *temperature*.

## Setup - Terminal
```
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run Analisis_Data_Streamlit.py
```
