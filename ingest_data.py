from helpers import ingest_data, crawl
from langchain_core.documents import Document


def ingest():

    # documents = crawl(
    #     start_url="https://win066.wixsite.com/brillar-bank/",
    #     ignore_list=[
    #         "https://win066.wixsite.com/brillar-bank/brillar-bank-blog-1",
    #         "https://win066.wixsite.com/brillar-bank/brillar-bank-blog-2",
    #         "https://win066.wixsite.com/brillar-bank/brillar-bank-blog-3",
    #         "https://win066.wixsite.com/brillar-bank/brillar-bank-blog-4",
    #     ],
    # )

    documents = [
        Document(
            page_content="Savings and Personal Current Account) : Below RM100,000 • Combination of Deposit\n"
            + "Accounts & Unit Trust (based on outstanding balance) : Below RM300,000 ATM\n"
            + "Related Click for more details Debit Card Related Click for more details Junior\n"
            + "Savings Account Related Over the counter withdrawal: • 1st withdrawal over-the-\n"
            + "counter per month • 2nd or subsequent withdrawals over-the-counter per month No\n"
            + "charge RM2.00 per withdrawal Basic Savings Account Related Over-the-counter\n"
            + "(OTC) Visits (per month): No charge",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank _ Junior Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="• First 6 OTC visits • From the 7th OTC onwards Waived until further notice\n"
            + "Others • CDS account opening (only applicable for Pay&Save Account) RM10.00\n"
            + "Fixed Deposit Account Fees & Charges Description Fees / Charges (subject to\n"
            + "Government Tax, if applicable) Cheque Related Dishonoured Inward Return Cheques\n"
            + "due to: • Post-dated reason only RM10.00 per cheque Changes to Account Related:\n"
            + "• Change to operating mandate",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank _ Junior Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="• Addition of joint accountholders RM10.00 per account RM10.00 per account (No\n"
            + "charge for Priority Banking customers) Service Charge Related Applicable for\n"
            + "Priority Banking customers only Average balance of the Deposit Accounts fall\n"
            + "below the minimum amount for 3 consecutive months: • Deposit Accounts (Personal\n"
            + "Fixed Deposit, Personal Savings and Personal Current Account) : Below RM100,000\n"
            + "• Combination of Deposit Accounts & Unit Trust (based on outstanding balance) :\n"
            + "Below RM200,000 RM50.00 (No charge for Priority Banking customers with Mortgage\n"
            + "Loan that is Personal Brillar Housing Loan or Shop Loan only) Others Replacement\n"
            + "of lost Fixed Deposit Receipt RM5.00 per receipt and RM10.00 for Letter of\n"
            + "Indemnity stamp duty",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank _ Junior Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Withdrawal by Banker’s Cheque RM5.00 per cheque. RM0.15 per cheque for stamp\n"
            + "duty. Cheque processing fee of RM0.50 Foreign Currency Current Account Fees &\n"
            + "Charges Description Fees / Charges (subject to Government Tax, if applicable)\n"
            + "Transaction Fee RM10.00 or its equivalent (Charges are waived for all new and\n"
            + "active Dual Currency Investments (DCI) customers) Service Charge RM30.00 or its\n"
            + "equivalent every half year ( June & December) (Charges are waived for all new\n"
            + "and active Dual Currency Investments (DCI) customers and Foreign Currency Bond\n"
            + "customers)",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank _ Junior Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="• Fixed Deposit Account > • Fixed Deposit Fixed Deposit Features and benefits\n"
            + "savings. Brillar Bank Fixed Deposit account is a good start for your long-term\n"
            + "savings plan. Long Term A choice of terms from 1 - 60 months. Interest Payout\n"
            + "Receive interest at maturity. Flexibility of early fixed deposit partial\n"
            + "withdrawal without losing interest on remaining balance Partial withdrawal is in\n"
            + "multiples of RM1,000. Outstanding balances will be shown on the monthly e-\n"
            + "statement. Effective 1 January 2019, no interest shall be payable on partially\n"
            + "withdrawn amounts and premature withdrawals of FD. Convenient Withdrawal You can\n"
            + "withdraw from any branch nationwide. Eligibility • Minimum deposit of RM5,000\n"
            + "for 1 month placement and RM500 for 2 months and above.",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="• Applicable for individual and non-individual customers. • For Malaysian aged\n"
            + "18 years old & above. • For Malaysian aged below 18 years old, account must be\n"
            + "opened as a trust account. Terms and Conditions apply. Member of PIDM. Protected\n"
            + "by PIDM up to RM250,000 for each depositor. Interest rates Tenure Interest Rates\n"
            + "(p.a.) 1 month 2.15% 2 months 2.25% 3 months 2.25% 4 months 2.30% 5 months 2.30%\n"
            + "6 months 2.30%",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="7 months 2.35% 8 months 2.35% 9 months 2.35% 10 months 2.35% 11 months 2.35% 12\n"
            + "months 2.35% 13 – 60 months 2.35% Fee and charges Current Account",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Fees & Charges Description Fees / Charges (subject to Government Tax, if\n"
            + "applicable) Cheque Related Issuance of cheque book Stamp duty of RM0.15 per\n"
            + "cheque 3rd and subsequent cheque books in a calendar month RM10.00 per cheque\n"
            + "book and RM0.15 per cheque leaf Cheque Processing Fee RM0.50 per issuance\n"
            + "Dishonoured Outward Return Cheques due to: • Insufficient funds (e.g. refer to\n"
            + "drawer, effects not cleared, not arranged for, & exceeded arrangement) •\n"
            + "Technical Error (e.g. alterations) RM150.00 per cheque RM10.00 per cheque\n"
            + "Dishonoured Inward Return Cheques due to: • Post-dated reason only RM10.00 per\n"
            + "cheque (imposed on payee)",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Postage charges for Return Cheques RM5.00 Stop Payment upon request: • On cheque\n"
            + "issued • Due to loss/ stolen cheques/ cheque book RM10.00 per cheque RM10.00 per\n"
            + "instruction Stop Payment upon presentation of stop payment cheque: • If\n"
            + "sufficient funds • If insufficient funds RM10.00 per cheque RM150.00 per cheque\n"
            + "Cheque encashment at domicile branch: • 1st party (by accountholder) encashment\n"
            + "• 3rd party encashment No charge RM2.00 per encashment (No charge for company\n"
            + "representative/s encashing cheques on behalf of the company) Cheque encashment\n"
            + "at non-domicile branch: • 1st party (by accountholder) encashment • 3rd party\n"
            + "encashment • Cheque amount RM5,000.00 and below No charge RM5.00 on payee and\n"
            + "RM2.00 on drawer RM7.00 on payee and RM2.00 on drawer",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="• Cheque amount above RM5,000.00 Destruction of uncollected Cheque Book (more\n"
            + "than 28 days): • Individual Account • Business Account RM30.00 per cheque book\n"
            + "RM50.00 per cheque book Others: • Printing special cheques • Handling Charges on\n"
            + "Representing Cheques • Redesignation of Special Account for bad cheque offenders\n"
            + "RM50.00 per printing RM50.00 per cheque RM50.00 Statement Related Statement\n"
            + "Request: • Weekly • Ad Hoc • For statement up to one year ago • For statement of\n"
            + "more than a year ago Hold Mail Request RM20.00 per month RM10.00 per request and\n"
            + "RM2.00 per page RM10.00 per request and RM5.00 per page",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="RM20.00 per month per mail (No charge for Priority and Private Banking\n"
            + "customers) Dormant Account Related Basic Current Account (No activity for 12\n"
            + "months and above): • Balance RM10.00 and below • Balance more than RM10.00\n"
            + "Dormant Current Account (No activity for 12 months and above): • Balance RM10.00\n"
            + "and below • Balance more than RM10.00 Account closed and balance absorbed as\n"
            + "charge RM10.00 yearly Account closed and balance absorbed as charge RM10.00\n"
            + "yearly Close Account Related Basic Current Account Other Current Account RM20.00\n"
            + "(within 3 months from opening) RM20.00 (within 6 months from opening)",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Account Related • Change of operating mandate • Addition of joint accountholders\n"
            + "• Mandate for operating account RM10.00 per account RM10.00 per account Service\n"
            + "Charge RM10.00 per mandate and stamp duty RM10.00 per mandate SMS Notification\n"
            + "Related • Applicable for Brillar Bank One Account only • Applicable for all\n"
            + "account RM0.50 per SMS (no charge for first 20 SMS alerts per calendar month)\n"
            + "RM5.00 monthly for Individual account RM10.00 monthly for Non-Individual account\n"
            + "ATM Related Click for more details Debit Card Related Click for more details\n"
            + "Service Charge Related • Where average balance for half year is below RM1,000.00\n"
            + "(other than Smartlink / Flexi One/ Top Yield/ One Account) RM10.00 every half\n"
            + "year (June & December)",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="• Brillar Bank Smartlink Account where average balance for half year is below\n"
            + "RM200.00; • Brillar Bank One Account, Top Yield Account and Flexi One Account\n"
            + "where average monthly balance is below RM1,000.00; • Where average balance of\n"
            + "all the Deposit Accounts of a Priority Banking Customer fall below the minimum\n"
            + "amount for 3 consecutive months. • Deposit Accounts (Personal Fixed Deposit,\n"
            + "Personal Savings and Personal Current Account) : Below RM100,000 • Combination\n"
            + "of Deposit Accounts & Unit Trust (based on outstanding balance) : Below\n"
            + "RM200,000 RM5.00 every half year (June & December) RM5.00 per month RM50.00 (No\n"
            + "charge for Priority Banking customers with Mortgage Loan that is Personal\n"
            + "Brillar Bank Housing Loan or Shop Loan only) Brillar Bank SmartLink Account\n"
            + "Related",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="• Cash withdrawal without cheque, or • Cheque encashment performed by 1st party\n"
            + "at domicile or interbranch RM5.00 per transaction Brillar Bank One Account\n"
            + "Overdraft (OD) Facility Fee Related • Prescribed Rate (Interest payable on\n"
            + "utilisation of OD) • Excess Rate (Interest payable on overdrawn OD limit) •\n"
            + "Commitment Fee (Interest payable on unutilised OD in excess of RM250,000.00) 1%\n"
            + "p.a. above BLR on daily rest on the utilised OD amount 4% p.a. above BLR on\n"
            + "daily rest on the amount drawn in excess of the approved OD limit 1% p.a. on\n"
            + "daily rest on the unutilised OD amount. BizOne Overdraft Facility (BizOne OD)\n"
            + "Related",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="• Prescribed Rate (Interest payable on utilisation of OD) • Excess Rate\n"
            + "(Interest payable on overdrawn OD limit) • Commitment Fee (Interest payable on\n"
            + "unutilised OD in excess of RM250,000.00) • Stamp Duties • Disbursement Fees 1%\n"
            + "p.a. above 1-month BizOne FD’s prevailing board rate on daily rest on the\n"
            + "utilized OD amount. 4% p.a. above BLR on daily rest on the amount drawn in\n"
            + "excess of the approved OD limit 1% p.a. on daily rest on the unutilised OD\n"
            + "amount. As per the Stamp Duty Act 1949 (Revised 1989) Ad Valorem (0.5% on\n"
            + "approved OD amount) Disbursement Fees including but not limited to registration\n"
            + "fees (e.g. for Form 34 to be filed with the Companies Commission of Malaysia for\n"
            + "companies), and any tax or levy as per the scale fees charged by the respective\n"
            + "authorities.",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="• Legal Fees Legal fees will be incurred in relation to the stamping and\n"
            + "registration of relevant loan/security documentation. Mortgage Overdraft (OD)\n"
            + "Facility Fee Related • Excess Rate (Interest payable on Overdrawn limit) •\n"
            + "Commitment Fee (Interest payable on unutilised OD in excess of RM250,000.00) 4%\n"
            + "p.a. above BLR on daily rest on the amount drawn in excess of the approved OD\n"
            + "limit; or 6.8% p.a. above BR on daily rest on the amount drawn in excess of the\n"
            + "approved OD limit 1% p.a. on daily rest on the unutilised OD amount. Brillar\n"
            + "Bank MyPAL Related • Convenience Fee • Late Payment Fee RM15.00 per usage RM1.00\n"
            + "every 3 days, up to a maximum of RM9.00 Basic Current Account Related",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Over-the-counter (OTC) Visits (per month): • First 6 OTC visits • From the 7th\n"
            + "OTC onwards No charge Waived until further notice Others • Sweeping from Brillar\n"
            + "Bank Flexi Fixed Deposit to Brillar Bank Flexi One account RM5.00 for every\n"
            + "RM3,000.00 swept Savings Account Fees & Charges Description Fees / Charges\n"
            + "(subject to Government Tax, if applicable) Cheque Related Dishonoured Inward\n"
            + "Return Cheques due to: • Post-dated reason only RM10.00 (No charge for Priority\n"
            + "and Private Banking customers) Passbook Related",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Lost Savings Passbook: • Only applicable for Harvest Savings Account and Senior\n"
            + "Savers Account RM10.00 per passbook and RM10.00 for Letter of Indemnity stamp\n"
            + "duty Close Account Related Basic Savings Account Other Savings Account RM20.00\n"
            + "(within 3 months from opening) RM20.00 (within 6 months from opening) Dormant\n"
            + "Account Related Basic Savings Account (no activity 12 months and above): •\n"
            + "Balance RM10.00 and below • Balance more than RM10.00 Other Savings Account (no\n"
            + "activity 12 months and above): • Balance RM10.00 and below • Balance more than\n"
            + "RM10.00 Account closed and balance absorbed as charge RM10.00 yearly Account\n"
            + "closed and balance absorbed as charge RM10.00 yearly",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Changes to Account Related: • Change to operating mandate • Addition of joint\n"
            + "accountholders RM10.00 per account RM10.00 per account (No charge for Priority\n"
            + "and Private Banking customers) SMS Notification Related: • Individual account •\n"
            + "Non-individual account RM5.00 monthly RM10.00 monthly Service Charge Related\n"
            + "Applicable for Pay&Save Account only • Brillar Bank Pay&Save Account where\n"
            + "average balance for half year is below RM200.00; Applicable for Priority Banking\n"
            + "customers only Average balance of the Deposit Accounts fall below the minimum\n"
            + "amount for 3 consecutive months: • Deposit Accounts (Personal Fixed Deposit,\n"
            + "Personal RM5.00 every half year (June & December) RM50.00 (No charge for\n"
            + "Priority Banking customers with Mortgage Loan that is Personal Brillar Bank\n"
            + "Housing Loan or Shop Loan only)",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Savings and Personal Current Account) : Below RM100,000 • Combination of Deposit\n"
            + "Accounts & Unit Trust (based on outstanding balance) : Below RM300,000 ATM\n"
            + "Related Click for more details Debit Card Related Click for more details Junior\n"
            + "Savings Account Related Over the counter withdrawal: • 1st withdrawal over-the-\n"
            + "counter per month • 2nd or subsequent withdrawals over-the-counter per month No\n"
            + "charge RM2.00 per withdrawal Basic Savings Account Related Over-the-counter\n"
            + "(OTC) Visits (per month): No charge",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="• First 6 OTC visits • From the 7th OTC onwards Waived until further notice\n"
            + "Others • CDS account opening (only applicable for Pay&Save Account) RM10.00\n"
            + "Fixed Deposit Account Fees & Charges Description Fees / Charges (subject to\n"
            + "Government Tax, if applicable) Cheque Related Dishonoured Inward Return Cheques\n"
            + "due to: • Post-dated reason only RM10.00 per cheque Changes to Account Related:\n"
            + "• Change to operating mandate",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="• Addition of joint accountholders RM10.00 per account RM10.00 per account (No\n"
            + "charge for Priority Banking customers) Service Charge Related Applicable for\n"
            + "Priority Banking customers only Average balance of the Deposit Accounts fall\n"
            + "below the minimum amount for 3 consecutive months: • Deposit Accounts (Personal\n"
            + "Fixed Deposit, Personal Savings and Personal Current Account) : Below RM100,000\n"
            + "• Combination of Deposit Accounts & Unit Trust (based on outstanding balance) :\n"
            + "Below RM200,000 RM50.00 (No charge for Priority Banking customers with Mortgage\n"
            + "Loan that is Personal Brillar Housing Loan or Shop Loan only) Others Replacement\n"
            + "of lost Fixed Deposit Receipt RM5.00 per receipt and RM10.00 for Letter of\n"
            + "Indemnity stamp duty",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Withdrawal by Banker’s Cheque RM5.00 per cheque. RM0.15 per cheque for stamp\n"
            + "duty. Cheque processing fee of RM0.50 Foreign Currency Current Account Fees &\n"
            + "Charges Description Fees / Charges (subject to Government Tax, if applicable)\n"
            + "Transaction Fee RM10.00 or its equivalent (Charges are waived for all new and\n"
            + "active Dual Currency Investments (DCI) customers) Service Charge RM30.00 or its\n"
            + "equivalent every half year ( June & December) (Charges are waived for all new\n"
            + "and active Dual Currency Investments (DCI) customers and Foreign Currency Bond\n"
            + "customers)",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Flexi Fixed Deposit A truly flexible fixed deposit account Brillar Flexi Fixed\n"
            + "Deposit rewards you with attractive interest and auto-sweep facility from Flexi\n"
            + "Fixed Deposit to Flexi One Account or vice versa. Earn attractive FD interest\n"
            + "for 12-month tenure When your Flexi One Account exceeds RM30,000, it will be\n"
            + "transferred to your Flexi FD Account to earn attractive FD interest. (Transfers\n"
            + "are automatic and done once a month in the multiples of RM30,000). Effective 1\n"
            + "January 2019, no interest shall be payable on partially withdrawn amounts and\n"
            + "premature withdrawals of FD. Interest Payout Receive interest at maturity.\n"
            + "Eligibility • For individuals, either single or in joint names. • The individual\n"
            + "must have attained the age of 18 at the point of opening the account •\n"
            + "Non-residents may open the Flexi FD and Flexi One Account. • The minimum initial\n"
            + "deposit is RM10,000 for opening the Flexi FD Account. • The minimum initial\n"
            + "deposit is RM10 for opening the Flexi One Account.",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Flexi Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Make an early partial withdrawal and still earn an attractive FD interest on\n"
            + "your remaining balance Make an early partial withdrawal anytime and continue to\n"
            + "earn an attractive FD interest on your remaining balance. (Partial withdrawal is\n"
            + "in multiples of RM3,000. No Overdraft Facility is given Terms and Conditions\n"
            + "apply. Member of PIDM. Protected by PIDM up to RM250,000 for each depositor.\n"
            + "Other flexible feature • Comes with a Flexi One Account so you can have the\n"
            + "convenience of chequing and savings at high interest rates. • Auto-sweeping from\n"
            + "Flexi FD to Flexi One Account when there are insufficient funds in your Flexi\n"
            + "One Account for in-clearing cheques and standing instruction payments.\n"
            + "(Auto-sweep is in multiples of RM3,000. A service charge of RM5 is imposed for\n"
            + "each auto-sweep) • Flexibility to make withdrawals at any branch nationwide. •\n"
            + "Consolidated monthly statements. No FD receipt issued. • Access via ATM,\n"
            + "Internet Banking and Phone Banking Interest rates Tenure Interest Rate (p.a.) 12\n"
            + "months 2.50%",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Flexi Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Fee and charges Current Account Fees & Charges Description Fees / Charges\n"
            + "(subject to Government Tax, if applicable) Cheque Related Issuance of cheque\n"
            + "book Stamp duty of RM0.15 per cheque 3rd and subsequent cheque books in a\n"
            + "calendar month RM10.00 per cheque book and RM0.15 per cheque leaf Cheque\n"
            + "Processing Fee RM0.50 per issuance Dishonoured Outward Return Cheques due to: •\n"
            + "Insufficient funds (e.g. refer to drawer, effects not cleared, not arranged for,\n"
            + "& exceeded arrangement) • Technical Error (e.g. alterations) RM150.00 per cheque\n"
            + "RM10.00 per cheque",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Flexi Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Dishonoured Inward Return Cheques due to: • Post-dated reason only RM10.00 per\n"
            + "cheque (imposed on payee) Postage charges for Return Cheques RM5.00 Stop Payment\n"
            + "upon request: • On cheque issued • Due to loss/ stolen cheques/ cheque book\n"
            + "RM10.00 per cheque RM10.00 per instruction Stop Payment upon presentation of\n"
            + "stop payment cheque: • If sufficient funds • If insufficient funds RM10.00 per\n"
            + "cheque RM150.00 per cheque Cheque encashment at domicile branch: • 1st party (by\n"
            + "accountholder) encashment • 3rd party encashment No charge RM2.00 per encashment\n"
            + "(No charge for company representative/s encashing cheques on behalf of the\n"
            + "company) Cheque encashment at non-domicile branch: No charge",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Flexi Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="• 1st party (by accountholder) encashment • 3rd party encashment • Cheque amount\n"
            + "RM5,000.00 and below • Cheque amount above RM5,000.00 RM5.00 on payee and RM2.00\n"
            + "on drawer RM7.00 on payee and RM2.00 on drawer Destruction of uncollected Cheque\n"
            + "Book (more than 28 days): • Individual Account • Business Account RM30.00 per\n"
            + "cheque book RM50.00 per cheque book Others: • Printing special cheques •\n"
            + "Handling Charges on Representing Cheques • Redesignation of Special Account for\n"
            + "bad cheque offenders RM50.00 per printing RM50.00 per cheque RM50.00 Statement\n"
            + "Related Statement Request: • Weekly • Ad Hoc • For statement up to one year ago\n"
            + "RM20.00 per month",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Flexi Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="• For statement of more than a year ago Hold Mail Request RM10.00 per request\n"
            + "and RM2.00 per page RM10.00 per request and RM5.00 per page RM20.00 per month\n"
            + "per mail (No charge for Priority and Private Banking customers) Dormant Account\n"
            + "Related Basic Current Account (No activity for 12 months and above): • Balance\n"
            + "RM10.00 and below • Balance more than RM10.00 Dormant Current Account (No\n"
            + "activity for 12 months and above): • Balance RM10.00 and below • Balance more\n"
            + "than RM10.00 Account closed and balance absorbed as charge RM10.00 yearly\n"
            + "Account closed and balance absorbed as charge RM10.00 yearly Close Account\n"
            + "Related",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Flexi Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Basic Current Account Other Current Account RM20.00 (within 3 months from\n"
            + "opening) RM20.00 (within 6 months from opening) Account Related • Change of\n"
            + "operating mandate • Addition of joint accountholders • Mandate for operating\n"
            + "account RM10.00 per account RM10.00 per account Service Charge RM10.00 per\n"
            + "mandate and stamp duty RM10.00 per mandate SMS Notification Related • Applicable\n"
            + "for Brillar Bank One Account only • Applicable for all account RM0.50 per SMS\n"
            + "(no charge for first 20 SMS alerts per calendar month) RM5.00 monthly for\n"
            + "Individual account RM10.00 monthly for Non-Individual account ATM Related Click\n"
            + "for more details Debit Card Related Click for more details Service Charge\n"
            + "Related",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Flexi Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="• Where average balance for half year is below RM1,000.00 (other than Smartlink\n"
            + "/ Flexi One/ Top Yield/ One Account) • Brillar Bank Smartlink Account where\n"
            + "average balance for half year is below RM200.00; • Brillar Bank One Account, Top\n"
            + "Yield Account and Flexi One Account where average monthly balance is below\n"
            + "RM1,000.00; • Where average balance of all the Deposit Accounts of a Priority\n"
            + "Banking Customer fall below the minimum amount for 3 consecutive months. •\n"
            + "Deposit Accounts (Personal Fixed Deposit, Personal Savings and Personal Current\n"
            + "Account) : Below RM100,000 • Combination of Deposit Accounts & Unit Trust\n"
            + "RM10.00 every half year (June & December) RM5.00 every half year (June &\n"
            + "December) RM5.00 per month RM50.00 (No charge for Priority Banking customers\n"
            + "with Mortgage Loan that is Personal Brillar Bank Housing Loan or Shop Loan only)",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Flexi Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="(based on outstanding balance) : Below RM200,000 Brillar Bank SmartLink Account\n"
            + "Related • Cash withdrawal without cheque, or • Cheque encashment performed by\n"
            + "1st party at domicile or interbranch RM5.00 per transaction Brillar Bank One\n"
            + "Account Overdraft (OD) Facility Fee Related • Prescribed Rate (Interest payable\n"
            + "on utilisation of OD) • Excess Rate (Interest payable on overdrawn OD limit) •\n"
            + "Commitment Fee 1% p.a. above BLR on daily rest on the utilised OD amount 4% p.a.\n"
            + "above BLR on daily rest on the amount drawn in excess of the approved OD limit\n"
            + "1% p.a. on daily rest on the unutilised OD amount.",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Flexi Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="(Interest payable on unutilised OD in excess of RM250,000.00) BizOne Overdraft\n"
            + "Facility (BizOne OD) Related • Prescribed Rate (Interest payable on utilisation\n"
            + "of OD) • Excess Rate (Interest payable on overdrawn OD limit) • Commitment Fee\n"
            + "(Interest payable on unutilised OD in excess of RM250,000.00) • Stamp Duties 1%\n"
            + "p.a. above 1-month BizOne FD’s prevailing board rate on daily rest on the\n"
            + "utilized OD amount. 4% p.a. above BLR on daily rest on the amount drawn in\n"
            + "excess of the approved OD limit 1% p.a. on daily rest on the unutilised OD\n"
            + "amount. As per the Stamp Duty Act 1949 (Revised 1989) Ad Valorem (0.5% on\n"
            + "approved OD amount)",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Flexi Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="• Disbursement Fees • Legal Fees Disbursement Fees including but not limited to\n"
            + "registration fees (e.g. for Form 34 to be filed with the Companies Commission of\n"
            + "Malaysia for companies), and any tax or levy as per the scale fees charged by\n"
            + "the respective authorities. Legal fees will be incurred in relation to the\n"
            + "stamping and registration of relevant loan/security documentation. Mortgage\n"
            + "Overdraft (OD) Facility Fee Related • Excess Rate (Interest payable on Overdrawn\n"
            + "limit) • Commitment Fee (Interest payable on unutilised OD in excess of\n"
            + "RM250,000.00) 4% p.a. above BLR on daily rest on the amount drawn in excess of\n"
            + "the approved OD limit; or 6.8% p.a. above BR on daily rest on the amount drawn\n"
            + "in excess of the approved OD limit 1% p.a. on daily rest on the unutilised OD\n"
            + "amount. Brillar Bank MyPAL Related • Convenience Fee",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Flexi Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="• Late Payment Fee RM15.00 per usage RM1.00 every 3 days, up to a maximum of\n"
            + "RM9.00 Basic Current Account Related Over-the-counter (OTC) Visits (per month):\n"
            + "• First 6 OTC visits • From the 7th OTC onwards No charge Waived until further\n"
            + "notice Others • Sweeping from Brillar Bank Flexi Fixed Deposit to Brillar Bank\n"
            + "Flexi One account RM5.00 for every RM3,000.00 swept Savings Account Fees &\n"
            + "Charges Description Fees / Charges (subject to Government Tax, if applicable)\n"
            + "Cheque Related",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Flexi Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Dishonoured Inward Return Cheques due to: • Post-dated reason only RM10.00 (No\n"
            + "charge for Priority and Private Banking customers) Passbook Related Lost Savings\n"
            + "Passbook: • Only applicable for Harvest Savings Account and Senior Savers\n"
            + "Account RM10.00 per passbook and RM10.00 for Letter of Indemnity stamp duty\n"
            + "Close Account Related Basic Savings Account Other Savings Account RM20.00\n"
            + "(within 3 months from opening) RM20.00 (within 6 months from opening) Dormant\n"
            + "Account Related Basic Savings Account (no activity 12 months and above): •\n"
            + "Balance RM10.00 and below • Balance more than RM10.00 Account closed and balance\n"
            + "absorbed as charge RM10.00 yearly",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Flexi Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Other Savings Account (no activity 12 months and above): • Balance RM10.00 and\n"
            + "below • Balance more than RM10.00 Account closed and balance absorbed as charge\n"
            + "RM10.00 yearly Changes to Account Related: • Change to operating mandate •\n"
            + "Addition of joint accountholders RM10.00 per account RM10.00 per account (No\n"
            + "charge for Priority and Private Banking customers) SMS Notification Related: •\n"
            + "Individual account • Non-individual account RM5.00 monthly RM10.00 monthly\n"
            + "Service Charge Related Applicable for Pay&Save Account only • Brillar Bank\n"
            + "Pay&Save Account where average balance for half year is below RM200.00; RM5.00\n"
            + "every half year (June & December)",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Flexi Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Applicable for Priority Banking customers only Average balance of the Deposit\n"
            + "Accounts fall below the minimum amount for 3 consecutive months: • Deposit\n"
            + "Accounts (Personal Fixed Deposit, Personal Savings and Personal Current Account)\n"
            + ": Below RM100,000 • Combination of Deposit Accounts & Unit Trust (based on\n"
            + "outstanding balance) : Below RM300,000 RM50.00 (No charge for Priority Banking\n"
            + "customers with Mortgage Loan that is Personal Brillar Bank Housing Loan or Shop\n"
            + "Loan only) ATM Related Click for more details Debit Card Related Click for more\n"
            + "details Junior Savings Account Related Over the counter withdrawal: • 1st\n"
            + "withdrawal over-the- counter per month No charge RM2.00 per withdrawal",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Flexi Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="• 2nd or subsequent withdrawals over-the-counter per month Basic Savings Account\n"
            + "Related Over-the-counter (OTC) Visits (per month): • First 6 OTC visits • From\n"
            + "the 7th OTC onwards No charge Waived until further notice Others • CDS account\n"
            + "opening (only applicable for Pay&Save Account) RM10.00 Fixed Deposit Account\n"
            + "Fees & Charges Description Fees / Charges (subject to Government Tax, if\n"
            + "applicable) Cheque Related",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Flexi Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Dishonoured Inward Return Cheques due to: • Post-dated reason only RM10.00 per\n"
            + "cheque Changes to Account Related: • Change to operating mandate • Addition of\n"
            + "joint accountholders RM10.00 per account RM10.00 per account (No charge for\n"
            + "Priority Banking customers) Service Charge Related Applicable for Priority\n"
            + "Banking customers only Average balance of the Deposit Accounts fall below the\n"
            + "minimum amount for 3 consecutive months: • Deposit Accounts (Personal Fixed\n"
            + "Deposit, Personal Savings and Personal Current Account) : Below RM100,000 •\n"
            + "Combination of Deposit Accounts & Unit Trust (based RM50.00 (No charge for\n"
            + "Priority Banking customers with Mortgage Loan that is Personal Brillar Housing\n"
            + "Loan or Shop Loan only)",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Flexi Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="on outstanding balance) : Below RM200,000 Others Replacement of lost Fixed\n"
            + "Deposit Receipt Withdrawal by Banker’s Cheque RM5.00 per receipt and RM10.00 for\n"
            + "Letter of Indemnity stamp duty RM5.00 per cheque. RM0.15 per cheque for stamp\n"
            + "duty. Cheque processing fee of RM0.50 Foreign Currency Current Account Fees &\n"
            + "Charges Description Fees / Charges (subject to Government Tax, if applicable)\n"
            + "Transaction Fee RM10.00 or its equivalent (Charges are waived for all new and\n"
            + "active Dual Currency Investments (DCI) customers)",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Flexi Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Service Charge RM30.00 or its equivalent every half year ( June & December)\n"
            + "(Charges are waived for all new and active Dual Currency Investments (DCI)\n"
            + "customers and Foreign Currency Bond customers)",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Flexi Fixed Deposit.pdf",
            },
        ),
        Document(
            page_content="Senior Savers Flexi FD A flexible fixed deposit account for golden ager Senior\n"
            + "Savers Flexi Fixed Deposit account is designed for individuals aged 50 years and\n"
            + "above. It gives attractive interest and allows partial withdrawal anytime\n"
            + "without losing your FD interest on account balance. Earn attractive interest,\n"
            + "credited at maturity into any Brillar Savings or Current Account Earn attractive\n"
            + "interest than conventional fixed deposits. Monthly consolidated statement For\n"
            + "easy account management. Flexibility of early fixed deposit partial withdrawal\n"
            + "without losing interest on remaining balance Partial withdrawal is in multiples\n"
            + "of RM3,000. Outstanding balances will be shown on the monthly e- statement.\n"
            + "Effective 1 January 2019, no interest shall be payable on partially withdrawn\n"
            + "amounts and premature withdrawals of Senior Savers Flexi FD. Convenient\n"
            + "withdrawal You can withdraw from any branch nationwide. Eligibility • For\n"
            + "Malaysian aged 50 years old and above, single or joint names. • Minimum RM10,000\n"
            + "to open the Senior Savers Flexi FD.",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Senior Savers Flexi Fixed Deposits.pdf",
            },
        ),
        Document(
            page_content="Terms and Conditions apply. Member of PIDM. Protected by PIDM up to RM250,000\n"
            + "for each depositor. Tenure Interest Rates (p.a.) 1 month 2.15% 2 - 3 months\n"
            + "2.25% 4 - 5 months 2.30% 6 months 2.30% 7 - 11 months 2.35% 12 - 60 months 2.50%\n"
            + "Fee and charges",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Senior Savers Flexi Fixed Deposits.pdf",
            },
        ),
        Document(
            page_content="Current Account Fees & Charges Description Fees / Charges (subject to Government\n"
            + "Tax, if applicable) Cheque Related Issuance of cheque book Stamp duty of RM0.15\n"
            + "per cheque 3rd and subsequent cheque books in a calendar month RM10.00 per\n"
            + "cheque book and RM0.15 per cheque leaf Cheque Processing Fee RM0.50 per issuance\n"
            + "Dishonoured Outward Return Cheques due to: • Insufficient funds (e.g. refer to\n"
            + "drawer, effects not cleared, not arranged for, & exceeded arrangement) •\n"
            + "Technical Error (e.g. alterations) RM150.00 per cheque RM10.00 per cheque\n"
            + "Dishonoured Inward Return Cheques due to: • Post-dated reason only RM10.00 per\n"
            + "cheque (imposed on payee)",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Senior Savers Flexi Fixed Deposits.pdf",
            },
        ),
        Document(
            page_content="Postage charges for Return Cheques RM5.00 Stop Payment upon request: • On cheque\n"
            + "issued • Due to loss/ stolen cheques/ cheque book RM10.00 per cheque RM10.00 per\n"
            + "instruction Stop Payment upon presentation of stop payment cheque: • If\n"
            + "sufficient funds • If insufficient funds RM10.00 per cheque RM150.00 per cheque\n"
            + "Cheque encashment at domicile branch: • 1st party (by accountholder) encashment\n"
            + "• 3rd party encashment No charge RM2.00 per encashment (No charge for company\n"
            + "representative/s encashing cheques on behalf of the company) Cheque encashment\n"
            + "at non-domicile branch: • 1st party (by accountholder) encashment • 3rd party\n"
            + "encashment • Cheque amount RM5,000.00 and below No charge RM5.00 on payee and\n"
            + "RM2.00 on drawer RM7.00 on payee and RM2.00 on drawer",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Senior Savers Flexi Fixed Deposits.pdf",
            },
        ),
        Document(
            page_content="• Cheque amount above RM5,000.00 Destruction of uncollected Cheque Book (more\n"
            + "than 28 days): • Individual Account • Business Account RM30.00 per cheque book\n"
            + "RM50.00 per cheque book Others: • Printing special cheques • Handling Charges on\n"
            + "Representing Cheques • Redesignation of Special Account for bad cheque offenders\n"
            + "RM50.00 per printing RM50.00 per cheque RM50.00 Statement Related Statement\n"
            + "Request: • Weekly • Ad Hoc • For statement up to one year ago • For statement of\n"
            + "more than a year ago Hold Mail Request RM20.00 per month RM10.00 per request and\n"
            + "RM2.00 per page RM10.00 per request and RM5.00 per page",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Senior Savers Flexi Fixed Deposits.pdf",
            },
        ),
        Document(
            page_content="RM20.00 per month per mail (No charge for Priority and Private Banking\n"
            + "customers) Dormant Account Related Basic Current Account (No activity for 12\n"
            + "months and above): • Balance RM10.00 and below • Balance more than RM10.00\n"
            + "Dormant Current Account (No activity for 12 months and above): • Balance RM10.00\n"
            + "and below • Balance more than RM10.00 Account closed and balance absorbed as\n"
            + "charge RM10.00 yearly Account closed and balance absorbed as charge RM10.00\n"
            + "yearly Close Account Related Basic Current Account Other Current Account RM20.00\n"
            + "(within 3 months from opening) RM20.00 (within 6 months from opening)",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Senior Savers Flexi Fixed Deposits.pdf",
            },
        ),
        Document(
            page_content="Account Related • Change of operating mandate • Addition of joint accountholders\n"
            + "• Mandate for operating account RM10.00 per account RM10.00 per account Service\n"
            + "Charge RM10.00 per mandate and stamp duty RM10.00 per mandate SMS Notification\n"
            + "Related • Applicable for Brillar Bank One Account only • Applicable for all\n"
            + "account RM0.50 per SMS (no charge for first 20 SMS alerts per calendar month)\n"
            + "RM5.00 monthly for Individual account RM10.00 monthly for Non-Individual account\n"
            + "ATM Related Click for more details Debit Card Related Click for more details\n"
            + "Service Charge Related • Where average balance for half year is below RM1,000.00\n"
            + "(other than Smartlink / Flexi One/ Top Yield/ One Account) RM10.00 every half\n"
            + "year (June & December)",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Senior Savers Flexi Fixed Deposits.pdf",
            },
        ),
        Document(
            page_content="• Brillar Bank Smartlink Account where average balance for half year is below\n"
            + "RM200.00; • Brillar Bank One Account, Top Yield Account and Flexi One Account\n"
            + "where average monthly balance is below RM1,000.00; • Where average balance of\n"
            + "all the Deposit Accounts of a Priority Banking Customer fall below the minimum\n"
            + "amount for 3 consecutive months. • Deposit Accounts (Personal Fixed Deposit,\n"
            + "Personal Savings and Personal Current Account) : Below RM100,000 • Combination\n"
            + "of Deposit Accounts & Unit Trust (based on outstanding balance) : Below\n"
            + "RM200,000 RM5.00 every half year (June & December) RM5.00 per month RM50.00 (No\n"
            + "charge for Priority Banking customers with Mortgage Loan that is Personal\n"
            + "Brillar Bank Housing Loan or Shop Loan only) Brillar Bank SmartLink Account\n"
            + "Related",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Senior Savers Flexi Fixed Deposits.pdf",
            },
        ),
        Document(
            page_content="• Cash withdrawal without cheque, or • Cheque encashment performed by 1st party\n"
            + "at domicile or interbranch RM5.00 per transaction Brillar Bank One Account\n"
            + "Overdraft (OD) Facility Fee Related • Prescribed Rate (Interest payable on\n"
            + "utilisation of OD) • Excess Rate (Interest payable on overdrawn OD limit) •\n"
            + "Commitment Fee (Interest payable on unutilised OD in excess of RM250,000.00) 1%\n"
            + "p.a. above BLR on daily rest on the utilised OD amount 4% p.a. above BLR on\n"
            + "daily rest on the amount drawn in excess of the approved OD limit 1% p.a. on\n"
            + "daily rest on the unutilised OD amount. BizOne Overdraft Facility (BizOne OD)\n"
            + "Related",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Senior Savers Flexi Fixed Deposits.pdf",
            },
        ),
        Document(
            page_content="• Prescribed Rate (Interest payable on utilisation of OD) • Excess Rate\n"
            + "(Interest payable on overdrawn OD limit) • Commitment Fee (Interest payable on\n"
            + "unutilised OD in excess of RM250,000.00) • Stamp Duties • Disbursement Fees 1%\n"
            + "p.a. above 1-month BizOne FD’s prevailing board rate on daily rest on the\n"
            + "utilized OD amount. 4% p.a. above BLR on daily rest on the amount drawn in\n"
            + "excess of the approved OD limit 1% p.a. on daily rest on the unutilised OD\n"
            + "amount. As per the Stamp Duty Act 1949 (Revised 1989) Ad Valorem (0.5% on\n"
            + "approved OD amount) Disbursement Fees including but not limited to registration\n"
            + "fees (e.g. for Form 34 to be filed with the Companies Commission of Malaysia for\n"
            + "companies), and any tax or levy as per the scale fees charged by the respective\n"
            + "authorities.",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Senior Savers Flexi Fixed Deposits.pdf",
            },
        ),
        Document(
            page_content="• Legal Fees Legal fees will be incurred in relation to the stamping and\n"
            + "registration of relevant loan/security documentation. Mortgage Overdraft (OD)\n"
            + "Facility Fee Related • Excess Rate (Interest payable on Overdrawn limit) •\n"
            + "Commitment Fee (Interest payable on unutilised OD in excess of RM250,000.00) 4%\n"
            + "p.a. above BLR on daily rest on the amount drawn in excess of the approved OD\n"
            + "limit; or 6.8% p.a. above BR on daily rest on the amount drawn in excess of the\n"
            + "approved OD limit 1% p.a. on daily rest on the unutilised OD amount. Brillar\n"
            + "Bank MyPAL Related • Convenience Fee • Late Payment Fee RM15.00 per usage RM1.00\n"
            + "every 3 days, up to a maximum of RM9.00 Basic Current Account Related",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Senior Savers Flexi Fixed Deposits.pdf",
            },
        ),
        Document(
            page_content="Over-the-counter (OTC) Visits (per month): • First 6 OTC visits • From the 7th\n"
            + "OTC onwards No charge Waived until further notice Others • Sweeping from Brillar\n"
            + "Bank Flexi Fixed Deposit to Brillar Bank Flexi One account RM5.00 for every\n"
            + "RM3,000.00 swept Savings Account Fees & Charges Description Fees / Charges\n"
            + "(subject to Government Tax, if applicable) Cheque Related Dishonoured Inward\n"
            + "Return Cheques due to: • Post-dated reason only RM10.00 (No charge for Priority\n"
            + "and Private Banking customers) Passbook Related",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Senior Savers Flexi Fixed Deposits.pdf",
            },
        ),
        Document(
            page_content="Lost Savings Passbook: • Only applicable for Harvest Savings Account and Senior\n"
            + "Savers Account RM10.00 per passbook and RM10.00 for Letter of Indemnity stamp\n"
            + "duty Close Account Related Basic Savings Account Other Savings Account RM20.00\n"
            + "(within 3 months from opening) RM20.00 (within 6 months from opening) Dormant\n"
            + "Account Related Basic Savings Account (no activity 12 months and above): •\n"
            + "Balance RM10.00 and below • Balance more than RM10.00 Other Savings Account (no\n"
            + "activity 12 months and above): • Balance RM10.00 and below • Balance more than\n"
            + "RM10.00 Account closed and balance absorbed as charge RM10.00 yearly Account\n"
            + "closed and balance absorbed as charge RM10.00 yearly",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Senior Savers Flexi Fixed Deposits.pdf",
            },
        ),
        Document(
            page_content="Changes to Account Related: • Change to operating mandate • Addition of joint\n"
            + "accountholders RM10.00 per account RM10.00 per account (No charge for Priority\n"
            + "and Private Banking customers) SMS Notification Related: • Individual account •\n"
            + "Non-individual account RM5.00 monthly RM10.00 monthly Service Charge Related\n"
            + "Applicable for Pay&Save Account only • Brillar Bank Pay&Save Account where\n"
            + "average balance for half year is below RM200.00; Applicable for Priority Banking\n"
            + "customers only Average balance of the Deposit Accounts fall below the minimum\n"
            + "amount for 3 consecutive months: • Deposit Accounts (Personal Fixed Deposit,\n"
            + "Personal RM5.00 every half year (June & December) RM50.00 (No charge for\n"
            + "Priority Banking customers with Mortgage Loan that is Personal Brillar Bank\n"
            + "Housing Loan or Shop Loan only)",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Senior Savers Flexi Fixed Deposits.pdf",
            },
        ),
        Document(
            page_content="Savings and Personal Current Account) : Below RM100,000 • Combination of Deposit\n"
            + "Accounts & Unit Trust (based on outstanding balance) : Below RM300,000 ATM\n"
            + "Related Click for more details Debit Card Related Click for more details Junior\n"
            + "Savings Account Related Over the counter withdrawal: • 1st withdrawal over-the-\n"
            + "counter per month • 2nd or subsequent withdrawals over-the-counter per month No\n"
            + "charge RM2.00 per withdrawal Basic Savings Account Related Over-the-counter\n"
            + "(OTC) Visits (per month): No charge",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Senior Savers Flexi Fixed Deposits.pdf",
            },
        ),
        Document(
            page_content="• First 6 OTC visits • From the 7th OTC onwards Waived until further notice\n"
            + "Others • CDS account opening (only applicable for Pay&Save Account) RM10.00\n"
            + "Fixed Deposit Account Fees & Charges Description Fees / Charges (subject to\n"
            + "Government Tax, if applicable) Cheque Related Dishonoured Inward Return Cheques\n"
            + "due to: • Post-dated reason only RM10.00 per cheque Changes to Account Related:\n"
            + "• Change to operating mandate",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Senior Savers Flexi Fixed Deposits.pdf",
            },
        ),
        Document(
            page_content="• Addition of joint accountholders RM10.00 per account RM10.00 per account (No\n"
            + "charge for Priority Banking customers) Service Charge Related Applicable for\n"
            + "Priority Banking customers only Average balance of the Deposit Accounts fall\n"
            + "below the minimum amount for 3 consecutive months: • Deposit Accounts (Personal\n"
            + "Fixed Deposit, Personal Savings and Personal Current Account) : Below RM100,000\n"
            + "• Combination of Deposit Accounts & Unit Trust (based on outstanding balance) :\n"
            + "Below RM200,000 RM50.00 (No charge for Priority Banking customers with Mortgage\n"
            + "Loan that is Personal Brillar Housing Loan or Shop Loan only) Others Replacement\n"
            + "of lost Fixed Deposit Receipt RM5.00 per receipt and RM10.00 for Letter of\n"
            + "Indemnity stamp duty",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Senior Savers Flexi Fixed Deposits.pdf",
            },
        ),
        Document(
            page_content="Withdrawal by Banker’s Cheque RM5.00 per cheque. RM0.15 per cheque for stamp\n"
            + "duty. Cheque processing fee of RM0.50 Foreign Currency Current Account Fees &\n"
            + "Charges Description Fees / Charges (subject to Government Tax, if applicable)\n"
            + "Transaction Fee RM10.00 or its equivalent (Charges are waived for all new and\n"
            + "active Dual Currency Investments (DCI) customers) Service Charge RM30.00 or its\n"
            + "equivalent every half year ( June & December) (Charges are waived for all new\n"
            + "and active Dual Currency Investments (DCI) customers and Foreign Currency Bond\n"
            + "customers)",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Senior Savers Flexi Fixed Deposits.pdf",
            },
        ),
        Document(
            page_content="• Brillar Bank Personal Banking > • Types of Fixed Deposit Fixed Deposit Earn\n"
            + "attractive interest with fixed tenures of up to 60 months e-Fixed Deposit Place\n"
            + "your e-Fixed Deposit online via Brillar Connect Flexi Fixed Deposit Enjoy the\n"
            + "flexibility of making early partial withdrawals Senior Savers Flexi Fixed\n"
            + "Deposit An attractive interest FD account for individuals aged 50 years and\n"
            + "above Junior Fixed Deposit An attractive interest FD account for children below\n"
            + "the age of 18 Foreign Currency Fixed Deposit A convenient way to invest in\n"
            + "foreign currency",
            metadata={
                "source": "D:\\Code\\langchainjs-test\\assets\\AWS Test\\Brillar Bank_Types of Fixed Deposit.pdf",
            },
        ),
    ]

    result = ingest_data(
        documents=documents,
        embedding_model="text-embedding-3-large",
        index_name="test",
        vector_db="qdrant",
        dimension=256,
    )

    return result


ingest()
