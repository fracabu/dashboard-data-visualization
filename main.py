import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import io
import requests

# Page config
st.set_page_config(page_title="Complete Dashboard Premium", layout="wide")

# Sidebar Theme Toggle
theme = st.sidebar.radio("Select Theme:", ["Light", "Dark"])

# Theme CSS
if theme == "Light":
    st.markdown("""
    <style>
    :root {
        --bg-primary: #f9fbfd;
        --bg-secondary: #ffffff;
        --text-primary: #1b2a4e;
        --text-secondary: #6e84a3;
        --accent: #2c7be5;
    }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    :root {
        --bg-primary: #0f172a;
        --bg-secondary: #1e293b;
        --text-primary: #f8fafc;
        --text-secondary: #94a3b8;
        --accent: #38bdf8;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("Complete Dashboard Premium Features")

# Caching data for performance
@st.cache_data
def load_csv(file):
    try:
        data = pd.read_csv(file)
        # Pulizia dati
        if "Unnamed: 0" in data.columns:
            data.drop(columns=["Unnamed: 0"], inplace=True)
        # Splitta "BloodPressure" in "Systolic" e "Diastolic"
        if "BloodPressure" in data.columns:
            bp_split = data["BloodPressure"].str.split("/", expand=True)
            data["Systolic"] = pd.to_numeric(bp_split[0], errors="coerce")
            data["Diastolic"] = pd.to_numeric(bp_split[1], errors="coerce")
        # Conversione delle date
        if "VisitDate" in data.columns:
            data["VisitDate"] = pd.to_datetime(data["VisitDate"], errors="coerce")
        return data
    except Exception as e:
        st.error(f"Error reading CSV file: {e}")
        return None

@st.cache_data
def filter_data(data, filters):
    filtered_data = data.copy()
    for column, filter_value in filters.items():
        if data[column].dtype == 'object':
            if filter_value:
                filtered_data = filtered_data[filtered_data[column].isin(filter_value)]
        else:
            filtered_data = filtered_data[(filtered_data[column] >= filter_value[0]) & (filtered_data[column] <= filter_value[1])]
    return filtered_data

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Visualization", "⚙️ Settings", "🌐 API Data"])

# Tab 1: Visualization
with tab1:
    uploaded_file = st.file_uploader("Upload the CSV file with data", type=["csv"])

    if uploaded_file:
        data = load_csv(uploaded_file)
        
        if data is not None:
            # File preview
            st.write("File loaded successfully! Here's a preview:")
            st.dataframe(data.head())

            # Filters
            st.sidebar.header("Filters")
            filters = {}
            columns_to_filter = ["Age", "Gender", "Diagnosis", "Systolic", "Diastolic", "GlucoseCategory"]

            for column in columns_to_filter:
                if column in data.columns:
                    if data[column].dtype == 'object':
                        unique_values = data[column].unique()
                        filters[column] = st.sidebar.multiselect(f'Select {column}', options=unique_values, default=unique_values)
                    elif data[column].dtype in ['int64', 'float64']:
                        min_val, max_val = data[column].min(), data[column].max()
                        filters[column] = st.sidebar.slider(f'Range of {column}', min_val, max_val, (min_val, max_val))

            filtered_data = filter_data(data, filters)

            # Metrics
            st.header("Key Metrics")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Records", len(filtered_data))
            if 'Age' in filtered_data.columns:
                col2.metric("Average Age", f"{filtered_data['Age'].mean():.1f}")
            if 'Diagnosis' in filtered_data.columns:
                col3.metric("Unique Diagnoses", filtered_data['Diagnosis'].nunique())
            if 'Gender' in filtered_data.columns:
                col4.metric("Most Common Gender", filtered_data['Gender'].mode()[0])

            # Charts
            st.subheader("Visualization Charts")
            with st.expander("Age Distribution", expanded=True):
                if 'Age' in filtered_data.columns:
                    fig = px.histogram(filtered_data, x='Age', nbins=20, title="Age Distribution", color_discrete_sequence=['#38bdf8'])
                    st.plotly_chart(fig, use_container_width=True)

            with st.expander("Diagnosis by Gender", expanded=False):
                if 'Gender' in filtered_data.columns and 'Diagnosis' in filtered_data.columns:
                    fig = px.bar(filtered_data.groupby(['Gender', 'Diagnosis']).size().reset_index(name='Count'),
                                 x='Diagnosis', y='Count', color='Gender', title="Diagnosis by Gender",
                                 color_discrete_sequence=['#38bdf8', '#0ea5e9'])
                    st.plotly_chart(fig, use_container_width=True)

            with st.expander("Heatmap of Correlations", expanded=False):
                numerical_data = filtered_data.select_dtypes(include=['float64', 'int64']).fillna(0)
                if not numerical_data.empty:
                    correlation = numerical_data.corr()
                    fig, ax = plt.subplots(figsize=(10, 6))
                    sns.heatmap(correlation, annot=True, cmap="coolwarm", ax=ax)
                    st.pyplot(fig)
                else:
                    st.warning("No numerical columns available for correlation.")

            # Scatter Plot
            with st.expander("Scatter Plot (Optional)", expanded=False):
                if 'Age' in filtered_data.columns:
                    numerical_columns = filtered_data.select_dtypes(include=['float64', 'int64']).columns
                    if len(numerical_columns) > 1:
                        scatter_col = st.selectbox("Select a numerical column for scatter plot", options=numerical_columns)
                        st.subheader(f"Scatter Plot: Age vs {scatter_col}")
                        scatter_fig = px.scatter(filtered_data, x='Age', y=scatter_col, color='Gender',
                                                 title=f"Scatter Plot: Age vs {scatter_col}",
                                                 color_discrete_sequence=px.colors.qualitative.Vivid)
                        st.plotly_chart(scatter_fig, use_container_width=True)

            # Data Preview
            st.subheader("Data Preview")
            st.dataframe(filtered_data)

            # Export Options
            st.subheader("Export Options")
            st.download_button(
                "Download Filtered Data (CSV)",
                filtered_data.to_csv(index=False).encode("utf-8"),
                "filtered_data.csv",
                "text/csv"
            )

            excel_buffer = io.BytesIO()
            with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
                filtered_data.to_excel(writer, index=False, sheet_name='Sheet1')
            st.download_button(
                label="Download Filtered Data (Excel)",
                data=excel_buffer.getvalue(),
                file_name="filtered_data.xlsx",
                mime="application/vnd.ms-excel"
            )

# Tab 2: Settings
with tab2:
    st.subheader("Dashboard Settings")
    chart_theme = st.selectbox("Chart Theme", ["plotly", "plotly_white", "plotly_dark"])
    export_format = st.radio("Export Format", ["CSV", "Excel", "JSON"])

    if st.button("Save Settings"):
        st.success("Settings saved successfully!")

# Tab 3: API Data
with tab3:
    st.subheader("API Data Integration")
    api_url = st.text_input("Enter API URL", "http://127.0.0.1:5000/medical-data")
    if st.button("Fetch Data"):
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                api_data = pd.DataFrame(response.json())
                st.write("API Data:")
                st.dataframe(api_data)
            else:
                st.error(f"API Error: {response.status_code}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
