import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Job Market Analysis with AI Adoption and Automation Risk')
st.write("This app analyzes job data, including AI adoption levels, automation risks, salary trends, and more.")

# Load dataset (update with your actual CSV file)
@st.cache_data 
def load_data():
    data = pd.read_csv('ai_job_market_insights.csv')
    return data

data = load_data()

# Sidebar for filtering options
st.sidebar.title("Filter Options")
industry_filter = st.sidebar.multiselect('Filter by Industry', options=data['Industry'].unique(), default=data['Industry'].unique())
company_size_filter = st.sidebar.multiselect('Filter by Company Size', options=data['Company_Size'].unique(), default=data['Company_Size'].unique())
location_filter = st.sidebar.multiselect('Filter by Location', options=data['Location'].unique(), default=data['Location'].unique())

# Filter data based on sidebar inputs
filtered_data = data[(data['Industry'].isin(industry_filter)) & 
                     (data['Company_Size'].isin(company_size_filter)) &
                     (data['Location'].isin(location_filter))]

# Display filtered data
st.subheader("Filtered Job Data")
st.write(filtered_data)

# 1. AI Adoption Level Distribution (using a Pie Chart with Plotly)
st.subheader("AI Adoption Levels in Jobs")
ai_adoption_count = filtered_data['AI_Adoption_Level'].value_counts().reset_index()
ai_adoption_count.columns = ['AI_Adoption_Level', 'Count']

# Create a pie chart using Plotly
fig_pie = px.pie(ai_adoption_count, 
                 names='AI_Adoption_Level', 
                 values='Count', 
                 title='AI Adoption Levels in Jobs',
                 color_discrete_sequence=px.colors.qualitative.Set3)

st.plotly_chart(fig_pie)

# S=lary Distribution (using Plotly)
st.subheader("Salary Distribution")
fig_salary = px.histogram(filtered_data, x='Salary_USD', nbins=10, 
                          title='Salary Distribution',
                          labels={'Salary_USD': 'Salary (USD)', 'count': 'Frequency'},
                          color_discrete_sequence=['skyblue'])
st.plotly_chart(fig_salary)

# 3. Job Growth Projection by Industry
st.subheader("Job Growth Projection by Industry")
job_growth = filtered_data.groupby(['Industry', 'Job_Growth_Projection']).size().reset_index(name='Count')
fig_growth = px.bar(job_growth, x='Industry', y='Count', color='Job_Growth_Projection',
                    title='Job Growth Projection by Industry',
                    labels={'Industry': 'Industry', 'Count': 'Number of Jobs'},
                    color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig_growth)

# 4. Automation Risk by Job Title (using Plotly)
st.subheader("Automation Risk by Job Title")
automation_risk = filtered_data.groupby(['Job_Title', 'Automation_Risk']).size().reset_index(name='Count')
fig_risk = px.bar(automation_risk, x='Job_Title', y='Count', color='Automation_Risk',
                  title='Automation Risk by Job Title',
                  labels={'Job_Title': 'Job Title', 'Count': 'Number of Jobs'},
                  color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(fig_risk)

# 5. Ranking of AI Adoption Levels by Industry (using Plotly)
st.subheader("AI Adoption Levels by Industry")
ai_adoption_by_industry = filtered_data.groupby(['Industry', 'AI_Adoption_Level']).size().reset_index(name='Count')
fig_adoption_industry = px.bar(ai_adoption_by_industry, x='Industry', y='Count', color='AI_Adoption_Level',
                               title='AI Adoption Levels by Industry',
                               labels={'Industry': 'Industry', 'Count': 'Number of Jobs'},
                               color_discrete_sequence=px.colors.qualitative.Dark2)
st.plotly_chart(fig_adoption_industry)

st.write("This is an analysis of job data with respect to AI adoption, automation risk, and salary distribution. You can adjust the filters on the sidebar to see specific data points.")
