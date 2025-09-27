import google.generativeai as genai
from database import get_employees, get_leaves

def setup_gemini(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-2.0-flash")

def ask_gemini(model, query):
    employees = get_employees()
    leaves = get_leaves()
    context = f"Employees: {employees}\nLeaves: {leaves}\n\nUser query: {query}"
    response = model.generate_content(context)
    return response.text
