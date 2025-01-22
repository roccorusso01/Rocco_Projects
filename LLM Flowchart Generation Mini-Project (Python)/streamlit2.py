#NEED TO KEY IN streamlit run streamlit2.py IN THE TERMINAL TO RUN THE CODE
#This is to create a subprocess that will engage the command line to run the streamlit app

"""
import subprocess
command = "streamlit run streamlit2.py"
subprocess.run(command, shell=True)
"""
    



#from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv
from genai_center_integration import GenAICenterLLM
from mermaid_func import *
import streamlit.components.v1 as components

import requests
from typing import List, Optional, Dict, Any, Mapping

def main():

    st.title("💬 Flowchartbot")
    st.caption("🚀 A Streamlit chatbot powered by OpenAI")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Input the steps that you wish to encapsulate in a flowchart."}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    #Allow users to select which model this is run on.
    model_selection = st.selectbox("What LLM model would you like to generate this flowchart in?", ("gpt-3", "gpt-4"))

    #Set Up Checkboxes allowing users some choice in how the code is generated
    download = st.checkbox("Download as a PNG file")
    branching = st.checkbox("Encourage Branching")

    if prompt := st.chat_input():
        """if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()"""

        load_dotenv(dotenv_path='.env')
        
        #Use the api_key and the model selected by the user to instantiate the LLM
        api_key="was_hardcoded_for_testing"
        model = model_selection
        client = GenAICenterLLM(model, api_key)
        #client = OpenAI(api_key=openai_api_key)
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        #If the user selected branching use a different prompt that encourages branching to chat gpt to generate the intial steps
        if branching:
            first_call = client("Take the following input and create a branching list of steps that represent the following input: " + prompt)
        else:
            first_call = client("Take the following input and create a short list of steps that represent the following input: " + prompt)

        #Take the result of the first call to the LLM and feed it back in with additional instructions to create mermaid markdown
        response = client("Take the following text and generate mermaidjs markdown with it (Don't return anything else other than the mermaid markdown) (For Example this would be a valid response: graph TD; A[Go to the store] --> B[Shop]; B --> C[Go home]) Make sure to include a semicolon at the end of each line : " + first_call)

        #Sometimes the response will return with mermaid and three backquotes at the start breaking the mermaid generator this removes those
        if "mermaid" in response:
            response = response.replace("mermaid", "", 1)
            response = response.replace("```", "")
        
        #response = client.chat.completions.create(model="gpt-4.0", messages=st.session_state.messages)
        #msg = response.choices[0].message.content = [{"role": "assistant", "content": "How may I assist?"}]
        #st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(response)
        #st.write(response)
        print(response)

        #Generates the Mermaid Diagram using the response from Chat GPT
        diagram = generate_mermaid(response)
        # If the Mermaid errors this removes parenthesis from the response (most common error is parenthesis in the response) and reruns the mermaid generation
        if diagram._repr_html_() == "invalid encoded code":
            response = response.replace("(", '')
            response = response.replace(")", '')
            diagram = generate_mermaid(response)
        
        #Displays the mermaid in streamlit using the HTML code representing the mermaid diagram
        components.html(diagram._repr_html_(), height = 500, scrolling = True)

        #If the user opted to download the mermaid file this dowloads the file named mermaid diagram to the local directory this file is run from.
        if download:
            if diagram._repr_html_() == "invalid encoded code":
                st.write("Sorry the mermaid code was invalid an thus cannot be downloaded please try again with a different input")
            else:
                st.write("Mermaid diagram downloaded as mermaid_diagram.png")
                save_mermaid(diagram, "mermaid_diagram")

        
    #user_steps = st.chat_message("assistant").write(response)

if __name__ == "__main__":
    main()
    
