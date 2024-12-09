# Advent of Code 2024

The questions from The Advent of Code 2024 can be found [here](https://adventofcode.com/2024/).

## Setup

A `cookies.json` file needs to be made like this in this directory (not any child directory):
```json
{
  "session": "add-session-id"
}
```

To fetch the session ID, open any puzzle's input. Then, open the Inspect menu. After that, click the Network tab. Then,
refresh the page. A `GET` request should populate. Open this request by clicking on it and find the Cookies for the
request. Then, copy the `session` cookie from here.

Alternatively, if one doesn't want to define the file or uses an incorrect session ID, the `input.txt` file can be used.
