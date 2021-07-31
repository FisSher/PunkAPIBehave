Feature: Getting beers with IBU 

  Scenario: Getting beers with IBU between two numbers
      Given we want to get beers using IBU between 9 and 51
      When the request is made using IBU
      Then we get the expected result 