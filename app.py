import os
from dotenv import load_dotenv
from google import genai

MODEL_NAME = "gemini-3.5-flash"

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def security_agent(code):

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=f"""
You are a security code reviewer.

Review the following code.

Look for:
- hardcoded passwords
- API keys
- SQL injection risks
- unsafe input handling

Return findings in bullet points.

Code:

{code}
"""
    )

    return response.text


def readability_agent(code):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=f"""
You are a readability and maintainability code reviewer.

Review the following code.

Look for:
- unclear variable names
- poor structure
- missing comments
- duplicated logic
- maintainability issues

Return findings in bullet points.

Code: 

{code}
"""
    )
    return response.text


def performance_agent(code):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=f"""
You are a performance code reviewer.

Review the following code.

Look for:
- unnecessary loops
- repeated calculations
- inefficient string concatenation
- unnecessary database queries
- memory-heavy operations
- algorithmic complexity
- anti-patterns that may slow the program down

Return findings in bullet points.
If there are no major performance issues, clearly state it.

Code:
{code}
"""
    )
    return response.text


def bug_agent(code):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=f"""
You are a bug detection code reviewer.

Review the following code.

Look for:
- logical bugs
- edge cases
- potential runtime errors
- incorrect assumptions
- missing validation

Return findings in bullet points.

Code:
{code}
"""
    )
    return response.text


def summary_agent(security_report, readability_report, performance_report, bug_report):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=f"""
You are a pro software engineer reviewer.

Summarize the following reports.

Security Report:
{security_report}

Readability Report:
{readability_report}

Performance Report:
{performance_report}

Bug Report:
{bug_report}

Provide:
1. Overall risk level
2. Most critical issues
3. Recommend fixes
4. Final summary

Return findings in bullet points.
"""
    )
    return response.text

with open("test.py", "r") as file:
    code = file.read()

print("Running Security Agent...")
security_report = security_agent(code)

print("Running Readability Agent...")
readability_report = readability_agent(code)

print("Running Performance Agent...")
performance_report = performance_agent(code)

print("Running Bug Agent...")
bug_report = bug_agent(code)

print("Running Summary Agent...")
final_report = summary_agent(
    security_report,
    readability_report,
    performance_report,
    bug_report
)

print("===== SECURITY REPORT =====")
print(security_report)

print("\n===== READABILITY REPORT =====")
print(readability_report)

print("\n===== PERFORMANCE REPORT =====")
print(performance_report)

print("\n===== BUG REPORT =====")
print(bug_report)

print("\n===== FINAL SUMMARY REPORT =====")
print(final_report)


