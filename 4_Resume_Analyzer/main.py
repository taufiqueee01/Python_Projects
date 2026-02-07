def analyze_resume():
    print("--- Resume Analyzer ---")
    print("Paste your resume text below (Press Enter then Ctrl+D or Ctrl+Z to finish):")
    
    try:
        lines = []
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass
    
    resume_text = " ".join(lines).lower()
    
    required_keywords = {
        "python", "java", "sql", "html", "css", 
        "project", "degree", "university", "communication",
        "teamwork", "git", "analysis"
    }
    
    found_keywords = set()
    for word in required_keywords:
        if word in resume_text:
            found_keywords.add(word)
            
    score = int((len(found_keywords) / len(required_keywords)) * 100)
    
    print("\n--- Analysis Report ---")
    print(f"Resume Score: {score}/100")
    
    missing = required_keywords - found_keywords
    if missing:
        print("\nMissing Keywords (Consider adding these):")
        print(", ".join(list(missing)))
    else:
        print("Excellent! Your resume covers all key areas.")

if __name__ == "__main__":
    analyze_resume()
