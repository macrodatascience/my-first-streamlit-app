import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('🎈 My First Streamlit App')
st.header("Welcome to the Streamlit Crash Course!")
st.markdown("***In this course, you'll learn how to create interactive web applications using Streamlit. Streamlit is a powerful and easy-to-use framework that allows you to build data-driven applications with minimal code.***")

st.subheader("Course Outline")
st.markdown("""1. Introduction to Streamlit
2. Setting up your environment
3. Creating your first Streamlit app
4. Adding interactivity with widgets
5. Displaying data and visualizations""")

st.badge("Let's get started!!!")

st.write("### 1. Introduction to Streamlit")
st.write("Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. With Streamlit, you can turn your Python scripts into interactive web applications in just a few lines of code.")
st.write("### 2. Setting up your environment")
st.write("To get started with Streamlit, you'll need to install it. You can do this using pip:")
st.code("pip install streamlit matplotlib pandas watchdog")
st.write("### 3. Creating your first Streamlit app")
st.write("Let's create a simple Streamlit app that displays a DataFrame. You can create a new Python file (e.g., `app.py`) and add the following code:")
st.code("""

st.title("My First Streamlit App")
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy'],    
        'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70], 
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']}
df = pd.DataFrame(data) 
st.write("Here's a simple DataFrame:")
st.dataframe(df)""")
st.write("### 4. Adding interactivity with widgets")
st.write("Streamlit provides a variety of widgets that allow you to add interactivity to your app. For example, you can use a slider to filter the DataFrame based on age:")
st.code("""age_filter = st.slider("Select age range", 0, 100, (20, 40))
filtered_df = df[(df['Age'] >= age_filter[0]) & (df['Age'] <= age_filter[1])]
st.write("Filtered DataFrame:") 
st.dataframe(filtered_df)""")
st.write("### 5. Displaying data and visualizations")
st.write("Streamlit also supports various types of visualizations. You can use libraries like Matplotlib, Seaborn, or Plotly to create charts and display them in your app. Here's an example using Matplotlib:")
st.code("""import matplotlib.pyplot as plt
        
ages = filtered_df['Age']
names = filtered_df['Name']
plt.bar(names, ages)
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Age of Individuals')
st.pyplot(plt)""")
st.write("That's it for this crash course! You now have a basic understanding of how to create interactive web applications using Streamlit. Feel free to explore more features and create your own custom apps!")

st.write("### Conclusion")
st.write("In this crash course, we've covered the basics of Streamlit, including how to set up your environment, create a simple app, add interactivity with widgets, and display data and visualizations. Streamlit is a powerful tool that can help you quickly build and share data-driven applications. Happy coding!") 

st.write(" see output in the terminal as below using `streamlit run streamlit_app.py`")
st.write("### additional resources")
st.write("- [Streamlit Documentation](https://docs.streamlit.io/)")
st.write("- [Streamlit GitHub Repository](https://github.com/streamlit/streamlit)")

st.write("### Next Steps")
st.write("Now that you've completed this crash course, you can start building your own Streamlit apps! Here are some ideas to get you started:")
st.write("- Create a dashboard to visualize your data")
st.write("- Build a machine learning model and create an app to make predictions")
st.write("- Integrate APIs to display real-time data") 
st.write("The possibilities are endless! Happy coding and have fun exploring Streamlit!")

st.write("### Final Thoughts")
st.write("Streamlit is a fantastic tool for data scientists and developers who want to quickly create interactive web applications. With its simplicity and powerful features, you can turn your ideas into reality in no time. Don't hesitate to experiment and explore the various functionalities that Streamlit offers. Happy coding!") 

st.write("### Thank You!")
st.write("Thank you for taking the time to go through this Streamlit crash course. I hope you found it helpful and that it inspires you to create amazing applications with Streamlit. If you have any questions or need further assistance, feel free to reach out. Happy coding and best of luck on your Streamlit journey!") 

st.write("### Output from the above code snippets")

st.title("🎈 My First Streamlit App")
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy'],    
        'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70], 
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
        }
df = pd.DataFrame(data)
st.write("Here's a simple DataFrame:")
st.dataframe(df)
age_filter = st.slider("Select age range", 0, 100, (20, 40))
filtered_df = df[(df['Age'] >= age_filter[0]) & (df['Age'] <= age_filter[1])]
st.write("Filtered DataFrame:")

ages = filtered_df['Age']
names = filtered_df['Name']
plt.bar(names, ages)
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Age of Individuals')
st.pyplot(plt)
