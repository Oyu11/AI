import re
import math
import os
from collections import defaultdict

# Имэйлээс агуулга унших функц
def read_email_content(file_path):
    with open(file_path, 'r', encoding='latin-1') as f:
        return f.read()

# Имэйлийн агуулгыг үгсийн жагсаалт болгон задлах
def tokenize(text):         #"Hello, world! Welcome to NLP, it's awesome."
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    return words            #['hello', 'world', 'welcome', 'to', 'nlp', 'it', 's', 'awesome']


# Сургалтын өгөгдлийг (Bag of Words) ашиглан бэлтгэх
def build_vocabulary(email_paths):
    vocabulary = set()
    word_counts = defaultdict(lambda: [0, 0])  # [хог биш тоо, спам тоо]

    for path, label in email_paths:                         #email1.txt (non-spam): "Hello, buy this product."
        content = read_email_content(path)                  #email2.txt (spam): "Buy more products now!"
        words = tokenize(content)                           #Count: {'buy': [1, 1]}

        for word in words:
            vocabulary.add(word)
            word_counts[word][label] += 1  # Шошго дээр үндэслэн тоог нэмэгдүүлэх (0 = хог биш, 1 = спам)

    return vocabulary, word_counts

# Лапласын жигдэлтийг ашиглан үгийн магадлалыг тооцоолох
def calculate_word_probabilities(word_counts, total_spam_words, total_ham_words, vocab_size, alpha):
    word_probs = {}

    for word, (ham_count, spam_count) in word_counts.items():
        prob_w_given_spam = (spam_count + alpha) / (total_spam_words + alpha * vocab_size)
        prob_w_given_ham = (ham_count + alpha) / (total_ham_words + alpha * vocab_size)
        word_probs[word] = (prob_w_given_spam, prob_w_given_ham)

    return word_probs
#P(w ∣ spam)= count ( w | spam) + α / total words in spam + (α × vocab size)

 

# Урьдчилсан магадлалуудыг (P(spam), P(ham)) тооцоолох
def calculate_prior_probabilities(spam_emails, ham_emails, total_emails):
    prob_spam = spam_emails / total_emails  #spam baih magadlal = spam mail too / niit mail too 
    prob_ham = ham_emails / total_emails    ##ham baih magadlal = hamp mail too / niit mail too
    return prob_spam, prob_ham

# Навайв Бэйсийн аргаар шинэ имэйлүүдийг ангилах
def classify(email_content, word_probs, prob_spam, prob_ham, total_spam_words, total_ham_words, vocab_size, alpha):
    words = tokenize(email_content)
    log_spam_prob = math.log(prob_spam)
    log_ham_prob = math.log(prob_ham)

    for word in words:
        if word in word_probs:
            log_spam_prob += math.log(word_probs[word][0])
            log_ham_prob += math.log(word_probs[word][1])
        else:
            # Шинэ үгэнд жигдэлт хийх
            log_spam_prob += math.log(alpha / (total_spam_words + alpha * vocab_size))
            log_ham_prob += math.log(alpha / (total_ham_words + alpha * vocab_size))

    return "spam" if log_spam_prob > log_ham_prob else "ham"

#logP(spam∣email)=logP(spam)+ #∑# logP(word∣spam)
                            #word


# Сургалтын өгөгдлийн замыг тодорхойлох
spam_path = r"D:\hicheel\AI\lab_6\spam_data\spam_data\train\spam"
ham_path = r"D:\hicheel\AI\lab_6\spam_data\spam_data\train\ham"

# Сургалтын өгөгдлийг цуглуулах
spam_file_names = [(os.path.join(spam_path, file), 1) for file in os.listdir(spam_path)]
ham_file_names = [(os.path.join(ham_path, file), 0) for file in os.listdir(ham_path)]

training_data = spam_file_names + ham_file_names

# Урьдчилсан магадлалуудыг тооцоолох
spam_emails = len(spam_file_names)  #1000
ham_emails = len(ham_file_names)    #1000
total_emails = len(training_data)

# Үгийн сан болон үгийн тооллогыг үүсгэх
vocabulary, word_counts = build_vocabulary(training_data)

# Үгсийн нийт тоог тооцоолох
total_spam_words = sum(count[1] for count in word_counts.values())
total_ham_words = sum(count[0] for count in word_counts.values())

# Лапласын жигдэлтийн параметр тохируулах
alpha = 1
vocab_size = len(vocabulary)

# Үгийн болон урьдчилсан магадлалуудыг тооцоолох
word_probs = calculate_word_probabilities(word_counts, total_spam_words, total_ham_words, vocab_size, alpha)
prob_spam, prob_ham = calculate_prior_probabilities(spam_emails, ham_emails, total_emails)

# Шалгалтын имэйлүүдийг ангилах
test_spam_path = r"D:\hicheel\AI\lab_6\spam_data\spam_data\dev\spam"
test_ham_path = r"D:\hicheel\AI\lab_6\spam_data\spam_data\dev\ham"

# Спам имэйлүүдийг шалгах
print("Спам ангиллын үр дүн:")
spam_correct = 0
spam_total_predicted = 0
test_spam_files = [os.path.join(test_spam_path, file) for file in os.listdir(test_spam_path)]

for file_path in test_spam_files:
    content = read_email_content(file_path)
    result = classify(content, word_probs, prob_spam, prob_ham, total_spam_words, total_ham_words, vocab_size, alpha)
    if result == "spam":
        spam_total_predicted += 1
        if result == "spam":
            spam_correct += 1
print("500 spam file dahi real spam ")
print(spam_correct)
print(f"Спам имэйл дээрх үнэн зөв байдал: {(spam_correct / len(test_spam_files)) * 100:.2f}%")

# Хог биш имэйлүүдийг шалгах
print("not spam ангиллын үр дүн:")
ham_correct = 0
ham_total_predicted = 0
test_ham_files = [os.path.join(test_ham_path, file) for file in os.listdir(test_ham_path)]

for file_path in test_ham_files:
    content = read_email_content(file_path)
    result = classify(content, word_probs, prob_spam, prob_ham, total_spam_words, total_ham_words, vocab_size, alpha)
    if result == "ham":
        ham_total_predicted += 1
        if result == "ham":
            ham_correct += 1
print("500 ham file dahi real ham:") 
print(ham_correct)
print(f"Ham mail deerh accuracy: {(ham_correct / len(test_ham_files)) * 100:.2f}%")

# Compute classification metrics for ham (positive class)
print("Ангиллын үр дүн (ham эсвэл not ham):")

# Define TP, FP, FN for unified classification
TP = ham_correct         # True Positives: correctly classified as ham
FP = len(test_spam_files) - spam_correct  # False Positives: classified as ham but actually spam
FN = len(test_ham_files) - ham_correct    # False Negatives: classified as spam but actually ham

# Unified precision, recall, and F1 score for ham vs. not ham
accuracy = (TP + spam_correct) / (len(test_ham_files) + len(test_spam_files))
precision = TP / (TP + FP) if (TP + FP) > 0 else 0
recall = TP / (TP + FN) if (TP + FN) > 0 else 0
f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Precision (Ham): {precision:.2f}")
print(f"Recall (Ham): {recall:.2f}")
print(f"F1 Score (Ham): {f1_score:.2f}")