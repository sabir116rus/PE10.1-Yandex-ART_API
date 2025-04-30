import dotenv
import os

dotenv.load_dotenv()

iam_token = os.getenv("iam_token")
catalog_id = os.getenv("catalog_id")

url_1 = "https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync"
url_2 = "https://llm.api.cloud.yandex.net:443/operations/"
