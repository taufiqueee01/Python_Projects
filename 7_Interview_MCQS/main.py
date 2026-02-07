import time

questions = [
    {
        "q": "What is mutable in Python?",
        "opts": ["A) Tuple", "B) List", "C) String", "D) Integer"],
        "ans": "B"
    },
    {
        "q": "Output of: print(2 ** 3)",
        "opts": ["A) 6", "B) 9", "C) 8", "D) 5"],
        "ans": "C"
    },
    {
        "q": "Keyword to define a function?",
        "opts": ["A) func", "B) def", "C) function", "D) define"],
        "ans": "B"
    }
]

def run_quiz():
    print("--- Interview Speed Quiz ---")
    input("Press Enter to start timer...")
    
    start_time = time.time()
    score = 0
    
    for i, item in enumerate(questions):
        print(f"\nQ{i+1}: {item['q']}")
        for opt in item['opts']:
            print(opt)
        
        user_ans = input("Your Answer (A/B/C/D): ").upper().strip()
        
        if user_ans == item['ans']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. Correct was {item['ans']}")
            
    end_time = time.time()
    duration = round(end_time - start_time, 2)
    
    print("\n--- Results ---")
    print(f"Score: {score}/{len(questions)}")
    print(f"Time Taken: {duration} seconds")
    
    # Save high score logic
    with open("quiz_history.txt", "a") as f:
        f.write(f"Score: {score}, Time: {duration}s\n")

if __name__ == "__main__":
    run_quiz()
