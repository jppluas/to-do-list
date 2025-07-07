import sys
import os
from behave import given, when, then
import main

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))


@given('the To-Do list is empty')
def step_empty_list(context):
    main.tasks = []


@given('the to-do list contains tasks')
def step_list_contains_tasks(context):
    main.tasks = []
    for row in context.table:
        main.add_task(row['Task'])
        if 'Status' in row.headings and row['Status'] == 'Completed':
            main.mark_completed(row['Task'])


@when('the user adds a task "{task}"')
def step_add_task(context, task):
    main.add_task(task)


@when('the user lists all tasks')
def step_list_tasks(context):
    context.output = main.list_tasks()


@when('the user marks task "{task}" as completed')
def step_mark_completed(context, task):
    main.mark_completed(task)


@when('the user clears the to-do list')
def step_clear_list(context):
    main.clear_tasks()


@when('the user deletes task "{task}"')
def step_delete_task(context, task):
    main.delete_task(task)


@when('the user searches for "{keyword}"')
def step_search_tasks(context, keyword):
    context.search_results = main.search_tasks(keyword)


@then('the to-do list should contain "{task}"')
def step_should_contain(context, task):
    task_titles = [t['title'] for t in main.tasks]
    assert task in task_titles


@then('the to-do list should not contain "{task}"')
def step_should_not_contain(context, task):
    task_titles = [t['title'] for t in main.tasks]
    assert task not in task_titles


@then('the output should contain')
def step_output_contains(context):
    expected = context.text.strip()
    actual = context.output.strip()
    assert expected == actual


@then('the to-do list should show task "{task}" as completed')
def step_task_completed(context, task):
    for t in main.tasks:
        if t['title'] == task:
            assert t['status'] == 'Completed'


@then('the to-do list should be empty')
def step_list_empty(context):
    assert len(main.tasks) == 0


@then('the search should find "{task}"')
def step_search_finds(context, task):
    found_titles = [t['title'] for t in context.search_results]
    assert task in found_titles

