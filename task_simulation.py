'''
This script models the workflow of crowdflower platform
 for the job of scope tagging scientific papers by crowd users.
The experiment uses synthetic data generated in the current script.

Parameters for the crowdflower synthesizer:
    test_page - number of test questions per page,
    papers_page - number of papers(excluding test questions) per page,
    n_papers - set of papers to be tagged(excluding test questions), must: n_papers % papers_page = 0,
    price_row - price per one row in dollars,
    judgment_min - min number judgments per row,
    cheaters_prop - proportion of cheaters from whole population of workers

    OUTPUT: accuracy of results, spent budget, total number of pages being paid

'''

import random
import numpy as np


# def get_accuracy(gold_data, trusted_workers_judgment):
#     total_criteria_judgments = 0.
#     correct_criteria_judgments = 0.
#     for row_id, row_gold in enumerate(gold_data):
#         for row_judgment in trusted_workers_judgment[row_id]:
#             for gold, judg in zip(row_gold, row_judgment):
#                 if gold == judg:
#                     correct_criteria_judgments += 1
#                 total_criteria_judgments += 1
#     job_accuracy = correct_criteria_judgments/total_criteria_judgments
#     return job_accuracy


def pick_worker(user_prop, user_population):
    smart_ch = user_prop[1]
    t_worker = user_prop[2]
    p_val = np.random.uniform(0.0, 1.)
    if p_val < t_worker:
        worker_trust, worker_accuracy = user_population['worker'].pop()
    elif p_val >= t_worker and p_val < t_worker + smart_ch:
        worker_trust, worker_accuracy = user_population['smart_ch'].pop()
    else:
        worker_trust, worker_accuracy = user_population['rand_ch'].pop()
    return (worker_trust, worker_accuracy)


# get current worker's trust
# def get_trust(w_page_judgment, gold_data, test_page, worker_trust, quiz_papers_n):
#     correctly_tagged_tests = 0
#     for row_id in w_page_judgment.keys()[:test_page]:
#         if gold_data[row_id] == w_page_judgment[row_id]:
#             correctly_tagged_tests += 1
#     new_trust = (worker_trust*quiz_papers_n + correctly_tagged_tests)/(quiz_papers_n + test_page)
#     return new_trust

#
# def do_judgment(worker_accuracy, gold_criteria):
#     judgment = []
#     for cr in gold_criteria:
#         if np.random.binomial(1, worker_accuracy):
#             judgment.append(cr)
#         else:
#             judgment.append(abs(cr-1))
#     return judgment


'''
each element in 'trusted_workers_judgment' is judgments of users who passed tests questions,
indexes of the trusted_workers_judgment' present row id
'''
def do_round(trust_min, test_page, papers_page, n_papers, price_row,
             gold_data, judgment_min, user_prop, user_population):
    cheaters_prop = user_prop[0] + user_prop[1]
    pages_n = n_papers / papers_page
    rows_page = test_page+papers_page
    price_page = price_row*rows_page
    budget_spent = 0.
    # budget_rest = budget
    trusted_workers_judgment = [[] for _ in range(rows_page*pages_n)]
    # number of different types of workers after completing a page
    trusted_workers_n = 0
    untrusted_workers_n = 0


    for page_id in range(pages_n):
        trust_judgment = 0
        while trust_judgment != judgment_min:
            # w_page_judgment = {}
            worker_trust, worker_accuracy = pick_worker(user_prop, user_population)

    #         for row_id in range(page_id*rows_page, page_id*rows_page+rows_page, 1):
    #             # if a worker is a cheater
    #             if np.random.binomial(1, cheaters_prop):
    #                 w_judgment = do_judgment(worker_accuracy=0.5, gold_criteria=gold_data[row_id])
    #             else:
    #                 w_judgment = do_judgment(worker_accuracy=worker_accuracy, gold_criteria=gold_data[row_id])
    #             w_page_judgment.update({row_id: w_judgment})
    #
    #         new_worker_trust = get_trust(w_page_judgment, gold_data, test_page, worker_trust, quiz_papers_n)
    #         # is a worker passed tests rows
    #         if new_worker_trust >= trust_min:
    #             # add data to trusted_workers_judgment
    #             for row_id in w_page_judgment.keys():
    #                 trusted_workers_judgment[row_id].append(w_page_judgment[row_id])
    #             trusted_workers_n += 1
    #             trust_judgment += 1
    #         else:
    #             untrusted_workers_n += 1
    #
    #         # monetary issue
    #         # budget_rest -= price_page
    #         budget_spent += price_page
    # paid_pages_n = trusted_workers_n+untrusted_workers_n
    # return (trusted_workers_judgment, budget_spent, paid_pages_n)


def do_task_scope(trust_min, test_page, papers_page, n_papers,
                  price_row, judgment_min, user_prop, user_population):
    # generate gold data
    # [paper_x] = [[gold_val], [is_easy]]
    pages_n = n_papers / papers_page
    tests_n = test_page * pages_n
    total_papers_n = tests_n + n_papers
    gold_data = [(random.randint(0, 1), random.randint(0, 1)) for _ in range(total_papers_n)]
    do_round(trust_min, test_page, papers_page, n_papers,
                price_row, gold_data, judgment_min, user_prop, user_population)

    pass
    # trusted_workers_judgment, budget_spent, paid_pages_n = first_round(trust_min, test_page, papers_page, quiz_papers_n,
    #                                                     n_papers, budget, price_row, gold_data, judgment_min, cheaters_prop)
    # job_accuracy = get_accuracy(gold_data, trusted_workers_judgment)
    # return (job_accuracy, budget_spent, paid_pages_n)