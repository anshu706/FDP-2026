# Streamlit app: CSV Sales Dashboard with Interactive Filters
# Run with: streamlit run app.py

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CSV Sales Dashboard", layout="wide")

st.title("📊 Sales Dashboard")
st.write("Upload a CSV file (e.g., sales data) and explore interactive charts with filters.")

# Sidebar
st.sidebar.header("Controls")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])


@st.cache_data
def load_data(file):
    return pd.read_csv(file)


if uploaded_file is None:
    st.info("Please upload a CSV file to begin.")
    st.stop()

# Load data
df = load_data(uploaded_file)

st.subheader("Preview")
st.dataframe(df.head())

# Basic assumptions / validation
if df.shape[1] < 2:
    st.error("CSV needs at least two columns.")
    st.stop()

# Column selectors
numeric_cols = df.select_dtypes(include="number").columns.tolist()
categorical_cols = df.select_dtypes(exclude="number").columns.tolist()

if not numeric_cols:
    st.error("No numeric columns found for charting.")
    st.stop()

x_col = st.sidebar.selectbox(
    "X-axis (category/date)", categorical_cols or df.columns.tolist())
y_col = st.sidebar.selectbox("Y-axis (numeric)", numeric_cols)

chart_type = st.sidebar.radio("Chart Type", ["Bar", "Line", "Scatter"])

# Filters
st.sidebar.subheader("Filters")
filtered_df = df.copy()

for col in categorical_cols:
    values = df[col].dropna().unique().tolist()
    if len(values) <= 50:
        selected = st.sidebar.multiselect(
            f"Filter {col}", values, default=values)
        filtered_df = filtered_df[filtered_df[col].isin(selected)]

for col in numeric_cols:
    col_data = df[col].dropna()
    if len(col_data) > 0:
        min_val, max_val = float(col_data.min()), float(col_data.max())
        if min_val != max_val:
            selected_range = st.sidebar.slider(
                f"Filter {col}", min_val, max_val, (min_val, max_val)
            )
            filtered_df = filtered_df[
                (filtered_df[col] >= selected_range[0]) & (
                    filtered_df[col] <= selected_range[1])
            ]

st.subheader("Filtered Data")
st.write(f"Rows: {len(filtered_df)}")
st.dataframe(filtered_df)

# Chart rendering
st.subheader("Visualization")

if len(filtered_df) == 0:
    st.warning(
        "No data to display after applying filters. Please adjust your filter settings.")
else:
    if chart_type == "Bar":
        fig = px.bar(filtered_df, x=x_col, y=y_col)
    elif chart_type == "Line":
        fig = px.line(filtered_df, x=x_col, y=y_col)
    else:
        fig = px.scatter(filtered_df, x=x_col, y=y_col)

    st.plotly_chart(fig, use_container_width=True)

st.caption("Built with Streamlit, Pandas, and Plotly")
