# ZeroClaw Shopify Agent 🤖

An AI agent to automate Shopify and CJ dropshipping operations.

## Features

- Automatically sync products from CJ to Shopify
- Auto-process new Shopify orders and place orders on CJ
- Real-time order status and inventory monitoring
- Integrated AI intelligent decision-making (optional)

## Installation

1. Clone the repository:
git clone https://github.com/charlestempo/zeroclaw-shopify-agent.git
cd zeroclaw-shopify-agent

2. Install dependencies:
pip install -r requirements.txt

3. Configure config.py:
- Fill in your Shopify store URL, API key, and password
- Fill in your CJ Affiliate ID and Auth Token
- (Optional) Fill in your OpenAI API key to enable AI features

4. Run the agent:
python agent.py

## Project Structure

zeroclaw-shopify-agent/
├── agent.py          # Main agent program
├── shopify_api.py    # Shopify API wrapper
├── cj_api.py         # CJ API wrapper
├── config.py         # Configuration file
├── requirements.txt  # Dependency list
└── README.md         # Project documentation

## Notes

- Keep your API keys secure and do not commit config.py to public repositories
- Ensure your Shopify store and CJ account are properly configured before first run
- It is recommended to fully test in a staging environment before using in production
