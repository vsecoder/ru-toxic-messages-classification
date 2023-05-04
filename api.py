import pickle, sklearn
import dill

import time


class API:
    def __init__(self):
        pkl_filename = "pickle_model.pkl"
        vct_filename = "vectorizer.pkl"

        with open(pkl_filename, 'rb') as file:
            self.pickle_model = pickle.load(file)
            
        with open(vct_filename, 'rb') as file:
            self.pickle_vectorizer = dill.load(file)

    def check(self, text):
        start_time = time.time()
        answer =  self.pickle_model.predict(
            self.pickle_vectorizer.transform(
                [text]
            )
        )

        return {
            "text": text,
            "answer": 'toxic' if answer[0] else 'neutral',
            "time": f'{time.time() - start_time}s'
        }


if __name__ == "__main__":
    api = API()
    print(api.check("ты пидор"))
