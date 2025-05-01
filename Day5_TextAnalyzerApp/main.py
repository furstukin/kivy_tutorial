import json
import certifi
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.network.urlrequest import UrlRequest

class Interface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def fetched(self, req_body, result):
        # print(result)
        polarity = result[0]
        if polarity < 0:
            self.ids.textResult.text = f"The statement was negative.\nPolarity {str(result[0])}\nSubjectivity {str(result[1])}"
        else:
            self.ids.textResult.text = f"The statement was positive.\nPolarity {str(result[0])}\nSubjectivity {str(result[1])}"

    def analyze(self):
        data = json.dumps({"sentence": self.ids.textInput.text})
        UrlRequest(url='https://kivy-vercel-api.vercel.app/analyze/', on_success=self.fetched, req_body=data, req_headers={"Content-Type": "application/json; charset=utf-8"}, ca_file=certifi.where(), verify=True)
        response = UrlRequest(url='https://kivy-vercel-api.vercel.app/analyze/', on_success=self.fetched, req_body=data, req_headers={"Content-Type": "application/json; charset=utf-8"}, ca_file=certifi.where(), verify=True)
        print(response)

    def clear(self):
        self.ids.textInput.text = ""
        self.ids.textResult.text = ""


class TextAnalyzerApp(App):
    pass

TextAnalyzerApp().run()