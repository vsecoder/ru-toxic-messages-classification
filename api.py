import pickle
import dill
import nltk

import time


class API:
    """"""

    def __init__(self):
        pkl_filename = "pickle_model.pkl"
        vct_filename = "vectorizer.pkl"

        nltk.download('punkt')
        nltk.download('stopwords')

        with open(pkl_filename, 'rb') as file:
            self.pickle_model = pickle.load(file)
            
        with open(vct_filename, 'rb') as file:
            self.pickle_vectorizer = dill.load(file)


    def check(self, text):
        """"""
        start_time = time.time()
        answer =  self.pickle_model.predict_proba(
            self.pickle_vectorizer.transform(
                [text]
            )
        )

        return {
            #"text": text,
            "toxic_percent": round(answer[0][1] * 100, 2),
            "neutral_percent": round(answer[0][0] * 100, 2),
            "work_time": f'{round(time.time() - start_time, 4)}s'
        }


if __name__ == "__main__":
    api = API()
    print(api.check("ты пидор"))
