styles = """
<style>

/* Limit width */
.block-container {
    max-width: 650px;
}

/* USER MESSAGE: reverse layout */
div[data-testid="stChatMessage"]:has(
    div[data-testid="stChatMessageAvatarUser"]
) {
    flex-direction: row-reverse !important;
}

/* USER avatar spacing */
div[data-testid="stChatMessageAvatarUser"] {
    margin-left: 10px;
    margin-right: 0px;
}

/* USER bubble styling */
div[data-testid="stChatMessageContent"][aria-label="Chat message from user"] {
    background: linear-gradient(135deg, #4da6ff, #00c6ff);
    color: white;
    border-radius: 20px 20px 5px 20px;
    padding: 12px 16px;
    margin-left: 50px;
}

/* ASSISTANT bubble styling */
div[data-testid="stChatMessageContent"][aria-label="Chat message from assistant"] {
    background-color: white;
    border: 2px solid #4da6ff;
    border-radius: 20px 20px 20px 5px;
    padding: 12px 16px;
    margin-right: 50px;
}

</style>
"""