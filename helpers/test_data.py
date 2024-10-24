def get_urls():
    urls = {
        "brillar_bank": [
            "https://win066.wixsite.com/brillar-bank/",
            "https://win066.wixsite.com/brillar-bank/fixed-deposit",
            "https://win066.wixsite.com/brillar-bank/e-fixed-deposit",
            "https://win066.wixsite.com/brillar-bank/flexi-fixed-deposit",
            "https://win066.wixsite.com/brillar-bank/senior-savers-flexi-fixed-deposit",
            "https://win066.wixsite.com/brillar-bank/junior-fixed-deposit",
            "https://win066.wixsite.com/brillar-bank/foreign-currency-fixed-deposit",
        ],
        "atom": [
            "https://www.atom.com.mm/en/personal/contact",
            "https://www.atom.com.mm/en/personal/simregistration",
            "https://www.atom.com.mm/en/personal/prepaid-sims",
            "https://www.atom.com.mm/en/personal/homeinternet",
            "https://homeinternet.atom.com.mm/ownership-intro",
            "https://www.atom.com.mm/en/personal/balance-transfer",
            "https://www.atom.com.mm/en/personal/volte",
            "https://www.atom.com.mm/en/personal/top-up-eng",
            "https://www.atom.com.mm/en/personal/kyo-thone",
            "https://www.atom.com.mm/en/personal/pay",
            "https://www.atom.com.mm/en/personal/term-of-use",
            "https://www.atom.com.mm/en/personal/flexiplan",
            "https://www.atom.com.mm/en/personal/YaungYin",
        ],
    }

    return urls


def get_questions():
    questions = {
        "brillar_bank": [
            "Tell me what is Brillar bank?",
            "How many types of fixed deposit does Brillar Bank provide?",
            "What are the interest rates for fixed deposit?",
            "What are the interest rates for e-fixed deposit?",
            "What are the interest rates for flexi-fixed deposit?",
            "What are the interest rates for junior fixed deposit?",
            "What is the difference between Fixed Deposit and eFixed Deposit?",
        ],
        "atom": [
            "What is Atom?",
            "Tell what ATOM is, where it is based, and the type of products it offers.",
            "Which products can be accessed as home internet from ATOM?",
            "Are there requirements for SIM registration?",
            "How many SIMs per ID can be registered?",
            "How much does it cost to register my SIM?",
            "I need to register 5 SIM cards for my family. Can I do that with my ID?",
            "I'm new to ATOM. How can I register for free?",
            "I need the Viber number for ATOM customer service.",
            "Why do I need to register my SIM cards?",
            "Do you have prepaid SIMs?",
            "Follow-up: How much is it?",
            "I am a foreigner. Can I buy a SIM card while I am in Myanmar?",
            "Which products can be accessed as home internet from ATOM?",
            "Can you explain the steps to change ownership of my device with ATOM?",
            "How do I transfer my ATOM balance to another ATOM number?",
            "Can you explain the balance transfer policy for ATOM prepaid users?",
            "Is there a fee for transferring balance?",
            "How can I transfer balance in the ATOM app?",
            "What is the daily transfer limit for ATOM prepaid users?",
            "How can I use VoLTE service with ATOM?",
            "Is Samsung S23 Ultra a VoLTE compatible handset model of ATOM?",
            "Follow-up: How about iPhone 14 Pro?",
            "I use an Android. If I want to use '4G VoLTE calling,' what steps do I need to take?",
            "Can I make a VoLTE video call on an iPhone?",
            "How many ways to recharge are available with ATOM?",
            "How many kinds of Recharge Coupon Vouchers can I get?",
            "How can I top up if a 1500ks coupon voucher is unavailable?",
            "Is it possible to re-register the same number if my SIM card is lost?",
            "What happens if my SIM card is not activated within 180 days?",
            "What if a top-up has not been made within 60 days?",
            "Can you guide me to bake a cake for ATOM's anniversary?",
            "What is ATOM Yaung Yin?",
            "How do I get started with ATOM Yaung Yin?",
            "Are there any discounts or special offers for new customers at ATOM Yaung Yin?",
            "Does the 2.5% discount apply only for the first top-up or for every balance load?",
        ],
        "langchain": [
            "How many methods can be used for building custom tool?",
            "What are the parameters for Chat Models?",
            "What are the differences between version 0.2 and 0.3?",
            "How do you get token usage in streaming?",
            "Tell me about the different retrieval approaches?",
            "How to write a custom retriever?",
            "How many types of document loaders do you offer?",
            "Indexing",
            "Does langchain support openai integration?",
            "How to invoke multimodal requests?",
        ],
    }

    return questions


__all__ = ["get_urls", "get_questions"]
