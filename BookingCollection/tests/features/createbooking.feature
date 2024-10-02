@wip
  Feature: Create booking
    Scenario: create booking for the given user
      When the user create booking
      Then the system responds with 200
      Then the booking Id should be generated
      Then the booking details in the response should match the request