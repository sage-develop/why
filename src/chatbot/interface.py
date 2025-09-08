def get_client_info_collection_interface() -> str:
    """
    Generate the client information collection interface.
    This includes a text input field for the user to type their client information.
    """
    return """
        **Client Information Collection**

        Before we begin the consultation, you can provide any existing information about this client to help speed up the process.

        **What information is helpful?**\n
        • Business type (importer, exporter, both)\n
        • Currency exposures and amounts\n
        • Hedging preferences and risk tolerance  \n
        • Interest rate risk concerns\n
        • Existing financial structures\n

        *Note: You can leave this blank and proceed with the normal consultation flow.*
    """
