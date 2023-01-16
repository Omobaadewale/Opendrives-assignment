# Created by dell at 1/16/2023
Feature: Smoke test to verify todo app page

  Scenario: verify user can create a task on the app
    Given   open todo app page
    When    user creates a task do laundry by 8pm
    And     user completes the task
    And     user unchecks the task
    And     user deletes the todo task
    Then    verify task is deleted and left with 3

