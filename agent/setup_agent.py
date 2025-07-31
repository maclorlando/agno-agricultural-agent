from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
#from agno.knowledge.file import FileKnowledge
from agno.vectordb.lancedb import LanceDb
from agno.embedder.openai import OpenAIEmbedder

memory = Memory(
    model=OpenAIChat(id="gpt-4", request_params={"max_tokens": 2048}),
    db=SqliteMemoryDb(table_name="farm_memories", db_file="data/farm_memory.db"),
)

# knowledge = FileKnowledge(
#     paths=["docs/embrapa", "docs/books", "docs/transcripts"],
#     vector_db=LanceDb(
#         uri="data/lancedb",
#         table_name="farm_docs",
#         embedder=OpenAIEmbedder(id="text-embedding-3-small", dimensions=1536),
#     ),
# )

agent = Agent(
    name="Farm Assistant",
    model=OpenAIChat(id="gpt-4"),
    memory=memory,
    #knowledge=knowledge,
    instructions=[
        "Forneça respostas práticas e técnicas para operações de pecuária e agricultura no Brasil.",
        "Responda sempre em português, exceto se solicitado o contrário.",
        "Use sua base de conhecimento e memória antes de responder.",
    ],
    enable_agentic_memory=True,
    markdown=True,
    debug_mode=True,
    monitoring=True,
)
