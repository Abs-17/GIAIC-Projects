# Imports
import streamlit as st
import pandas as pd
import xlsxwriter
import os
from io import BytesIO
from fpdf import FPDF
import matplotlib.pyplot as plt

# Set up our App
st.set_page_config(page_title="💿 Data Sweeper", layout="wide")
st.title("💿 Data Sweeper")
st.write("Transform your file between CSV and Excel formats with built-in data cleaning and visualization!")

uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue

        # Display file info
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.getbuffer().nbytes / 1024:.2f} KB")

        # Show first 5 rows
        st.write("### Preview of Data")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader("🧹 Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("✅ Duplicates Removed!")

            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("✅ Missing values filled!")

        # Choose specific columns
        st.subheader("📌 Select Columns to Keep")
        columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]

        # Data Visualization
        st.subheader("📊 Data Visualization")
        selected_viz_cols = st.multiselect(f"Select numeric columns for {file.name} visualization", 
                                           df.select_dtypes(include=['number']).columns)

        if selected_viz_cols:
            st.bar_chart(df[selected_viz_cols])

        # File Conversion
        st.subheader("🔄 File Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            file_name = file.name.replace(file_ext, f".{conversion_type.lower()}")

            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                    df.to_excel(writer, index=False, sheet_name="Sheet1")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)

            # Download button
            st.download_button(
                label=f"⬇ Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

        # Generate PDF Report
        st.subheader("📄 Generate Analysis Report")
        if st.button(f"Generate PDF Report for {file.name}"):
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Arial", style='B', size=16)
            pdf.cell(200, 10, "Data Analysis Report", ln=True, align='C')
            pdf.ln(10)
            pdf.set_font("Arial", size=12)

            # Basic Data Summary
            pdf.cell(200, 10, f"File Name: {file.name}", ln=True)
            pdf.cell(200, 10, f"Rows: {df.shape[0]}, Columns: {df.shape[1]}", ln=True)
            pdf.ln(5)

            # Missing Values
            missing_values = df.isnull().sum()
            missing_data = missing_values[missing_values > 0]
            if not missing_data.empty:
                pdf.cell(200, 10, "Missing Values:", ln=True)
                for col, val in missing_data.items():
                    pdf.cell(200, 10, f"{col}: {val} missing values", ln=True)
                pdf.ln(5)

            # Descriptive Statistics
            pdf.cell(200, 10, "Descriptive Statistics:", ln=True)
            for col in df.select_dtypes(include=['number']).columns:
                pdf.cell(200, 10, f"{col} - Mean: {df[col].mean():.2f}, Min: {df[col].min()}, Max: {df[col].max()}", ln=True)
            pdf.ln(5)

            # Generate and Save a Chart
            if selected_viz_cols:
                plt.figure(figsize=(6, 4))
                df[selected_viz_cols].mean().plot(kind='bar')
                plt.title("Average Values of Selected Columns")
                plt.xlabel("Columns")
                plt.ylabel("Mean Value")
                chart_path = "chart.png"
                plt.savefig(chart_path)
                pdf.image(chart_path, x=10, w=180)

            # Save PDF
            pdf_output = BytesIO()
            pdf_bytes = pdf.output(dest='S').encode('latin1')  # Get PDF as bytes
            pdf_output.write(pdf_bytes)
            pdf_output.seek(0)


            # Download PDF Button
            st.download_button(
                label=f"⬇ Download Report for {file.name}",
                data=pdf_output,
                file_name=f"{file.name.replace(file_ext, '_report.pdf')}",
                mime="application/pdf"
            )

st.success("🎉 All files processed successfully!")
