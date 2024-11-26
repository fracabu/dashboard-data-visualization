import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Page config
st.set_page_config(page_title="Medical Dashboard", layout="wide")

# CSS with dark/light mode
st.markdown("""
<style>
/* Theme Variables */
:root[data-theme="light"] {
    --bg-primary: #f9fbfd;
    --bg-secondary: #ffffff;
    --text-primary: #1b2a4e;
    --text-secondary: #6e84a3;
    --accent: #2c7be5;
    --border: #e9ecef;
    --shadow: rgba(0, 0, 0, 0.1);
}

:root[data-theme="dark"] {
    --bg-primary: #0f172a;
    --bg-secondary: #1e293b;
    --text-primary: #f8fafc;
    --text-secondary: #94a3b8;
    --accent: #38bdf8;
    --border: #334155;
    --shadow: rgba(0, 0, 0, 0.3);
}

/* Base Styles */
body {
    background: var(--bg-primary);
    color: var(--text-primary);
    transition: all 0.3s ease;
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
}

/* Header */
.header-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 2rem;
    background: var(--bg-secondary);
    box-shadow: 0 2px 8px var(--shadow);
    margin-bottom: 2rem;
}

.logo {
    width: 40px;
    height: 40px;
    margin-right: 1rem;
}

/* Theme Toggle */
.theme-switch {
    position: relative;
    width: 60px;
    height: 30px;
}

.theme-switch input {
    opacity: 0;
    width: 0;
    height: 0;
}

.switch-label {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: var(--text-secondary);
    border-radius: 15px;
    transition: 0.4s;
}

.switch-label:before {
    content: "🌙";
    position: absolute;
    height: 24px;
    width: 24px;
    left: 4px;
    bottom: 3px;
    background: var(--bg-secondary);
    border-radius: 50%;
    transition: 0.4s;
    text-align: center;
    line-height: 24px;
}

input:checked + .switch-label {
    background: var(--accent);
}

input:checked + .switch-label:before {
    transform: translateX(28px);
    content: "☀️";
}

/* Sidebar */
.css-1d391kg {
    background: var(--bg-secondary);
}

/* Content */
.stApp {
    background: var(--bg-primary);
}

.css-18e3th9 {
    color: var(--accent);
    font-size: 2.4rem;
    font-weight: 800;
    text-align: center;
    margin: 2rem 0;
}

.stDataFrame {
    background: var(--bg-secondary) !important;
}

/* File uploader */
.stFileUploader {
    border: 2px dashed var(--accent) !important;
    background: rgba(44, 123, 229, 0.05) !important;
    border-radius: 12px;
    padding: 1.5rem;
}

/* Metrics */
.css-1wivf9j {
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1rem;
}

[data-testid="stMetricValue"] {
    color: var(--accent);
}
</style>

""", unsafe_allow_html=True)



# Sidebar Toggle for Theme
theme = st.sidebar.radio("Select Theme:", ["Light", "Dark"])

# Apply CSS based on the selected theme
if theme == "Light":
    st.markdown(
        """
        <style>
        :root {
            --bg-primary: #f9fbfd;
            --bg-secondary: #ffffff;
            --text-primary: #1b2a4e;
            --text-secondary: #6e84a3;
            --accent: #2c7be5;
        }
        body {
            background-color: var(--bg-primary);
            color: var(--text-primary);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
        :root {
            --bg-primary: #0f172a;
            --bg-secondary: #1e293b;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --accent: #38bdf8;
        }
        body {
            background-color: var(--bg-primary);
            color: var(--text-primary);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# Main content
st.title("Medical Data Visualization Dashboard")

# Tabs
tab1, tab2 = st.tabs(["📊 Visualization", "⚙️ Settings"])

with tab1:
    uploaded_file = st.file_uploader("Upload the CSV file with medical data", type=["csv"])

    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        
        # Sidebar filters
        st.sidebar.header("Filters")
        
        # Create filters
        filters = {}
        for column in data.columns:
            if data[column].dtype == 'object':
                unique_values = data[column].unique()
                filters[column] = st.sidebar.multiselect(
                    f'Select {column}',
                    options=unique_values,
                    default=unique_values
                )
            elif data[column].dtype in ['int64', 'float64']:
                min_val = float(data[column].min())
                max_val = float(data[column].max())
                filters[column] = st.sidebar.slider(
                    f'Range of {column}',
                    min_val, max_val,
                    (min_val, max_val)
                )

        # Apply filters
        filtered_data = data.copy()
        for column, filter_value in filters.items():
            if data[column].dtype == 'object':
                if filter_value:
                    filtered_data = filtered_data[filtered_data[column].isin(filter_value)]
            else:
                filtered_data = filtered_data[
                    (filtered_data[column] >= filter_value[0]) & 
                    (filtered_data[column] <= filter_value[1])
                ]

        # Display metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Records", len(filtered_data))
        with col2:
            if 'Age' in filtered_data.columns:
                st.metric("Average Age", f"{filtered_data['Age'].mean():.1f}")
        with col3:
            if 'Diagnosis' in filtered_data.columns:
                st.metric("Unique Diagnoses", filtered_data['Diagnosis'].nunique())
        with col4:
            if 'Gender' in filtered_data.columns:
                most_common_gender = filtered_data['Gender'].mode()[0]
                st.metric("Most Common Gender", most_common_gender)

        # Charts
        chart_col1, chart_col2 = st.columns(2)
        
        with chart_col1:
            if 'Age' in filtered_data.columns:
                st.subheader("Age Distribution")
                fig = px.histogram(filtered_data, x='Age', nbins=20,
                                 title="Age Distribution",
                                 color_discrete_sequence=['#38bdf8'])
                st.plotly_chart(fig, use_container_width=True)

        with chart_col2:
            if 'Gender' in filtered_data.columns and 'Diagnosis' in filtered_data.columns:
                st.subheader("Diagnosis by Gender")
                fig = px.bar(filtered_data.groupby(['Gender', 'Diagnosis']).size().reset_index(name='Count'),
                           x='Diagnosis', y='Count', color='Gender',
                           title="Diagnosis by Gender",
                           color_discrete_sequence=['#38bdf8', '#0ea5e9'])
                st.plotly_chart(fig, use_container_width=True)

        st.subheader("Additional Charts")

        # Scatter Plot
        if 'Age' in filtered_data.columns and any(filtered_data.dtypes == 'float64') or any(filtered_data.dtypes == 'int64'):
            numerical_columns = filtered_data.select_dtypes(include=['float64', 'int64']).columns
            if len(numerical_columns) > 1:
                scatter_col = st.selectbox("Select a numerical column for scatter plot", options=numerical_columns)
                st.subheader(f"Scatter Plot: Age vs {scatter_col}")
                scatter_fig = px.scatter(filtered_data, x='Age', y=scatter_col, color='Gender',
                                         title=f"Scatter Plot: Age vs {scatter_col}",
                                         color_discrete_sequence=px.colors.qualitative.Vivid)
                st.plotly_chart(scatter_fig, use_container_width=True)

        # Pie Chart
        if 'Diagnosis' in filtered_data.columns:
            st.subheader("Diagnosis Distribution")
            pie_fig = px.pie(filtered_data, names='Diagnosis', title="Diagnosis Distribution",
                             color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(pie_fig, use_container_width=True)

        # Data preview with pagination
        st.subheader("Data Preview")
        page_size = 10
        page_number = st.number_input('Page', min_value=1, 
                                    max_value=(len(filtered_data) // page_size) + 1, 
                                    value=1)
        start_idx = (page_number - 1) * page_size
        end_idx = start_idx + page_size
        st.dataframe(filtered_data.iloc[start_idx:end_idx])

        # Download button
        st.download_button(
            label="Download filtered data (CSV)",
            data=filtered_data.to_csv(index=False).encode("utf-8"),
            file_name="filtered_data.csv",
            mime="text/csv"
        )

with tab2:
    st.subheader("Dashboard Settings")
    
    # Chart settings
    st.write("Chart Settings")
    chart_theme = st.selectbox("Chart Theme", 
                             ["plotly", "plotly_white", "plotly_dark"])
    show_grid = st.checkbox("Show Grid", value=True)
    
    # Export settings
    st.write("Export Settings")
    export_format = st.radio("Export Format", 
                           ["CSV", "Excel", "JSON"])
    include_metadata = st.checkbox("Include Metadata", value=False)

    # Save settings button
    if st.button("Save Settings"):
        st.success("Settings saved successfully!")