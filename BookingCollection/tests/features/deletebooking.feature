@wip
  Feature: Create booking
    Scenario: create booking for the given user
      When the booking is created
      And the user deletes the booking with id
      Then the system responds with 201
      And the booking should be deleted
