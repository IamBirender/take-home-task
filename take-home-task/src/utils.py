from google.cloud import bigquery
import pandas as pd
client = bigquery.Client()

def check_balance(user,project_id = "take-home-task", dataset = "venmo", table = "wallet"):
    '''
    For a given user account, check balance/amount in the wallet.
    '''

    query_job = client.query(
        f"""
        SELECT * FROM `{project_id}.{dataset}.{table}` where user_name = '{user}'
        """
    )
    results = query_job.to_dataframe(progress_bar_type='tqdm') 
    return results


def make_payment(user1, user2, amount):
    '''
    Make payments from one user account to another.
    '''
    pass

def request_money(sender, receiver, amount, project_id, dataset, tablename, status):
    '''
    Request payments from other user(s)
    '''

    rows_to_insert = [
        {u"sender_id": sender, u"receiver_id": receiver, u"amount":amount, u"status": status},
    ]

    errors = client.insert_rows_json(f"{project_id}.{dataset}.{tablename}", rows_to_insert)  # Make an API request.
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))

def to_send_list(user):
    '''
    Request payments from other user(s)
    '''

    rows_to_insert = [
        {u"full_name": u"Phred Phlyntstone", u"age": 32},
        {u"full_name": u"Wylma Phlyntstone", u"age": 29},
    ]

    errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))

def recieve_from_list(user):
    '''
    Request payments from other user(s)
    '''

    rows_to_insert = [
        {u"full_name": u"Phred Phlyntstone", u"age": 32},
        {u"full_name": u"Wylma Phlyntstone", u"age": 29},
    ]

    errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))


if __name__ == '__main__':
    # project_id = "take-home-task"
    # dataset = "venmo"
    # table = "wallet"
    # # table = "transactions"
    # user= "Harry Potter"
    # print(check_balance(project_id, dataset, table, user))
    project_id = "take-home-task"
    dataset = "venmo"
    table = "transactions"
    sender= 1
    receiver = 2
    amount = 5
    status = "pending"
    request_money(sender, receiver, amount, project_id, dataset, table, status)
