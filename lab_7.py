import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Perceptron ангилалын алгоритм
class Perceptron:
    def __init__(self, num_features):
        # Жин (weights)-ийг эхлээд 0 утгаар тохируулна
        self.weights = np.zeros(num_features)
    
    def predict(self, x):
        # Хэрэв x-ийн жинтэй утга 0-оос их байвал 1 гэж тооцоолно
        return 1 if np.dot(self.weights, x) > 0 else 0
    
    def train(self, X, y, learning_rate=0.1, epochs=1):
        # Сургалт хийх үе шатууд
        for epoch in range(epochs):
            for i in range(len(X)):
                # Урьдчилсан таамаглал гаргах
                prediction = self.predict(X[i])
                # Алдаа тооцоолох
                error = y[i] - prediction
                # Алдааг засахад жингүүдийг шинэчлэх
                self.weights += learning_rate * error * X[i]

# Файл байрлах зам
path = r"D:\hicheel\AI\lab_7\IRIS.csv"
import pandas as pd


try:
    # Файлыг уншиж, мөр тус бүрийг салгаж өгнө
    with open(path, "r") as file:
        lines = file.readlines()
    
    # Мөр бүрийг боловсруулж, хоосон зайг болон хэрэггүй тэмдгүүдийг арилгана
    data = [[item.strip().replace('"', '') for item in line.split(",")] for line in lines[1:]]  # Хөрвүүлэх мөрийн толгойн мөрийг орхино
    
    # DataFrame үүсгэх
    df = pd.DataFrame(data, columns=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])
    
    # Хэмжээтэй багануудыг тоон утгаар хөрвүүлнэ
    for col in ["sepal_length", "sepal_width", "petal_length", "petal_width"]:
        df[col] = pd.to_numeric(df[col])

    # "species" баганаг LabelEncoder ашиглан кодлох
    le = LabelEncoder()
    df['species'] = le.fit_transform(df['species'])

    # "bias" буюу онцлог нэмэх
    df.insert(0, 'bias', 1)

    # Онцлог болон хариу тэмдгийг ялгах
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values

    # Сургалт ба тестийн мэдээлэлд хуваах
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

    # Perceptron алгоритм ашиглан сургалт хийх
    num_features = X_train.shape[1]
    perceptron = Perceptron(num_features)
    perceptron.train(X_train, y_train)

    # Тестийн таамаглал хийх
    y_test_pred = [perceptron.predict(x) for x in X_test]
    test_accuracy = accuracy_score(y_test, y_test_pred)
    print(f"[test accucary]: {test_accuracy:.2f}")
    print("weight:", perceptron.weights[1:])
    conf_matrix = confusion_matrix(y_test, y_test_pred)
    print("confusion  матрицууд:")
    print(conf_matrix)

except KeyError:
    print("'species' багана алга эсвэл буруу нэртэй байна. Файл бүтэц шалгана уу.")
except Exception as e:
    print("Алдаа гарлаа:", e)
except FileNotFoundError:
    print("Файл олдсонгүй. Зам болон файлын нэрийг шалгана уу.")







# Кодиудын тайлбар:
# Perceptron ангилал:
# Perceptron классын хувьд, энэ нь суралцах процесстэй, таамаглал хийх чадвартай бөгөөд жингүүдийг шинэчилж сургадаг.
# Файлыг унших:
# IRIS.txt файлыг уншиж, өгөгдлийг зөв форматтай болгож DataFrame үүсгэдэг.
# Хэмжээтэй өгөгдлийг боловсруулж хөрвүүлэх:
# Тусгай багануудыг (жишээ нь sepal_length, sepal_width гэх мэт) тоон утгаар хөрвүүлж, species баганад Label Encoding хийдэг.
# Тренинг болон Тест:
# Perceptron-ийг сургасан дараа тестийн нарийвчлал болон будлиан матрицыг хэвлэдэг.
# Хүснэгтүүд:
# Тестийн нарийвчлал: Сургалтаар олсон моделийг тестийн өгөгдөл дээр туршиж, нарийвчлалыг тооцоолно.
# Жинүүд: Сургалтын явцад Perceptron модель хэрхэн суралцаж байгаа жингүүдийг хэвлэдэг.
# Будлиан матрицууд: Хүлээж авсан хариу болон бодит хариуг харьцуулж, будлиан матрицыг харуулна.
# Таны кодыг монгол хэл дээр тайлбарлаж өгсөн бөгөөд хэрэв ямар нэгэн асуудал гарах юм бол надад мэдэгдээрэй!






