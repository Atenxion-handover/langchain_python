from helpers import ingest_data, crawl
from langfuse.decorators import observe, langfuse_context


@observe(as_type="generation")
def ingest():

    documents = crawl(
        start_url="https://win066.wixsite.com/brillar-bank/",
        ignore_list=[
            "https://win066.wixsite.com/brillar-bank/brillar-bank-blog-1",
            "https://win066.wixsite.com/brillar-bank/brillar-bank-blog-2",
            "https://win066.wixsite.com/brillar-bank/brillar-bank-blog-3",
            "https://win066.wixsite.com/brillar-bank/brillar-bank-blog-4",
        ],
    )

    langfuse_context.update_current_observation(
        model="text-embedding-3-large-custom", input=documents
    )

    result = ingest_data(
        documents=documents,
        embedding_model="text-embedding-3-large",
        index_name="cost_test",
        vector_db="qdrant",
        dimension=256,
    )

    return result


print(ingest())
