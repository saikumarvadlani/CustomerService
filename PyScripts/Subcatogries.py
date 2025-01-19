import openai

def suggest_subcategory(user_query, categories, key):
    openai.api_key = key
    """
    Suggest a single, precise subcategory for a user query using the ChatCompletion API.
    :param user_query: String, the user’s input.
    :param categories: categories to refine the subcategories.
    :return: A single suggested subcategory.
    """
    try:
        # Use ChatCompletion for GPT models this method is used to interact with the ChatGPT model 
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Version of GPT
            messages=[
                {"role": "system", "content": "You are a helpful assistant for customer support."},
                {"role": "user", "content": f"""
                I need help subcategorizing the following query using given categories. 
                Categories: "{categories}"
                User Query: "{user_query}"
                Given a user query, analyze both the query and categories to
                suggest the most relevant subcategory that is different
                from the given categories. Return the suggestion as exactly two words.
                If the query is invalid, return 'sorry, can't assign subcategory'.
                """}  # Promt is given such a way that it will return desired string if it is not valid
            ],
            max_tokens=100,
            temperature=0.7,
        )

        # Extract and return the assistant's message
        return response["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"Error: {str(e)}"
