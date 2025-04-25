from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Endpoint
endpoint = "https://aiservicesai900.cognitiveservices.azure.com/"
key = "2nDOsJoeWNZscliGmRVpC88rpvMsF3wF5KjGqcrSUqmjAX1N6zrlJQQJ99AKACYeBjFXJ3w3AAAAACOGr0oi"

# Long input text
document = """
Washington, D.C., formally the District of Columbia and commonly known as Washington or D.C., is the capital city and federal district of the United States. The city is on the Potomac River, across from Virginia, and shares land borders with Maryland to its north and east. It was named after George Washington, the first president of the United States. The district is named for Columbia, the female personification of the nation.

The U.S. Constitution in 1789 called for the creation of a federal district under exclusive jurisdiction of the U.S. Congress. As such, Washington, D.C., is not part of any state, and is not one itself. The Residence Act, adopted on July 16, 1790, approved the creation of the capital district along the Potomac River. The city was founded in 1791, and the 6th Congress held the first session in the unfinished Capitol Building in 1800 after the capital moved from Philadelphia. In 1801, the District of Columbia, formerly part of Maryland and Virginia and including the existing settlements of Georgetown and Alexandria, was officially recognized as the federal district; initially, the city was a separate settlement within the larger district. In 1846, Congress reduced the size of the district when it returned the land originally ceded by Virginia, including the city of Alexandria. In 1871, it created a single municipality for the district. There have been several unsuccessful efforts to make the district into a state since the 1880s; a statehood bill passed the House of Representatives in 2021 but was not adopted by the U.S. Senate. To become law, it would have to be passed by the Senate and signed by the president; it would have renamed the city Washington, Douglass Commonwealth and shrunk the Federal District to about the size of the National Mall.

Designed in 1791 by Pierre Charles L'Enfant, the city is divided into quadrants, which are centered on the Capitol Building and include 131 neighborhoods. As of the 2020 census, the city had a population of 689,545.[3] Commuters from the city's Maryland and Virginia suburbs raise the city's daytime population to more than one million during the workweek.[12] The Washington metropolitan area, which includes parts of Maryland, Virginia, and West Virginia, is the country's seventh-largest metropolitan area, with a 2023 population of 6.3 million residents.[6] A locally elected mayor and 13-member council have governed the district since 1973, though Congress retains the power to overturn local laws. Washington, D.C., residents do not have voting representation in Congress, but elect a single non-voting congressional delegate to the U.S. House of Representatives. The city's voters choose three presidential electors in accordance with the Twenty-third Amendment, passed in 1961.

Washington, D.C., anchors the southern end of the Northeast megalopolis. As the seat of the U.S. federal government, the city is an important world political capital.[13] The city hosts buildings that house federal government headquarters, including the White House, U.S. Capitol, Supreme Court Building, and multiple federal departments and agencies. The city is home to many national monuments and museums, located most prominently on or around the National Mall, including the Jefferson Memorial, Lincoln Memorial, and Washington Monument. It hosts 177 foreign embassies and the global headquarters of the World Bank, International Monetary Fund, Organization of American States, and other international organizations. Home to many of the nation's largest industry associations, non-profit organizations, and think tanks, the city is known as a lobbying hub, which is centered on and around K Street.[14] It is also among the country's top tourist destinations; in 2022, it drew an estimated 20.7 million domestic[15] and 1.2 million international visitors, seventh-most among U.S. cities.[16]
"""

# Authenticate
credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

# Summarization is an asynchronous API
poller = client.begin_abstract_summary(
    documents=[document],
    sentence_count=3  # Optional: how many summary sentences you want
)

# Get the result
result = poller.result()

# Show summary
for doc in result:
    if not doc.is_error:
        print("\n\nSummary:")
        for sentence in doc.summaries:
            print(f"- {sentence.text}")
    else:
        print(f"Error: {doc.error}")
