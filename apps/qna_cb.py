from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai  import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

que = "who is pm of india"
result  = llm.invoke(que)

print(result.content)