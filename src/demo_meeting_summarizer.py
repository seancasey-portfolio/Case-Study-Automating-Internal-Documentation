# TSD-ID: SSD-2
# Filename: demo_meeting_summarizer.py (v1.1)
# Purpose: To provide a clear, simplified demonstration of how to automate the creation
#          of internal documentation by extracting key information from unstructured text.
#          This script serves as the technical appendix for the
#          "Case-Study-Automating-Internal-Documentation" portfolio piece.

# --- INPUT DATA ---
# A hard-coded multi-line string representing a fictional meeting transcript.
# It's intentionally conversational and contains information mixed with filler.
MEETING_TRANSCRIPT = """
Alright team, let's kick off the Project Nightingale sync. First up, financials.
Sarah, what's the latest on the budget?
Sarah: We're currently tracking at 75% of our allocated budget for Q3, which is right on target.
We need to finalize the vendor contract by next Friday.
John: Okay, great. Next, the Project Timeline. Where are we with the alpha release?
Mike: We've hit a small snag with the integration module. I think it will push the timeline
back by about a week. The new projected date for the alpha is October 28th.
John: A week is acceptable. Let's make sure we document that.
Finally, let's talk about Key Decisions from this meeting. We've agreed to move forward
with the 'Orion' UI framework. I also want to confirm the decision to table the
internationalization feature until Phase 2.
All: Agreed.
John: Perfect. That's all for today. Let's get back to it. The budget is solid, and the
timeline slip is manageable.
"""

# --- CONFIGURATION ---
# In a real-world scenario, these themes would be key areas of interest for stakeholders.
# They act as a filter to extract only the most relevant information from the noise.
KEY_THEMES = [
    "Budget",
    "Project Timeline",
    "Key Decisions"
]

def summarize_transcript(transcript, themes):
    """
    Orchestrates the process of creating a structured summary from raw text.

    This function represents the core methodology of the case study: taking a large
    volume of unstructured information and programmatically distilling it into a
    concise, structured, and easy-to-read format for internal documentation.

    Args:
        transcript (str): The raw text of the meeting.
        themes (list): A list of keywords to guide the summary.

    Returns:
        str: A Markdown-formatted summary string.
    """
    
    # --- STEP 1: PRE-PROCESSING & SENTENCE EXTRACTION ---
    # The first step is to break the unstructured block of text into manageable
    # chunks, in this case, sentences. This allows us to analyze each piece
    # of information individually.
    print("Step 1: Parsing transcript into individual sentences...")
    
    # A simple split by period is sufficient for this demonstration.
    sentences = transcript.split('.')
    print(f"  -> Found {len(sentences)} sentences to analyze.\n")

    # --- STEP 2: THEME-BASED INFORMATION RETRIEVAL ---
    # We now iterate through the sentences and extract only those that are relevant
    # to our predefined key themes. This simulates an AI's ability to identify and
    # pull out the most important points from a conversation.
    print("Step 2: Identifying and extracting sentences relevant to key themes...")
    
    # We'll store the results in a dictionary to keep them organized by theme.
    themed_sentences = {theme: [] for theme in themes}

    for sentence in sentences:
        if not sentence.strip():
            continue
        for theme in themes:
            # A simple, case-insensitive check to see if the theme is mentioned.
            if theme.lower() in sentence.lower():
                themed_sentences[theme].append(sentence.strip())
                
    print("  -> Extraction complete.\n")

    # --- STEP 3: STRUCTURED SUMMARY GENERATION ---
    # The final step is to format the extracted information into a clean,
    # professional, and easily digestible document. Markdown is used here as it's a
    # common standard for internal wikis and documentation platforms.
    print("Step 3: Formatting extracted information into a Markdown summary...")
    
    # REVISION v1.1: The dynamic date generation has been replaced with a static
    # placeholder to ensure the script has zero external dependencies, in full
    # compliance with the "Minimal Dependencies" governing principle.
    summary_parts = ["# Meeting Summary - YYYY-MM-DD\n"]
    
    for theme, points in themed_sentences.items():
        if points:
            summary_parts.append(f"## {theme}\n")
            for point in points:
                summary_parts.append(f"- {point}.\n")
            summary_parts.append("\n")
            
    print("  -> Formatting complete.\n")
    
    return "".join(summary_parts)

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print("--- Starting Meeting Summarizer Script ---\n")
    
    final_summary = summarize_transcript(MEETING_TRANSCRIPT, KEY_THEMES)
    
    print("--- Script Complete ---\n")
    
    print("Final Generated Summary:")
    print("-------------------------")
    print(final_summary)
