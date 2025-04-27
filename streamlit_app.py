# -----------------------------------
# Program: AP Performance Task
# Version 1.0
# Development Date(s): 2/21/25
# -----------------------------------


import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px


# define data
df = pd.read_csv("College Majors & Incomes.csv")
ranks = df["Rank"].tolist()
majors = df["Major"].tolist()
medianEarnings = df["Median"].tolist()
totals = df["Total"].tolist()
unemployment_rates = df["Unemployment_rate"].tolist()
categories = df["Major_category"].tolist()


# Page configuration
st.set_page_config(page_title="College Major Helper")


# Function: apply_university_styling()
  # Purpose: Applies the university styling to the entire page
  # Parameters: none
  # Returns: nothing; just applies general stylies
# styles by Claude AI
def apply_university_styling():
   st.markdown("""
   <style>
       /* Main theme colors */
       :root {
           --primary: #0A2240;       /* Deep Navy Blue */
           --secondary: #8B0000;     /* Dark Red */
           --accent: #C5B358;        /* Gold */
           --light-bg: #F5F5F5;      /* Light Gray */
           --text: #333333;          /* Dark Gray */
           --light-text: #FFFFFF;    /* White */
       }
      
       /* Body styling */
       .main {
           background-color: var(--light-bg);
           color: var(--text);
           font-family: "Palatino Linotype", "Book Antiqua", Palatino, serif;
       }
      
       /* Header styling */
       h1, h2, h3 {
           font-family: "Trajan Pro", "Times New Roman", serif;
           color: var(--primary);
           font-weight: 600;
           letter-spacing: 1px;
       }
      
       h1 {
           border-bottom: 4px solid var(--accent);
           padding-bottom: 10px;
           text-align: center;
       }
      
       h2 {
           padding-bottom: 5px;
           margin-top: 30px;
       }
      
       /* University seal style container */
       .university-seal {
           background-color: var(--primary);
           color: var(--light-text);
           text-align: center;
           padding: 20px;
           border-radius: 10px;
           margin: 20px 0;
           border: 5px double var(--accent);
       }
      
       /* Button styling */
       .stButton > button {
           background-color: var(--primary);
           color: var(--light-text);
           font-weight: bold;
           border: 2px solid var(--accent);
           border-radius: 4px;
           transition: all 0.3s;
           font-family: "Palatino Linotype", serif;
       }
      
       .stButton > button:hover {
           background-color: var(--accent);
           color: var(--primary);
           border: 2px solid var(--primary);
           transform: scale(1.02);
       }
      
      
       /* Form fields */
       .stTextInput > div > div > input {
           border: 1px solid var(--primary);
           border-radius: 4px;
           padding: 10px;
           font-family: "Palatino Linotype", serif;
       }
      
       /* Create decorative elements for headers */
       .header-decoration {
           display: flex;
           align-items: center;
           justify-content: center;
           margin: 10px 0;
       }
      
       .header-line {
           flex-grow: 1;
           height: 2px;
           background-color: var(--accent);
       }
      
       .header-emblem {
           font-size: 24px;
           margin: 0 15px;
           color: var(--secondary);
       }
   </style>
   """, unsafe_allow_html=True)


# Apply university styling
apply_university_styling()


# Header
# styles by Claude AI
st.markdown("""
<style>
   /* University seal style container */
   .university-seal {
       background-color: var(--primary);
       color: var(--light-text);
       text-align: center;
       padding: 20px;
       border-radius: 10px;
       margin: 20px 0;
       border: 5px double var(--accent);
   }
</style>


<div class="university-seal">
   <h1 style="color: white; margin-bottom: 5px;">COLLEGE MAJOR HELPER</h1>
   <div style="font-size: 18px; font-style: italic; color: #C5B358;">Guiding Your Academic Journey</div>
</div>


""", unsafe_allow_html=True)


# Introduction section
# Styles by Claude AI
st.markdown("""
<div style="text-align: center; margin: 20px 0;">
   <h2>Are you ready to discover your ideal major?</h2>
</div>
""", unsafe_allow_html=True)


# Link to data source with styled button
# Styles by Claude AI
st.markdown("""
<div style="text-align: center; margin: 20px 0;">
   <a href="https://drive.google.com/file/d/1auROzXY9tR8M-F23dK8QQOEtlzEm7REJ/view" target="_blank"
      style="background-color: #0A2240; color: white; padding: 8px 15px; text-decoration: none;
             border-radius: 5px; border: 2px solid #C5B358; font-weight: bold;">
       View Complete Dataset 🔗
   </a>
</div>
""", unsafe_allow_html=True)


st.write("")


# Initialize session state for quiz responses
if 'quiz_answers' not in st.session_state:
  st.session_state.quiz_answers = {}
if 'quiz_completed' not in st.session_state:
  st.session_state.quiz_completed = False


# ------------------------------
# Quiz Section
# ------------------------------




# Styles by Claude AI
st.markdown("""
<div style="text-align: center; margin: 20px 0; margin-bottom: 0;">
   <h2>Major Selection Quiz</h2>
</div>
""", unsafe_allow_html=True)


if not st.session_state.quiz_completed:
  with st.form("major_quiz"):
      st.write("Answer these questions to help narrow down your major choices:")
      # Question 1
      q1 = st.radio(
          "1. What salary range are you expecting after graduation?",
          ["Under $40,000", "$40,000 - $60,000", "$60,000 - $80,000", "Over $80,000"]
      )
      # Question 2
      q2 = st.radio(
          "2. How important is job security to you?",
          ["Not important", "Somewhat important", "Very important", "Critical"]
      )
      # Question 3
      q3 = st.multiselect(
          "3. Which fields interest you the most?",
          ["Business", "Engineering", "Arts", "Science", "Healthcare", "Education", "Technology"]
      )
      # Question 4
      q4 = st.slider(
          "4. How many years of education are you willing to commit to?",
          min_value=2, max_value=10, value=4
      )
      # Question 5
      q5 = st.radio(
          "5. Do you prefer working with people, data, or things?",
          ["People", "Data", "Things", "A mix of these"]
      )
    
      # Submit button
      submitted = st.form_submit_button("Submit Quiz")
      if submitted:
          # Store answers in session state
          st.session_state.quiz_answers = {
              "Salary Expectations": q1,
              "Job Security Importance": q2,
              "Fields of Interest": ",".join(q3),
              "Education Years": str(q4),
              "Work Preference": q5
          }
          st.session_state.quiz_completed = True
          st.success("Quiz completed! Scroll down to see your results and recommended majors.")


# Display quiz results if completed
if st.session_state.quiz_completed:
  st.subheader("Recommended Majors Based on Your Answers")
  recommended_majors = []
  # get quiz results that we will use to find recomended majors
  salary_expectation = st.session_state.quiz_answers["Salary Expectations"]
  job_security = st.session_state.quiz_answers["Job Security Importance"]
  FOIs = st.session_state.quiz_answers["Fields of Interest"].split(",")
  min_salary = 0
  max_salary = 0


  # get salary range
  if salary_expectation == "Under $40,000":
      min_salary = 0
      max_salary = 40000
  elif salary_expectation == "$40,000 - $60,000":
      min_salary = 40000
      max_salary = 60000
  elif salary_expectation == "$60,000 - $80,000":
      min_salary = 60000
      max_salary = 80000
  else:  # Over $80,000
      min_salary = 80000
      # none of these jobs will pay a trillion duh
      max_salary = 999999999
   # set unemployment limit for job security
  unemployment_threshold = 1
  if job_security == "Critical":
      unemployment_threshold = 0.04
  elif job_security == "Very important":
      unemployment_threshold = 0.055
  elif job_security == "Somewhat important":
      unemployment_threshold = 0.07
   # Filter majors by salary range and jobn security preferenche
  for x in range(len(majors)):
      if (min_salary <= medianEarnings[x] <= max_salary) and (unemployment_rates[x] <= unemployment_threshold) and (categories[x] in FOIs):
         major_name = majors[x]
         earnings = medianEarnings[x]
         unemployment = unemployment_rates[x]
         recommended_majors.append([major_name, earnings, unemployment])
   # Sort by earnings and take top 5
  # need function for sorting
 
  # Function: sort_by_earnings
  # Purpose: Provides a key function for sorting recommended majors by earnings
  # Parameters:
  #   major_info: A list containing major information where the second element [1] is earnings
  # Returns:
  #   The earnings value to be used for sorting
  def sort_by_earnings(major_info):
     return major_info[1]
 
  recommended_majors.sort(key=sort_by_earnings, reverse=True)
  top_recommendations = []
  for x in range(min(5,len(recommended_majors))):
      top_recommendations.append(recommended_majors[x])


  # Create a recommendations frame to display (if statement written by Claude AI)
  if top_recommendations:
      # Prepare data for DataFrame
      major_names = []
      formatted_earnings = []
      formatted_unemployment = []
    
      for rec in top_recommendations:
          major_names.append(rec[0])
          formatted_earnings.append(f"${rec[1]:,.2f}")
          formatted_unemployment.append(f"{rec[2]*100:.2f}%")
    
      recommendations_data = {
          "Major": major_names,
          "Median Earnings": formatted_earnings,
          "Unemployment Rate": formatted_unemployment
      }
      recommendations_df = pd.DataFrame(recommendations_data)
      st.dataframe(recommendations_df)
  else:
      st.warning("No majors match your criteria exactly. Try adjusting your answers.")


  # Add a button to retake the quiz
  if st.button("Retake Quiz"):
      st.session_state.quiz_completed = False
      st.session_state.quiz_answers = {}


st.write("")


# ------------------------------
# Buttons and Entry field for Quick Info Section
# ------------------------------


# Styles by Claude AI
st.markdown("""
<div style="text-align: center; margin: 20px 0; margin-bottom: 0;">
   <h2>Learn more about your major</h2>
</div>
""", unsafe_allow_html=True)


# Input field
major = st.text_input("Enter a major:").strip()


# Functions


# Function: show_median_earnings
# Purpose: Displays median earnings information for the specified major and creates a bar chart
#          comparing it with surrounding majors in the ranking
# Parameters: None (uses the global 'major' variable)
# Returns: None, displays info and chart directly in the Streamlit UI
def show_median_earnings():
  if major in majors:
      # Find the selected major
      idx = 0
      for x in range(len(majors)):
          if majors[x] == major:
              idx = int(ranks[x]) - 1
              median = medianEarnings[x]
      st.info(f"The median earnings of an employed {major} graduate is ${median:,} annually.")


      # Create empty lists for the bar chart
      bar_majors = []
      bar_earnings = []
      for x in range(idx - 3, idx + 4):
          bar_majors.append(majors[x])
          bar_earnings.append(medianEarnings[x])
       # plotly chart (written by Claude AI)
      fig = px.bar(
          x=bar_majors,
          y=bar_earnings,
          title="Median Earnings Comparison",
          labels={"x": "Majors", "y": "Median Earnings ($)"},
          text=bar_earnings,  # Show the values on top of bars
      )
      fig.update_traces(
          marker_color='royalblue',
          marker_line_color='black',
          marker_line_width=1,
          texttemplate='$%{text:,.0f}',  # Format with dollar sign and comma
          textposition='outside'
      )
      fig.update_layout(
          width=800,
          height=800,
          xaxis_tickangle=-45,
          plot_bgcolor='white',
          yaxis_gridcolor='lightgray'
      )
      st.plotly_chart(fig, use_container_width=True)
  else:
      st.error(f"{major} is not a major in the dataset")


# Function: show_rankings
# Purpose: Creates a markdown table showing all majors ranked by median earnings,
#          with the specified major highlighted
# Parameters: None (uses the global 'major' variable)
# Returns: A string containing markdown-formatted table of all majors and their rankings
def show_rankings():
  rows = []
  for x in range(len(df)):
      row = df.loc[x]
      # (if statement writtten by Claude AI) this is cuz css styles confuse me and markdonwn too but thats easier
      if row['Major'] == major:
          # highlight selected major using markdown and html with embedded css styles
          rows.append(f"| <span style='background-color: #ffffa3; color: black; padding: 2px 4px; border-radius: 3px;'>{int(row['Rank'])}</span> | <span style='background-color: #ffffc0; color: black; padding: 2px 4px; border-radius: 3px;'>{row['Major']}</span> | <span style='background-color: #ffffdd; color: black; padding: 2px 4px; border-radius: 3px;'>${row['Median']:,.2f}</span> |")
      else:
          # regular row
          rows.append(f"| {int(row['Rank'])} | {row['Major']} | ${row['Median']:,.2f} |")
  # combine rows and wrap in table
  # Header row
  header = "| Rank | Major | Median Earnings |\n| --- | --- | --- |"
  table_markdown = header + "\n" + "\n".join(rows)
  return table_markdown


# Function: get_rank
# Purpose: Displays the rank of the specified major based on median earnings
# Parameters: None (uses the global 'major' variable)
# Returns: None, displays info directly in the Streamlit UI
def get_rank():
  if major in majors:
      for x in range(len(majors)):
          if majors[x] == major:
              rank = ranks[x]
      st.info(f"{major} is ranked #{int(rank)} out of all college majors by median earnings in their respective fields.")
  else:
      st.error(f"{major} is not a major in the dataset")


# Function: show_unemployment
# Purpose: Displays unemployment information for the specified major and creates a histogram
#          showing the distribution of unemployment rates across all majors
# Parameters: None (uses the global 'major' variable)
# Returns: None, displays info and chart directly in the Streamlit UI
def show_unemployment():
  if major in majors:
      for x in range(len(majors)):
          if majors[x] == major:
              total = totals[x]
              gen_unemployment = unemployment_rates[x]
      st.info(f"The general unemployment rate for {major} graduates in their respective field (out of {int(total):,} surveyed) is {round(gen_unemployment*100,2)}% ")
      # Create the figure
      fig, ax = plt.subplots(figsize=(10, 6))
      # filter rates to percentages
      filtered_unemployment_rates=[]
      for x in unemployment_rates:
          filtered_unemployment_rates.append(round(x*100,2))
      ax.hist(filtered_unemployment_rates, bins=20, color='teal', alpha=0.7, edgecolor='black')
      plt.xlabel('Unemployment Rate (%)')
      plt.ylabel('Number of Majors')
      plt.title('Distribution of Unemployment Rates Across All College Majors', fontsize=14)
      ax.axvline(x=round(gen_unemployment*100,2), color='#8B0000', linestyle='--', linewidth=2)
      ax.text(round(gen_unemployment*100,2)+0.5, max(plt.ylim())*0.9,
              f'{major}: {round(gen_unemployment*100,2)}%',
              color='#8B0000', fontweight='bold', fontfamily='serif')
      plt.grid(linestyle='--', alpha=0.7)
      plt.tight_layout()
      # Display in Streamlit
      st.pyplot(fig)
  else:
      st.error(f"{major} is not a major in the dataset")


# buttons for quick info


# Create session state variables to track button states
if 'show_earnings' not in st.session_state:
  st.session_state.show_earnings = False
if 'show_rankings' not in st.session_state:
  st.session_state.show_rankings = False
if 'show_unemployment' not in st.session_state:
  st.session_state.show_unemployment = False


# Function: toggle_earnings
# Purpose: Callback function that toggles the visibility state of earnings information
# Parameters: None
# Returns: None, modifies the st.session_state.show_earnings variable
def toggle_earnings():
  st.session_state.show_earnings = not st.session_state.show_earnings


# Function: toggle_rankings
# Purpose: Callback function that toggles the visibility state of rankings information
# Parameters: None
# Returns: None, modifies the st.session_state.show_rankings variable
def toggle_rankings():
  st.session_state.show_rankings = not st.session_state.show_rankings


# Function: toggle_unemployment
# Purpose: Callback function that toggles the visibility state of unemployment information
# Parameters: None
# Returns: None, modifies the st.session_state.show_unemployment variable
def toggle_unemployment():
  st.session_state.show_unemployment = not st.session_state.show_unemployment


# display buttons
col1, col2, col3 = st.columns([1,1,1])
with col1:
  st.button("See Median Earnings by Degree", on_click=toggle_earnings)
with col2:
  st.button("See the Rank of Each Major by Median Earnings", on_click=toggle_rankings)
with col3:
  st.button("See Unemployment Rate by Degree", on_click=toggle_unemployment)


# Display content based on session state
if st.session_state.show_earnings:
  show_median_earnings()


if st.session_state.show_rankings:
  get_rank()
  st.markdown(show_rankings(), unsafe_allow_html=True)


if st.session_state.show_unemployment:
  show_unemployment()

