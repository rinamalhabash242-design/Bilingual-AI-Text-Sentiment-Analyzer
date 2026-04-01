# ---------------------------------------------------------
# Project: Bilingual AI Text Sentiment Analyzer
# Developer: [Renam Mohammad Al-habash]
# Technology: Python (Natural Language Processing - NLP)
# ---------------------------------------------------------

def text_intelligence_analyzer(text):
    """
    Analyzes text to determine sentiment (Positive, Negative, or Neutral)
    based on a bilingual dictionary (English & Arabic).
    """
    
    # --- Expanded Bilingual Dictionary ---
    positive_words = [
        'good', 'great', 'excellent', 'happy', 'amazing', 'success', 'perfect', 
        'love', 'best', 'helpful', 'satisfied', 'wonderful', 'efficient',
        'ممتاز', 'رائع', 'سعيد', 'ناجح', 'مبدع', 'جميل', 'شكرا', 'أشكركم', 
        'بطل', 'كفو', 'تطور', 'مفيد', 'متقن'
    ]
    
    negative_words = [
        'bad', 'poor', 'sad', 'fail', 'error', 'difficult', 'slow', 'worst', 
        'angry', 'terrible', 'hate', 'disappointed', 'issue', 'broken',
        'سيء', 'ضعيف', 'حزين', 'فاشل', 'خطأ', 'صعب', 'بطيء', 'أسوأ', 
        'غاضب', 'مشكلة', 'تأخير', 'ضعف', 'خلل'
    ]

    # --- Data Processing ---
    # Convert to lowercase and split into words
    input_words = text.lower().split()
    word_count = len(input_words)
    
    score = 0
    detected_positives = []
    detected_negatives = []

    # --- Sentiment Analysis Logic ---
    for word in input_words:
        # Clean punctuation from words (e.g., "Good!" -> "Good")
        clean_word = word.strip('.,!?;:()')
        
        if clean_word in positive_words:
            score += 1
            detected_positives.append(clean_word)
        elif clean_word in negative_words:
            score -= 1
            detected_negatives.append(clean_word)

    # --- Determine Sentiment Result ---
    if score > 0:
        sentiment = "POSITIVE 😊"
    elif score < 0:
        sentiment = "NEGATIVE 😔"
    else:
        sentiment = "NEUTRAL 😐"

    # --- Professional Analysis Report ---
    print("\n" + "="*45)
    print("      AI TEXT INTELLIGENCE REPORT")
    print("="*45)
    print(f" > Total Words Analyzed : {word_count}")
    print(f" > Detected Sentiment   : {sentiment}")
    print(f" > Sentiment Score      : {score}")
    print("-" * 45)
    print(f" [+] Positive Keywords: {', '.join(detected_positives) if detected_positives else 'None'}")
    print(f" [-] Negative Keywords: {', '.join(detected_negatives) if detected_negatives else 'None'}")
    print("="*45 + "\n")

# --- Main Interface ---
if __name__ == "__main__":
    print("Welcome to the AI Text Analyzer System")
    print("Enter 'quit' to exit the program.")
    
    while True:
        user_input = input("Enter text to analyze (EN/AR): ")
        if user_input.lower() == 'quit':
            print("Exiting System... Goodbye!")
            break
        
        if not user_input.strip():
            print("Please enter some text to start analysis.")
            continue
            
        text_intelligence_analyzer(user_input)
