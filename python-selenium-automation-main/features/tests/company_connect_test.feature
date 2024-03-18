# Created by brand at 3/17/2024
Feature: Relly.oi Company connect test

  Scenario: User clicks on “Connect the company” button and can use the form to register a new agency
    Given Open the main page
    When Log in to the page
    And Click on “Connect the company”
    And Switch the new tab
    Then Enter some test information in the form
    And Verify the right information is present
    And Verify “send request” button is available and clickable
    And Verify “buy a subscription” button is available and clickable
