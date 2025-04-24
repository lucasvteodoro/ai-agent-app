from langchain_anthropic import ChatAnthropic



def create_llm():
    llm = ChatAnthropic(temperature=0.0, model='claude-3-5-sonnet-20241022')
    return llm




