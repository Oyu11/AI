import math

# Алхам 1: Жишээ өгөгдөл үүсгэх
emails = [
    ('Congratulations! You have won a lottery', 'spam'),
    ('Click here to claim your prize', 'spam'),
    ('Hello friend, how are you?', 'ham'),
    ('Your invoice is attached', 'ham'),
    ('Win money now!', 'spam'),
    ('Meeting at 10 AM tomorrow', 'ham'),
    ('Exclusive offer just for you', 'spam'),
    ('Please see the attached document', 'ham')
]

# Алхам 2: Үгсийн хэтэвчийг бэлтгэх
def create_bag_of_words(emails):
    word_count = {}
    labels = []

    for email, label in emails:
        words = email.lower().split()  # И-мэйлыг жижиг үсгээр болгож, үгсэд хуваана
        labels.append(label)

        for word in words:
            if word not in word_count:
                word_count[word] = [0, 0]  # [spam-д орсон тоо, ham-д орсон тоо]
            if label == 'spam':
                word_count[word][0] += 1
            else:
                word_count[word][1] += 1

    return word_count, labels

# Үгсийн хэтэвчийг үүсгэх
word_count, labels = create_bag_of_words(emails)

# Алхам 3: Ангиллын магадлалуудыг тооцоолох
def calculate_probabilities(word_count, labels):
    total_spam = labels.count('spam')
    total_ham = labels.count('ham')
    total_emails = len(labels)
    total_words = len(word_count)

    probabilities = {}
    for word, counts in word_count.items():
        spam_count = counts[0]
        ham_count = counts[1]

        # Лаплас тэглэлт хийх
        prob_spam = (spam_count + 1) / (total_spam + total_words)
        prob_ham = (ham_count + 1) / (total_ham + total_words)

        probabilities[word] = (prob_spam, prob_ham)

    # Урьдчилсан магадлалуудыг тооцоолох
    prior_spam = total_spam / total_emails
    prior_ham = total_ham / total_emails

    return probabilities, prior_spam, prior_ham

# Магадлалуудыг тооцоолох
probabilities, prior_spam, prior_ham = calculate_probabilities(word_count, labels)

# Алхам 4: Төсөөлөл хийх функц
def predict(email):
    words = email.lower().split()  # И-мэйлыг жижиг үсгээр болгож, үгсэд хуваана
    log_prob_spam = math.log(prior_spam)  # Spam-ийн урьдчилсан магадлалын логийг эхлүүлэх
    log_prob_ham = math.log(prior_ham)    # Ham-ийн урьдчилсан магадлалын логийг эхлүүлэх

    # Ангилал бүрийн лог магадлалыг тооцоолох
    for word in words:
        if word in probabilities:
            log_prob_spam += math.log(probabilities[word][0])  # P(үзэгдэл | spam)-ийн логийг нэмэх
            log_prob_ham += math.log(probabilities[word][1])    # P(үзэгдэл | ham)-ийн логийг нэмэх

    # Хамгийн өндөр магадлалтай ангиллыг буцаах
    return 'spam' if log_prob_spam > log_prob_ham else 'ham'

# Алхам 5: Төсөөлөл хийх
for email, label in emails:
    prediction = predict(email)
    print(f'Email: "{email}" - Predicted: {prediction}, Actual: {label}')
